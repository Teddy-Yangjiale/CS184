# CS 184/284A — 2026 计算机图形学课件库

加州大学伯克利分校 **CS 184/284A: Foundations of Computer Graphics** 官方课件整理。
整理日期：2026-11-02

---

## 先看这里

| 你的目标 | 直接去 |
|---|---|
| **系统学完一整门课** | **`sp26/` — Spring 2026 完整课程（推荐）**，索引见 `sp26/README.md` |
| **看不懂课件，需要中文逐页讲解** | **`fa26/notes/`**，入口见 `fa26/notes/README.md` |
| 跟当前最新进度 | `fa26/` — Fall 2026 当前学期，L1–L17 |
| 补秋季还没发布/没开设的专题 | `su26/` — Summer 2026，最近的往期 |
| **Final Project 选题与提案** | **`final-project/`**，入口见 `final-project/README.md` |
| 了解图形学前缘与趋势 | `Graphics-2026-Overview.md` |
| 视觉模型辅助学习 | `AI-Graphics-Tutor.md` |
| 把讲课录像转成文字 | `tools/transcribe.py`，说明见 `ASR-LOCAL.md` |

**为什么选 Spring 2026 作为完整课程**：它是完整 16 周学期，27 讲全部有对应讲义，动画 202 页、物理模拟 116 页、流体单独 56 页，深度明显高于 7 周压缩的 Summer 2026。

---

## 目录结构

```
CS184_2026/
├── sp26/                  # ★ 完整课程（Spring 2026）
│   ├── README.md          # 27 讲完整索引
│   ├── lectures/          # 19 份讲义，覆盖 L1–L27
│   └── discussions/       # D2–D14 共 20 份习题/解答
├── fa26/                  # Fall 2026 当前学期
│   ├── lectures/          # L1–L17 最新版
│   ├── discussions/       # 已发布的讨论课资料
│   └── notes/             # ★ 中文逐页讲解文档（L02 / L04–05 / L13）
├── su26/                  # Summer 2026 缺口补齐
│   ├── lectures/          # 材质、相机、模拟、颜色、IP、VR 等
│   └── discussions/       # 含 slides + worksheet + solutions
├── final-project/         # Final Project 选题库
│   ├── README.md          # 官方入口、deadline、文件索引
│   ├── topics.md          # 26 个选题完整整理
│   ├── recommendations.md # 选题推荐与避坑
│   ├── past-projects.md   # 往届 Showcase
│   ├── proposal-template.md
│   └── project-plan-4weeks.md
├── tools/                 # 本地工具
│   └── transcribe.py      # 离线语音转写（faster-whisper）
├── ASR-LOCAL.md           # 本机 ASR 环境说明
├── README.md              # 本文件
└── MANIFEST.md            # 全部 PDF 的页数/大小/SHA-256
```

---

## 一、Spring 2026 完整课程（`sp26/`）

19 份讲义覆盖 27 讲：

| 讲次 | 主题 | 文件 |
|---|---|---|
| L1 | Introduction | `SP26-L01-introduction.pdf` |
| L2 | Drawing Triangles | `SP26-L02-drawing-triangles.pdf` |
| L3 | Sampling and Aliasing | `SP26-L03-sampling-aliasing.pdf` |
| L4–5 | Transforms | `SP26-L04-05-transforms.pdf` |
| L6 | Texture Mapping | `SP26-L06-texture-mapping.pdf` |
| L7–8 | Rasterization Pipeline | `SP26-L07-08-rasterization-pipeline.pdf` |
| L9–11 | Bézier Curves and Surfaces | `SP26-L09-11-curves-surfaces.pdf` |
| L12 | Mesh Representations & Geometry Processing | `SP26-L12-meshes-geometry-processing.pdf` |
| L13 | Ray Tracing & Acceleration Structures | `SP26-L13-ray-tracing-acceleration.pdf` |
| L14 | Radiometry, Photometry & Monte Carlo | `SP26-L14a-radiometry-photometry.pdf` |
| L14 | Monte Carlo Integration（第二部分） | `SP26-L14b-monte-carlo-integration.pdf` |
| L15 | Monte Carlo Integration cont. | `SP26-L15-monte-carlo-integration.pdf` |
| L16–17 | Global Illumination & Path Tracing | `SP26-L16-17-global-illumination-path-tracing.pdf` |
| L18 | Material Modeling | `SP26-L18-material-modeling.pdf` |
| L19–20 | Color Science | `SP26-L19-20-color-science.pdf` |
| L21–23 | Animation / Motion Capture / IK | `SP26-L21-23-animation.pdf` |
| L24 | Physical Simulation | `SP26-L24-physical-simulation.pdf` |
| L25 | Fluid Simulation | `SP26-L25-fluid-simulation.pdf` |
| L26–27 | Virtual Reality | `SP26-L26-27-virtual-reality.pdf` |

完整页数、讨论课索引、学习顺序见 **`sp26/README.md`**。

说明：
- L14 官方是两份连续讲义，拆为 `L14a` / `L14b`。
- L26–27 共用一份 178 页 VR 大讲义，L27 没有单独第二份。
- Spring 2026 课表没有 B-Splines；已从 Fall 2026 网格讲义抽出 28 页，另存为 `sp26/lectures/SP26-EXTRA-b-splines-from-fa26.pdf`。

---

## 二、Fall 2026 当前学期（`fa26/`）

| 讲次 | 主题 | 文件 |
|---|---|---|
| L1 | Introduction | `L01-introduction.pdf` |
| L2 | Drawing Triangles | `L02-drawing-triangles.pdf` |
| L3 | Sampling and Aliasing | `L03-sampling-aliasing.pdf` |
| L4–5 | Transforms | `L04-05-transforms.pdf` |
| L6–7 | Perspective Projection / Texture Mapping | `L06-07-texture-mapping.pdf` |
| L8–9 | Visibility / Shading / Pipeline | `L08-09-rasterization-pipeline-shading.pdf` |
| L10 | Bézier Curves and Surfaces | `L10-bezier-curves-surfaces.pdf` |
| L11–12 | Meshes / Geometry Processing | `L11-12-meshes-geometry-processing.pdf` |
| L12b | B-Splines（在同一份网格讲义第 58–85 页） | 同上 |
| L13 | Ray Tracing & Acceleration | `L13-ray-tracing-acceleration.pdf` |
| L14 | Radiometry | `L14-radiometry.pdf` |
| L15 | Monte Carlo Integration | `L15-monte-carlo-integration.pdf` |
| L16–17 | Global Illumination & Path Tracing | `L16-17-global-illumination-path-tracing.pdf` |

### Fall 2026 缺口怎么补

| 秋季讲次 | 主题 | 补齐来源 |
|---|---|---|
| L18 | Color Science | `su26/lectures/SU26-L20-21-color-science.pdf` |
| L19 | Introduction to Animation | `su26/lectures/SU26-L19-animation-motion-capture-ik.pdf` |
| L20 | Motion Capture | 同上；加长版 `sp26/lectures/SP26-L21-23-animation.pdf` |
| L21 | Inverse Kinematics & Optimization | 同上；加长版 `sp26/lectures/SP26-L21-23-animation.pdf` |
| L22 | Physical Simulation | `su26/lectures/SU26-L18-simulation.pdf`；加长版 `sp26/lectures/SP26-L24-physical-simulation.pdf` |
| L23 | Fluid Simulation | `sp26/lectures/SP26-L25-fluid-simulation.pdf` |
| L24 | Virtual Reality | `su26/lectures/SU26-L23-virtual-reality.pdf` |
| L25 | TBD | 官方未公布，任何学期都没有对应公开讲义 |

秋季课表本身没有、但属于完整图形学课程的补充专题：

| 文件 | 主题 |
|---|---|
| `su26/lectures/SU26-L15-material-modeling.pdf` | Material Modeling |
| `su26/lectures/SU26-L16-17-cameras-lenses.pdf` | Cameras & Lenses |
| `su26/lectures/SU26-L22-image-processing.pdf` | Image Processing |
| `su26/lectures/SU26-L27-exam-2-review.pdf` | Exam 2 Review |

---

## 三、Summer 2026 缺口补齐（`su26/`）

Summer 2026 是 Fall 2026 之前最近的一期，用于补秋季尚未发布的专题。

### 讲义

| 文件 | SU26 讲次 | 主题 | 页数 |
|---|---|---:|---:|
| `SU26-L15-material-modeling.pdf` | L15 | Material Modeling | 98 |
| `SU26-L16-17-cameras-lenses.pdf` | L16–17 | Cameras & Lenses | 132 |
| `SU26-L18-simulation.pdf` | L18 | Physical Simulation + Fluid | 83 |
| `SU26-L19-animation-motion-capture-ik.pdf` | L19 | Animation / MoCap / IK | 81 |
| `SU26-L20-21-color-science.pdf` | L20–21 | Color Science | 175 |
| `SU26-L22-image-processing.pdf` | L22 | Image Processing | 61 |
| `SU26-L23-virtual-reality.pdf` | L23 | Virtual Reality | 154 |
| `SU26-L27-exam-2-review.pdf` | L27 | Exam 2 Review | 19 |

### 讨论课（含 slides）

| 文件 | 内容 |
|---|---|
| `SU26-D08-probability-monte-carlo-{slides,worksheet,solutions}.pdf` | 概率与蒙特卡洛估计 |
| `SU26-D09-material-modeling-{slides,worksheet,solutions}.pdf` | 材质建模 |
| `SU26-D10-cameras-{slides,worksheet,solutions}.pdf` | 相机与镜头 |
| `SU26-D11-color-{slides,worksheet,solutions}.pdf` | 颜色 |

---

## 四、讨论课资料汇总

### Spring 2026（完整课程配套，`sp26/discussions/`）

D2 三角形与采样、D3 变换与纹理、D4 纹理与管线、D5 样条曲线、D6 半边与光线追踪、D7 光线追踪、D8 光度学与蒙特卡洛、D10 全局光照与材质、D12 颜色、D13 模拟/运动学/动画、D14 VR 与图像传感器。

### Fall 2026（`fa26/discussions/`）

D2、D3、D4–5、D6、D7、D8 Exam 1 Review、D9 光度学与蒙特卡洛（官方解答 404）、D10 全局光照与材质。

### Summer 2026（`su26/discussions/`）

D08 概率/蒙特卡洛、D09 材质、D10 相机、D11 颜色，均含 slides + worksheet + solutions。

> 部分讨论课 slides 托管在 Google Slides，需要 Berkeley 账号登录；本库只包含公开可下载的 PDF。

---

## 五、建议学习路线（按 Spring 2026 完整课程）

1. **光栅化基础（L1–L8）**
   采样 → 走样/抗锯齿 → 变换/投影 → 纹理 → 光栅化管线与着色。
   配套 Homework 1：软光栅器。
2. **几何建模（L9–L12）**
   Bézier 曲线曲面 → 网格表示与半边结构 → 几何处理。
   配套 Homework 2。
3. **光线追踪与全局光照（L13–L17）**
   光线求交/BVH → 辐射度量 → 蒙特卡洛积分 → 路径追踪。
   配套 Homework 3。
4. **材质与颜色（L18–L20）**
   BRDF/微表面 → 颜色感知 → 色彩空间。
5. **动画与模拟（L21–L25）**
   动画/运动学 → Motion Capture → IK → 物理模拟 → 流体。
   配套 Homework 4。
6. **VR（L26–L27）**

## 六、官方资源

- Spring 2026 完整课程主页：<https://cs184.eecs.berkeley.edu/sp26>
- Fall 2026 当前课程主页：<https://cs184.eecs.berkeley.edu/fa26>
- Summer 2026 主页：<https://cs184.eecs.berkeley.edu/su26>
- 作业：
  - [Homework 0](https://cs184.eecs.berkeley.edu/sp26/hw/hw0/)
  - [Homework 1](https://cs184.eecs.berkeley.edu/sp26/hw/hw1/)
  - [Homework 2](https://cs184.eecs.berkeley.edu/sp26/hw/hw2/)
  - [Homework 3](https://cs184.eecs.berkeley.edu/sp26/hw/hw3/)
  - [Homework 4](https://cs184.eecs.berkeley.edu/sp26/hw/hw4/)
- [Supplemental Readings](https://cs184.eecs.berkeley.edu/sp26/resources/readings/)
- [Math Resources](https://cs184.eecs.berkeley.edu/sp26/resources/math-resources/)
- [CGL Library Primer](https://cs184.eecs.berkeley.edu/sp26/resources/cgl-primer/)

## 七、推荐教材

- *Fundamentals of Computer Graphics*, 5th ed. — Shirley, Marschner
- *Computer Graphics: Principles and Practice*, 3rd ed. — Hughes, van Dam, et al.
- *Physically Based Rendering: From Theory to Implementation*, 4th ed. — Pharr, Jakob, Humphreys
  免费在线版：<https://pbr-book.org/>

## 八、备注

- 所有 PDF 均来自课程官网公开链接，仅供个人学习；版权归 UC Berkeley 及授课教师所有。
- `MANIFEST.md` 记录每份 PDF 的页数、大小和 SHA-256 前 16 位，可用于校验完整性。
- Spring 2026 的 B-Splines 未单独开设，可从 Fall 2026 网格讲义补；Fall 2026 的 L25 主题尚未公布。
