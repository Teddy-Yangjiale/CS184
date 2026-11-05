# CS 184/284A — Spring 2026 完整课程

这是本库中**首选的完整课程套装**：2026 春季完整 16 周学期，共 27 讲。
课程主页：<https://cs184.eecs.berkeley.edu/sp26>

- 讲义：19 份 PDF，覆盖 L1–L27（同一主题多讲共用一份讲义）
- 讨论课：D2–D14，共 20 份 worksheet / solutions
- 所有文件均已验证可打开

---

## 讲义索引

| 讲次 | 主题 | 文件 | 页数 |
|---|---|---|---:|
| L1 | Introduction | `lectures/SP26-L01-introduction.pdf` | 109 |
| L2 | Drawing Triangles | `lectures/SP26-L02-drawing-triangles.pdf` | 70 |
| L3 | Sampling and Aliasing | `lectures/SP26-L03-sampling-aliasing.pdf` | 118 |
| L4–5 | Transforms | `lectures/SP26-L04-05-transforms.pdf` | 305 |
| L6 | Texture Mapping | `lectures/SP26-L06-texture-mapping.pdf` | 173 |
| L7–8 | Rasterization Pipeline | `lectures/SP26-L07-08-rasterization-pipeline.pdf` | 139 |
| L9–11 | Bézier Curves and Surfaces | `lectures/SP26-L09-11-curves-surfaces.pdf` | 203 |
| L12 | Mesh Representations & Geometry Processing | `lectures/SP26-L12-meshes-geometry-processing.pdf` | 85 |
| L13 | Ray Tracing & Acceleration Structures | `lectures/SP26-L13-ray-tracing-acceleration.pdf` | 91 |
| L14 | Radiometry, Photometry & Monte Carlo | `lectures/SP26-L14a-radiometry-photometry.pdf` | 59 |
| L14 | Monte Carlo Integration（同讲第二部分） | `lectures/SP26-L14b-monte-carlo-integration.pdf` | 71 |
| L15 | Monte Carlo Integration cont. | `lectures/SP26-L15-monte-carlo-integration.pdf` | 114 |
| L16–17 | Global Illumination & Path Tracing | `lectures/SP26-L16-17-global-illumination-path-tracing.pdf` | 227 |
| L18 | Material Modeling | `lectures/SP26-L18-material-modeling.pdf` | 118 |
| L19–20 | Color Science | `lectures/SP26-L19-20-color-science.pdf` | 112 |
| L21–23 | Animation / Motion Capture / IK | `lectures/SP26-L21-23-animation.pdf` | 202 |
| L24 | Physical Simulation | `lectures/SP26-L24-physical-simulation.pdf` | 116 |
| L25 | Fluid Simulation | `lectures/SP26-L25-fluid-simulation.pdf` | 56 |
| L26–27 | Virtual Reality | `lectures/SP26-L26-27-virtual-reality.pdf` | 178 |

### 说明

- L14 官方给的是两份连续讲义（Radiometry/Photometry + Monte Carlo），所以拆成 `L14a`、`L14b`。
- L15 的“Monte Carlo Integration cont.”使用另一份 114 页讲义。
- L26–27 的 VR 只有一份 178 页大讲义，覆盖两讲内容；L27 官方没有单独上传第二份。
- Spring 2026 课表没有 B-Splines 专题；已从 Fall 2026 网格讲义抽出 28 页，另存为 `lectures/SP26-EXTRA-b-splines-from-fa26.pdf`，方便直接学习。

---

## 讨论课索引

| 讨论课 | 主题 | 文件 |
|---|---|---|
| D2 | Triangles and Sampling | `discussions/SP26-D02-triangles-sampling-{worksheet,solutions}.pdf` |
| D3 | Transforms and Texture Mapping | `discussions/SP26-D03-transforms-texture-{worksheet,solutions}.pdf` |
| D4 | Texture Mapping and Graphics Pipeline | `discussions/SP26-D04-texture-pipeline-{worksheet,solutions}.pdf` |
| D5 | Splines and Curves | `discussions/SP26-D05-splines-curves-{worksheet,solutions}.pdf` |
| D6 | Half Edges and Ray Tracing | `discussions/SP26-D06-half-edges-ray-tracing-{worksheet,solutions}.pdf` |
| D7 | Ray Tracing | `discussions/SP26-D07-ray-tracing-{worksheet,solutions}.pdf` |
| D8 | Photometry and Monte Carlo Integration | `discussions/SP26-D08-photometry-monte-carlo-{worksheet,solutions}.pdf` |
| D10 | Global Illumination and Materials | `discussions/SP26-D10-global-illumination-materials-{worksheet,solutions}.pdf` |
| D12 | Color | `discussions/SP26-D12-color-{worksheet,solutions}.pdf` |
| D13 | Simulation, Kinematics, Animation | `discussions/SP26-D13-simulation-kinematics-animation-worksheet.pdf` |
| D14 | VR and Image Sensors | `discussions/SP26-D14-vr-image-sensors-worksheet.pdf` |

缺失说明：
- D9（Exam 1 Review）官方只提供 Google Slides，需要 Berkeley 登录。
- D13 官方“solutions”链接实际指向 worksheet 本身。
- D14 官方只提供 worksheet。
- 部分讨论课 slides 托管在 Google Slides，未包含在此。

---

## 推荐学习顺序

1. L1–L8：采样、走样、变换、纹理、光栅化管线
2. L9–L12：Bézier 曲线曲面、网格与几何处理
3. L13–L17：光线追踪、辐射度量、蒙特卡洛、路径追踪
4. L18–L20：材质建模、颜色科学
5. L21–L25：动画、MoCap、IK、物理模拟、流体
6. L26–L27：VR

配套作业：
- Homework 1：软光栅器（L1–L8）
- Homework 2：曲线曲面 + 半边网格（L9–L12）
- Homework 3：路径追踪器（L13–L17）
- Homework 4：弹簧-质点 + shader（L21–L24）

作业说明：<https://cs184.eecs.berkeley.edu/sp26/hw/hw1/>

---

## 备注

所有 PDF 均来自课程官网公开链接，仅供个人学习；版权归 UC Berkeley 及授课教师所有。
