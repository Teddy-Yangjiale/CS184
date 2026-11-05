#!/usr/bin/env python
"""CS184 本地语音转写工具（faster-whisper，完全离线）

用法
----
    # 单个文件
    python transcribe.py lecture.mp4

    # 指定模型与语言
    python transcribe.py lecture.mp4 --model small --lang en

    # 处理整个目录里所有音视频
    python transcribe.py "D:\\videos\\cs184" --model medium

    # 直接从 URL 抓音频（ffmpeg 内部处理，B站/YouTube 需先拿到直链）
    python transcribe.py "https://...mp4" --ss 120 --duration 600

输出
----
    与输入同名的 .txt（纯文本）和 .srt（带时间轴字幕），
    默认写在输入文件旁边；用 --out 指定输出目录。

依赖
----
    faster-whisper、ffmpeg、已下载的模型权重（见 ASR-LOCAL.md）
"""

import argparse
import os
import subprocess
import sys
import tempfile

# 在 Windows 上，Anaconda 的 MKL 与 ctranslate2 会各带一份 libiomp5md.dll，
# 导致 "OMP: Error #15"。必须在 import faster_whisper 之前设置。
os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

AUDIO_EXT = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac", ".wma", ".opus"}
VIDEO_EXT = {".mp4", ".mkv", ".webm", ".mov", ".avi", ".flv", ".ts", ".m4v"}
MEDIA_EXT = AUDIO_EXT | VIDEO_EXT

MODEL_CACHE = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "hub")


def find_local_model(name: str) -> str | None:
    """在 HF 缓存里找已下载的 faster-whisper 权重，返回 snapshot 目录。"""
    repo = os.path.join(MODEL_CACHE, f"models--Systran--faster-whisper-{name}")
    snapshots = os.path.join(repo, "snapshots")
    if not os.path.isdir(snapshots):
        return None
    # 优先带 refs/main 指向的那个，否则取第一个含 model.bin 的
    for entry in os.listdir(snapshots):
        candidate = os.path.join(snapshots, entry)
        if os.path.isfile(os.path.join(candidate, "model.bin")):
            return candidate
    return None


def load_model(name: str, compute_type: str):
    from faster_whisper import WhisperModel

    local = find_local_model(name)
    if local:
        print(f"[model] 使用本地权重: {local}", flush=True)
        return WhisperModel(local, device="cpu", compute_type=compute_type)

    print(f"[model] 本地无 {name}，尝试从 HuggingFace 下载…", flush=True)
    return WhisperModel(name, device="cpu", compute_type=compute_type)


def extract_audio(src: str, ss: str | None, duration: str | None) -> str:
    """用 ffmpeg 把任意音视频（或 URL）转成 16kHz 单声道 wav。"""
    fd, wav = tempfile.mkstemp(suffix=".wav")
    os.close(fd)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    if ss:
        cmd += ["-ss", str(ss)]
    if duration:
        cmd += ["-t", str(duration)]
    cmd += ["-i", src, "-vn", "-ar", "16000", "-ac", "1", wav]
    subprocess.run(cmd, check=True)
    return wav


def srt_ts(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def transcribe_one(model, path: str, args) -> None:
    print(f"\n=== {os.path.basename(path)} ===", flush=True)
    wav = extract_audio(path, args.ss, args.duration)
    try:
        segments, info = model.transcribe(
            wav,
            language=args.lang,
            beam_size=args.beam_size,
            vad_filter=not args.no_vad,
            initial_prompt=args.prompt,
        )
        print(
            f"[info] 语言={info.language} 置信度={info.language_probability:.2f} "
            f"时长={info.duration:.1f}s",
            flush=True,
        )

        stem = os.path.splitext(os.path.basename(path))[0]
        out_dir = args.out or os.path.dirname(os.path.abspath(path))
        os.makedirs(out_dir, exist_ok=True)
        txt_path = os.path.join(out_dir, stem + ".txt")
        srt_path = os.path.join(out_dir, stem + ".srt")

        lines, srt_blocks, n = [], [], 0
        for seg in segments:
            text = seg.text.strip()
            if not text:
                continue
            n += 1
            lines.append(text)
            srt_blocks.append(
                f"{n}\n{srt_ts(seg.start)} --> {srt_ts(seg.end)}\n{text}\n"
            )
            if args.verbose:
                print(f"  [{seg.start:7.1f}s] {text}", flush=True)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        with open(srt_path, "w", encoding="utf-8") as f:
            f.write("\n".join(srt_blocks))

        print(f"[done] {n} 段 -> {txt_path}", flush=True)
        print(f"[done] 字幕 -> {srt_path}", flush=True)
    finally:
        try:
            os.remove(wav)
        except OSError:
            pass


def main() -> int:
    ap = argparse.ArgumentParser(
        description="本地离线语音转写（faster-whisper）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("input", help="音视频文件、URL，或包含多媒体的目录")
    ap.add_argument("--model", default="medium", help="small / medium（默认 medium）")
    ap.add_argument("--lang", default=None, help="语言代码，如 en / zh；默认自动检测")
    ap.add_argument("--out", default=None, help="输出目录")
    ap.add_argument("--compute-type", default="int8", help="int8（默认，快）/ float32（准）")
    ap.add_argument("--beam-size", type=int, default=5)
    ap.add_argument("--ss", default=None, help="起始时间（秒或 HH:MM:SS），只转一段时用")
    ap.add_argument("--duration", default=None, help="转写时长（秒）")
    ap.add_argument("--prompt", default=None, help="初始提示词，可给专有名词纠错")
    ap.add_argument("--no-vad", action="store_true", help="关闭静音检测")
    ap.add_argument("--verbose", action="store_true", help="逐段打印")
    args = ap.parse_args()

    targets = []
    if os.path.isdir(args.input):
        for name in sorted(os.listdir(args.input)):
            if os.path.splitext(name)[1].lower() in MEDIA_EXT:
                targets.append(os.path.join(args.input, name))
        if not targets:
            print(f"[error] 目录里没有音视频文件: {args.input}", file=sys.stderr)
            return 1
    elif os.path.isfile(args.input) or args.input.startswith(("http://", "https://")):
        targets = [args.input]
    else:
        print(f"[error] 找不到输入: {args.input}", file=sys.stderr)
        return 1

    model = load_model(args.model, args.compute_type)
    for path in targets:
        transcribe_one(model, path, args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
