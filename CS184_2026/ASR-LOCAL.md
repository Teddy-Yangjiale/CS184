# 本机 ASR 环境说明（离线语音转写）

> 核查日期：2026-11-05
> 用途：把讲课录像/音频转成文字，用于核对讲解文档、补逐字稿

---

## 一、结论：可以离线跑，已验证

| 项目 | 状态 |
|---|---|
| 推理框架 | `faster-whisper 1.2.1`（基于 CTranslate2）✅ |
| Python | Anaconda `D:\Anaconda\python.exe`，3.13.5 ✅ |
| 模型权重 | `faster-whisper-medium`（1.46 GB）、`faster-whisper-small`（461 MB），**均已缓存到本地** ✅ |
| 音频解码 | `ffmpeg 8.1.2`（winget: Gyan.FFmpeg）✅ |
| 联网需求 | **无**。权重已在本地，全程离线 ✅ |
| 实测结果 | 模型加载 3.5 s；真实课堂音频转写正常，中英混读可识别 ✅ |

**缺的东西**（不影响上述流程）：

| 组件 | 说明 |
|---|---|
| `openai-whisper` | 官方实现，已被 faster-whisper 替代，不需要 |
| `funasr` / `vosk` / `sherpa-onnx` | 其他 ASR 方案，未安装；中文场景 funasr 效果更好，但需另外下载 |
| `transformers` | 未安装（本流程不依赖） |
| `yt-dlp` | 未安装。若要直接从 B站/YouTube 抓音轨，需要它，或按下方"URL 抓取"手动拿直链 |

---

## 二、快速开始

```powershell
# 转写单个文件（自动识别语言）
& D:\Anaconda\python.exe D:\CS184\CS184_2026\tools\transcribe.py D:\videos\lecture02.mp4

# 指定模型、语言、输出目录，并打印每段
& D:\Anaconda\python.exe D:\CS184\CS184_2026\tools\transcribe.py lecture02.mp4 `
    --model medium --lang en --out D:\CS184\transcripts --verbose

# 只转某一段（例如从 2 分 30 秒起、转 10 分钟）
& D:\Anaconda\python.exe D:\CS184\CS184_2026\tools\transcribe.py lecture02.mp4 --ss 150 --duration 600

# 批量处理一个目录
& D:\Anaconda\python.exe D:\CS184\CS184_2026\tools\transcribe.py D:\videos\cs184 --model medium
```

输出：与输入同名的 `.txt`（纯文本）和 `.srt`（带时间轴字幕）。

---

## 三、必须知道的两个坑

### 坑 1：`OMP: Error #15`

Anaconda 的 MKL 和 CTranslate2 各带一份 `libiomp5md.dll`，同时加载会崩：

```
OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.
```

**解决**：设置环境变量（`tools/transcribe.py` 里已经内置，无需手动处理）

```powershell
$env:KMP_DUPLICATE_LIB_OK='TRUE'
```

若你直接写 Python 脚本调 faster-whisper，**必须在 `import faster_whisper` 之前**设置。

### 坑 2：开头大段静音 → 转写结果为空

课堂录像开头常有 1–3 分钟的空场、调试、等人。配合 `vad_filter`（默认开启）时，这段会被全部过滤，**如果取样窗口正好落在静音区，会得到 0 段**——这不是脚本坏了。

**排查方法**：用 `--no-vad` 再跑一遍；或用 ffmpeg 看音量包络：

```powershell
ffmpeg -i input.wav -af volumedetect -f null - 2>&1 | Select-String "mean_volume"
```

实测例子：某 B站讲次前 150 秒全静音，人声从 150 s 才开始。

---

## 四、模型怎么选

| 模型 | 体积 | 速度（CPU, int8） | 适用 |
|---|---:|---|---|
| `small` | 461 MB | 很快 | 快速定位内容、抓关键词 |
| `medium` | 1.46 GB | 约 1/4 实时 | 正式逐字稿（默认推荐） |

本机 **没有** `large-v3`。若要更高准确率（尤其带口音或专业术语密集时），可以只下载一次：

```powershell
& D:\Anaconda\python.exe -c "from faster_whisper import WhisperModel; WhisperModel('large-v3', device='cpu', compute_type='int8')"
# 约 3 GB 权重，会缓存到 %USERPROFILE%\.cache\huggingface\hub\
```

> 纯 CPU 下 `large-v3` 明显慢（约为 `medium` 的 2–3 倍耗时）。若机器有 NVIDIA 显卡，把 `tools/transcribe.py` 里的 `device='cpu'` 改成 `'cuda'`、`compute_type='int8'` 改成 `'float16'`，速度可提升一个数量级。

### 提升专业术语准确率

用 `--prompt` 给一段术语表，能显著减少专有名词错拼：

```powershell
... transcribe.py l13.mp4 --prompt "CS184 computer graphics. Terms: rasterization, barycentric, Blinn-Phong, BVH, SAH, Möller-Trumbore, KD-tree, radiance, BRDF."
```

---

## 五、直接从 URL 抓音轨

`transcribe.py` 支持传 URL（内部走 ffmpeg）。但 B站/YouTube 的页面地址不是媒体直链，需要先拿到直链。

**B站**：用 playurl 接口取 `durl[0].url`（`fnval=1&qn=16` 即可，无需登录），再配合 `Referer: https://www.bilibili.com/` 请求头：

```powershell
# 示例：抓第 2 讲的 2:00–4:00
ffmpeg -headers "Referer: https://www.bilibili.com/`r`nUser-Agent: Mozilla/5.0`r`n" `
  -ss 120 -t 120 -i "<playurl 拿到的 .mp4 直链>" -vn -ar 16000 -ac 1 seg.wav
```

**YouTube**：需要 `yt-dlp`（未安装）。可 `pip install yt-dlp` 后：

```powershell
yt-dlp -f "bestaudio" -o "lecture.%(ext)s" "https://www.youtube.com/watch?v=..."
```

---

## 六、一段完整示例：给 B站某讲生成逐字稿

```powershell
$py = 'D:\Anaconda\python.exe'
$tool = 'D:\CS184\CS184_2026\tools\transcribe.py'

# 1) 取 B站直链（BV119Hk6QEPs 第 09 讲）
$bv = 'BV119Hk6QEPs'
$view = Invoke-RestMethod "https://api.bilibili.com/x/web-interface/view?bvid=$bv" `
          -Headers @{'User-Agent'='Mozilla/5.0'; 'Referer'='https://www.bilibili.com/'}
$cid = $view.data.pages[8].cid

$play = Invoke-RestMethod "https://api.bilibili.com/x/player/playurl?bvid=$bv&cid=$cid&fnval=1&qn=16" `
          -Headers @{'User-Agent'='Mozilla/5.0'; 'Referer'='https://www.bilibili.com/'}
$url = $play.data.durl[0].url

# 2) 抽取音轨（B站需要 Referer 头）
ffmpeg -y -loglevel error `
  -headers "Referer: https://www.bilibili.com/`r`nUser-Agent: Mozilla/5.0`r`n" `
  -i $url -vn -ar 16000 -ac 1 "$env:TEMP\p09.wav"

# 3) 转写
& $py $tool "$env:TEMP\p09.wav" --model medium --lang en --out D:\CS184\transcripts --verbose
```

---

## 七、性能参考（本机实测）

| 操作 | 耗时 |
|---|---|
| 加载 `medium`（int8, CPU） | 3.5 s |
| 转写 7 分钟音频（`medium`, beam=1） | 约 1.5–2 分钟 |
| 转写 7 分钟音频（`small`, beam=1） | 约 30–40 秒 |

按此估算：**一讲 80 分钟的课，`medium` 约需 20 分钟**。整门课 27 讲 ≈ 9 小时，可挂后台批量跑。

---

*相关文件：[`tools/transcribe.py`](tools/transcribe.py)、[`fa26/notes/README.md`](fa26/notes/README.md)*
