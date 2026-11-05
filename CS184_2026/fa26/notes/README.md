# fa26 讲解文档（已迁移）

**逐页讲解文档已迁移到个人笔记站**（本地仓库 `D:\notes`，线上 `teddy-yangjiale.github.io/notes`），专栏 id `cs184`。

| 讲次 | 笔记站路径 | 状态 |
|---|---|---|
| L02 Drawing Triangles（光栅化 = 采样） | `/cs184-02-drawing-triangles/` | ✅ |
| L04–05 Transforms（变换） | `/cs184-04-05-transforms/` | 待写 |
| L13 Ray Tracing & Acceleration | `/cs184-13-ray-tracing/` | 待写 |

> 本目录原来的三篇 Markdown 草稿（旧格式：逐页纯文字、无截图、无图解）已删除，避免与笔记站版本冲突。
>
> 新格式的写作与图解规范见笔记站仓库的 `scripts/cs184-notes-standard.md`。

---

## 附：配套录课现状（保留备查）

### 官方渠道不可公开访问

UC Berkeley CS184 的**正课录像不在公开 YouTube 上**。核实结果：

| 检查点 | 结果 |
|---|---|
| [cs184.eecs.berkeley.edu/sp26](https://cs184.eecs.berkeley.edu/sp26)、[fa26](https://cs184.eecs.berkeley.edu/fa26) | 只挂 PDF 讲义链接，**无任何视频链接** |
| [官方录课存档页](https://inst.eecs.berkeley.edu/~cs184/fa12/onlinelectures.html) | 被 **CalNet 登录墙**挡住（需 Berkeley 账号） |
| YouTube 搜索 `CS184` | 只有 `Cs184 Departmental` 频道的 TA Discussion / Exam Review，无正课录像 |
| B站搜索 `CS184` / `CS184 2026` / `CS184 fa26` / `CS184 sp26` | **没有 2026 版**；最新是 **22SP** |

### B站 22SP 两个镜像

| 镜像 | UP 主 | 分P | 特点 |
|---|---|---:|---|
| [BV1qR4y1y7tu](https://www.bilibili.com/video/BV1qR4y1y7tu) | RubatoTheEmber | 22 | 分P带正式讲次名；UP 自述「少了几集」 |
| [BV119Hk6QEPs](https://www.bilibili.com/video/BV119Hk6QEPs) | GPT中英字幕课程资源 | 25 | 分P只叫「第NN讲」，多出的 3 讲不是光追 |

**分P对照（已用本机 ASR 实测核对内容，不是凭标题推断）**：

| fa26 讲次 | BV1qR4y1y7tu | BV119Hk6QEPs |
|---|---|---|
| L01 Introduction | [P1](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=1) | 第01讲 |
| **L02 Drawing Triangles** | [**P2**](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=2) | 第02讲 |
| L03 Sampling & Aliasing | [P3](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=3) | 第03讲 |
| **L04–05 Transforms** | [**P4**](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=4) | 第04讲 |
| L06 Texture Mapping | [P5](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=5) | 第05讲 |
| L07–08 Rasterization Pipeline | [P6](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=6) | 第06讲 |
| L10 Bézier Curves | ❌ 缺 | 第09讲（ASR：bezier / spline） |
| **L13 Ray Tracing & Acceleration** | ❌ 缺 | ❌ **缺** |
| L14 Radiometry | [P7](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=7) | 第11讲 |
| L15 Monte Carlo | [P8](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=8) | 第12讲 |
| L16–17 Global Illumination | [P9](https://www.bilibili.com/video/BV1qR4y1y7tu/?p=9) | 第13讲 |

**两点别被编号骗了**：

1. **22SP 与 fa26 讲次不对应**。fa26 把光追放 L13，22SP 课程顺序不同。**按主题对照，不要按编号对照**。
2. **BV119Hk6QEPs 多出的第 07–09 讲不是光追**。ASR 抽样结果：第07 讲是程序化/实体纹理 + 帧缓冲深度；第08 讲是 Blinn-Phong 着色回顾；第09 讲是 Bézier 曲线。且该镜像**第 10 讲缺失**。

**结论：两个镜像都没有公开的光线追踪正课。** L13 的替代视频建议用 B站 [GAMES101 P13](https://www.bilibili.com/video/BV1X7411F744/?p=13) + [P14](https://www.bilibili.com/video/BV1X7411F744/?p=14)（同为 Whitted / BVH / SAH 术语体系）。

### 需要逐字稿时

本机有可离线运行的 ASR 环境，说明见 [../../ASR-LOCAL.md](../../ASR-LOCAL.md)，脚本见 [../../tools/transcribe.py](../../tools/transcribe.py)。

```powershell
# 转写本地音视频（输出同名 .txt + .srt）
& D:\Anaconda\python.exe D:\CS184\CS184_2026\tools\transcribe.py lecture.mp4 --model medium --lang en
```

注意课堂录像开头常有 1–3 分钟静音，取样窗口落在静音区会得到空结果（`ASR-LOCAL.md` 的「坑 2」）。
