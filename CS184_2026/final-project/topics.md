# 官方选题完整整理（Fall 2026）

来源：<https://cs184.eecs.berkeley.edu/fa26/project/ideas/>
共 **8 大类、26 个选题**。难度为官方标注；`—` 表示官方未标。

> 说明：下面的「4 人 4 周推荐度」和「分工建议」是本整理根据官方难度、课程进度和往届 Showcase 做的经验判断，不是官方评分标准。

---

## 总览

| # | 类别 | 选题 | 官方难度 | 4 人推荐度 |
|---:|---|---|---:|---|
| 1 | Rendering | Rendering Volumetric Scattering | 2.0 | ★★★★★ |
| 2 | Rendering | Progressive Photon Mapping | 2.5 | ★★★★ |
| 3 | Rendering | Bidirectional Path Tracing & MIS | 2.5 | ★★★★ |
| 4 | Rendering | Add Texture Support to Homework Framework | 1.5 | ★★★ |
| 5 | Rendering | Non-Photorealistic Rendering | 1.5 | ★★★ |
| 6 | Rendering | Pathtracing Lenses & Contrast-based Autofocus | 2.0 | ★★★★ |
| 7 | Rendering | Speeding up the Ray Tracer | 1.0–3.0 | ★★★ |
| 8 | Material | Subsurface Scattering | 2.0 | ★★★★★ |
| 9 | Material | Rendering Glints | 2.5 | ★★★★ |
| 10 | Material | Iridescent / Wavelength-dependent Path Tracing | — | ★★★★ |
| 11 | Material | Cloth Rendering | 2.0 | ★★★★ |
| 12 | Real-time | Shaders and Shaders Only | 1.5–2.5 | ★★★ |
| 13 | Real-time | Cloth Simulation using GPU Shader / CUDA | 2.0 | ★★★★★ |
| 14 | Real-time | GPU Path Tracer using NVIDIA OptiX | 2.0 | ★★★★★ |
| 15 | Real-time | Visual / Rendering Mods for Games | 1.5–3.5 | ★★ |
| 16 | Real-time | Game / Interactive Demo | 2.0 | ★★★ |
| 17 | Rasterization | Font Rendering | 2.0 | ★★★★ |
| 18 | Texture | Solid Texture Synthesis | 1.5 | ★★★ |
| 19 | Geometry | Mesh Simplification & Remeshing | 1.5 | ★★★ |
| 20 | Geometry | Point Cloud to Mesh | 2.0 | ★★★★ |
| 21 | Geometry | Alternate Subdivision Schemes | 1.5 | ★★★ |
| 22 | Geometry | Remeshing / Mesh Regularization | 1.5 | ★★★ |
| 23 | Imaging | Light Field Camera Support | 1.5 | ★★★★★ |
| 24 | Imaging | Multi-shot HDR | 2.0 | ★★★ |
| 25 | Animation | 2D Grid Based Fluid Dynamics Simulation | 2.0 | ★★★★★ |
| 26 | Animation | Animation using Spatial Keyframing | 2.0 | ★★★ |

---

# Rendering

## 1. Rendering Volumetric Scattering — 2.0

**核心任务**：把 Homework 3 的表面路径追踪扩展成体积渲染。光线在击中表面前就可能被介质散射，需要同时处理表面积分和体积积分。

**必须做**
- 在 path tracer 中加入 participating media
- 实现 homogeneous / heterogeneous 介质的 ray marching 或自由程采样
- 至少支持一种 phase function（Henyey-Greenstein 或 isotropic）
- 渲染雾、烟、云、大气等效果

**加分**
- 体积光/god rays
- 多次散射近似
- 与表面材质正确耦合

**关联课程**：L14–L17 辐射度量、蒙特卡洛、路径追踪
**关键参考**
- Jarosz thesis 第 4 章：<https://cs.dartmouth.edu/~wjarosz/publications/dissertation/chapter4.pdf>
- Lafortune & Willems 实现细节：<http://luthuli.cs.uiuc.edu/~daf/courses/rendering/papers/lafortune96rendering.pdf>
- 大气散射：<https://cseweb.ucsd.edu/~ravir/papers/singlescat/scattering.pdf>

**4 人分工建议**
1. 介质采样与自由程
2. 体积渲染方程 / phase function
3. 场景与材质（雾、云、烟）
4. 验证、性能、对比图与视频

**风险**：体积渲染噪声大，必须做重要性采样，否则出图很慢。

---

## 2. Progressive Photon Mapping — 2.5

**核心任务**：实现 photon mapping，重点解决 path tracing 很难渲染的 caustics（焦散）。

**必须做**
- Photon emission / tracing
- 光子空间查询结构：KD-tree 或 hash grid
- Radiance estimate（球形邻域）
- Progressive photon mapping 降低偏差

**加分**
- 与 path tracer 结果对比
- 玻璃、水面、棱镜等 caustics 场景
- 光子可视化

**关键参考**
- PBRT 第 15.6 节（photon mapping）
- Progressive photon mapping 论文：<http://dl.acm.org/citation.cfm?id=1409083>

**4 人分工建议**
1. 光子发射与追踪
2. KD-tree / hash grid
3. radiance estimate + progressive 更新
4. caustics 场景、对比、性能

**风险**：难度偏高，KD-tree 和参数调优容易拖时间；建议先做普通 photon mapping，再做 progressive。

---

## 3. Bidirectional Path Tracing & Multiple Importance Sampling — 2.5

**核心任务**：实现 BDPT，从相机和光源各生成半路径，再在中间连接；同时实现 MIS 降噪。

**必须做**
- Camera subpath + light subpath
- 所有连接策略（t=1..N）
- MIS 权重计算
- 与普通 path tracer 的噪声/效果对比

**加分**
- 焦散、glossy inter-reflection 场景
- 不同连接策略的可视化
- 方差分析

**4 人分工建议**
1. camera subpath
2. light subpath
3. 连接 + MIS 权重
4. 场景、对比、误差分析

**风险**：MIS 权重和 pdf 很容易写错；建议先用简单场景验证无偏性。

---

## 4. Add Texture Support to Homework Framework — 1.5

**核心任务**：让 Homework 3 的 path tracer 支持纹理。当前框架只支持常量 albedo。

**必须做**
- 加载带 UV 的 OBJ/MTL 或自定义模型
- 插值 UV
- 纹理采样（nearest / bilinear）
- 把纹理颜色接入 diffuse / other BSDF

**加分**
- Mipmap + 三线性过滤
- Normal mapping / bump mapping
- 程序化纹理
- 纹理重要性采样

**关键参考**
- Cornell 纹理课：<https://www.cs.cornell.edu/courses/cs4620/2017sp/slides/06rt-textures.pdf>

**注意**：官方难度只有 1.5，4 人单独做会偏少；建议至少加 normal mapping、mipmap 和程序化纹理之一。

---

## 5. Non-Photorealistic Rendering — 1.5

**核心任务**：实现风格化渲染，如 cel shading、sketch、watercolor、toon outline。

**必须做**
- 至少两种 NPR 风格
- 边缘检测 / 轮廓线
- 色调量化或笔触模拟
- 与 PBR 结果对比

**加分**
- 风格迁移
- 时序稳定的动画风格化
- 交互式参数面板

**注意**：1.5 偏容易，4 人项目需要做得非常精致，或加入动画/交互系统。

---

## 6. Pathtracing Lenses & Contrast-based Autofocus — 2.0

**核心任务**：在 path tracer 中实现真实镜头模型，并做基于对比度的自动对焦。

**必须做**
- 厚透镜/多镜片相机模型
- 景深、bokeh、曝光
- 对比度评价函数
- 自动搜索对焦距离

**加分**
- 镜头像差（球差、色差、暗角）
- 不同光圈形状
- 与薄透镜模型对比

**关联课程**：相机与镜头、蒙特卡洛
**4 人分工建议**
1. 镜头几何与光线折射
2. 传感器/景深/曝光
3. autofocus 搜索算法
4. 场景、对比、UI

---

## 7. Speeding up the Ray Tracer — 1.0–3.0

**核心任务**：从算法或工程层面加速 path tracer，目标可以是交互式帧率。

**可选方向**
- Ray packets / SIMD
- 自适应采样与重建
- GPU path tracer
- 硬件光追（DXR / RTX / OptiX）
- Radiance cache

**关键参考**
- Ray packets：<https://graphics.stanford.edu/~boulos/papers/cook_gi07.pdf>
- 自适应采样：<http://graphics.ucsd.edu/~matthias/Papers/mdas.pdf>

**注意**：难度跨度最大，可能 1 周做完，也可能 4 周卡在平台问题上。必须提前确定 baseline 和 benchmark。

---

# Rendering: Material Modeling

## 8. Subsurface Scattering — 2.0

**核心任务**：实现 BSSRDF，渲染皮肤、玉石、大理石、蜡烛等次表面散射材质。

**必须做**
- Dipole approximation（或更好的模型）
- BSSRDF 采样
- 至少 2 个材质场景
- 与普通 diffuse 对比

**加分**
- 多层皮肤模型
- 重要性采样
- 实时近似

**关键参考**
- 2001 seminal paper：<https://graphics.stanford.edu/papers/bssrdf/bssrdf.pdf>

**4 人分工建议**
1. BSSRDF 数学与采样
2. 材质参数/场景
3. 渲染器集成
4. 对比、性能、视频

---

## 9. Rendering Glints — 2.5

**核心任务**：在 microfacet 模型上渲染微小表面细节产生的闪烁高光（glints）。

**必须做**
- 高分辨率 normal map
- 微表面统计模型
- 至少一种 glints 模型（normal map 或 stochastic）
- 与普通 microfacet 对比

**关键参考**
- Lingqi Yan glints：<https://rgl.epfl.ch/publications/Yan2014Rendering>
- Stochastic glints：<http://www.cs.cornell.edu/projects/stochastic-sg14/stochastic.pdf>
- Ray differentials：<https://graphics.stanford.edu/papers/trd/trd.pdf>

**风险**：需要纹理和 ray differential 基础；建议先完成 texture support。

---

## 10. Iridescent / Wavelength-dependent Path Tracing — 官方未标难度

**核心任务**：实现光谱渲染，渲染薄膜干涉、肥皂泡、CD、孔雀/蝴蝶羽毛等虹彩效果。

**必须做**
- 光谱表示（多个波长采样）
- 人眼 CIE 响应曲线转 RGB
- 薄膜干涉 reflectance
- 至少 2 个虹彩场景

**关键参考**
- 肥皂泡 reflectance：<http://www.dgp.toronto.edu/~nmorris/CSC2530/Project/morris.pdf>
- Wavelength-dependent reflectance：<https://www-users.cs.umn.edu/~gmeyer/papers/gondek-meyer-siggraph-1994.pdf>

**建议难度**：按 2.0–2.5 评估。光谱渲染改动面较大，适合对颜色/物理光学感兴趣的小组。

---

## 11. Cloth Rendering — 2.0

**核心任务**：实现布料外观模型，表现 sheen、纤维感和各向异性高光。

**必须做**
- 至少一种 cloth BRDF（microcylinder / microflake / empirical）
- 布料纹理与参数
- 与普通 diffuse/specular 对比

**加分**
- 多层布料
- 磨损/污渍
- 实时近似

**关键参考**
- Practical microcylinder cloth model：<http://graphics.ucsd.edu/~henrik/papers/practical_microcylinder_appearance_model_for_cloth_rendering.pdf>

---

# Real-time Graphics

## 12. Shaders and Shaders Only — 1.5–2.5

**核心任务**：用 ShaderToy / GLSL 做一组高质量 shader 作品。

**必须做**
- 至少 3–5 个不同主题的 shader
- 展示 raymarching、SDF、噪声、光照、后处理等技术
- 有交互或动画

**加分**
- 实时全局光照近似
- 体积云/雾
- 风格化后处理

**注意**：很容易做成“炫酷但技术浅”，提案里要明确技术点。

---

## 13. Cloth Simulation using GPU Shader / CUDA — 2.0

**核心任务**：把 Homework 4 的 CPU 布料模拟搬到 GPU，并提升精度/规模。

**必须做**
- GPU 上的 spring-mass / Verlet 积分
- 碰撞与约束
- 与 CPU 版本性能对比
- 至少一个可交互场景

**加分**
- 自碰撞
- 更稳定的隐式积分
- 实时渲染 + 材质

**参考**：ShaderToy cloth demo <https://www.shadertoy.com/view/MldXWX>

**4 人分工建议**
1. GPU 数据布局与积分
2. 碰撞/约束
3. 渲染与材质
4. 性能分析、对比视频

---

## 14. GPU Path Tracer using NVIDIA OptiX — 2.0

**核心任务**：用 OptiX/CUDA 写 GPU path tracer，支持 Homework 3 的全部效果。

**必须做**
- GPU BVH 构建/遍历
- 光线-三角形求交
- 材质与直接/间接光照
- 与 CPU 版本对比，目标 10x 加速

**加分**
- 降噪
- 动态场景
- 实时预览

**注意**：需要有 NVIDIA GPU；Mac 用户不适合作为主平台。

---

## 15. Visual / Rendering Mods for Games — 1.5–3.5

**核心任务**：给现成游戏写渲染 mod，如 ReShade、Minecraft shaders、Quake RTX。

**可选方向**
- SSAO
- 屏幕空间反射
- 路径追踪 mod
- 后处理风格化

**风险**：工具链文档少、平台限制多，难度方差极大。适合已有 modding 经验的小组。

---

## 16. Game / Interactive Demo — 2.0

**核心任务**：做一个小游戏或交互 demo，但必须有明确的图形学技术组件。

**必须做**
- 自己实现的渲染/模拟/几何算法
- 明确区分“引擎自带”与“自己写的”
- 可玩的 demo + 技术说明

**可以做的技术点**
- 程序化地形/纹理
- 自己写光栅化或光线追踪
- 自己写动画/物理
- 高级 shader

**注意**：官方 FAQ 明确说可以，但纯游戏逻辑不算；必须突出 graphics 技术贡献。

---

# Rasterization

## 17. Font Rendering — 2.0

**核心任务**：加载 TrueType/OpenType 字体，自己写 Bézier 曲线光栅化器。

**必须做**
- 解析 .ttf/.otf 轮廓
- Bézier 曲线细分/扫描线填充
- 抗锯齿
- 排版基础（字距、行距）

**加分**
- GPU 文本渲染
- SDF 字体
- 亚像素渲染
- 动态字号/缩放质量对比

**4 人分工建议**
1. 字体文件解析
2. 曲线细分与填充
3. 抗锯齿/扫描线
4. 排版、UI、性能

---

# Texture Synthesis

## 18. Solid Texture Synthesis — 1.5

**核心任务**：从 2D 示例纹理生成 3D solid texture，并用体积渲染展示。

**必须做**
- 2D exemplar → 3D volume
- 邻域匹配/优化
- 体积渲染或切片展示

**关键参考**
- Solid Texture Synthesis from 2D Exemplars：<http://www.cs.princeton.edu/courses/archive/fall07/cos597B/papers/kopf-solid-texture.pdf>

**注意**：需要自己补一个体积渲染器；可与 Volumetric Scattering 结合。

---

# Geometry

> 官方特别说明：这些几何题目**对 4 人项目来说偏简单**，建议选 2 个以上组合，或加自己的扩展。

## 19. Mesh Simplification & Remeshing — 1.5

**核心任务**：实现网格简化（如 QEM 边折叠）和/或 remeshing。

**必须做**
- 二次误差度量（QEM）
- 边折叠/顶点合并
- 简化前后误差与面数对比

**加分**
- 保特征边
- 纹理/法线保持
- 交互式简化

---

## 20. Point Cloud to Mesh — 2.0

**核心任务**：把点云重建为三角网格。

**可选算法**
- Ball Pivoting（较简单）
- Poisson Surface Reconstruction（较难）

**必须做**
- 点云输入/法线估计
- 重建网格
- 与原始网格对比
- 至少 2 个 Stanford 模型

**数据**：Stanford 3D Scanning Repository <https://graphics.stanford.edu/data/3Dscanrep/>

---

## 21. Alternate Subdivision Schemes — 1.5

**核心任务**：在 Homework 2 的 Loop Subdivision 之外，实现其他细分方案。

**可选**
- Butterfly / modified Butterfly
- √3-Subdivision
- Catmull-Clark（四边形网格）
- Polar subdivision
- Sharp edges

**建议**：4 人项目至少实现 3 种，并做质量/连续性对比。

---

## 22. Remeshing / Mesh Regularization — 1.5

**核心任务**：把质量差的三角网格变成更均匀、各向同性的网格。

**必须做**
- 顶点重定位
- 边翻转/分裂/折叠
- 质量指标（三角形形状、边长分布）

**参考**：Hao Li remeshing slides <https://www.hao-li.com/cs599-ss2015/slides/Lecture09.1.pdf>

---

# Imaging and Computational Photography

## 23. Light Field Camera Support — 1.5

**核心任务**：在 path tracer 中模拟光场相机，记录每个像素的方向信息，实现后期重对焦。

**必须做**
- 微透镜阵列模型
- 方向采样
- 光场数据存储
- 后期 refocus + 光圈形状

**加分**
- 复杂镜头
- 交互式 refocus GUI
- 与薄透镜景深对比

**关键参考**：Ren Ng 技术报告 <https://graphics.stanford.edu/papers/lfcamera/lfcamera-150dpi.pdf>

**4 人分工建议**
1. 光场相机模型
2. 采样与存储
3. refocus 算法
4. GUI + 场景 + 视频

---

## 24. Multi-shot HDR — 2.0

**核心任务**：用多张不同曝光的照片合成 HDR，并降噪。

**必须做**
- 多曝光对齐
- HDR merge
- tone mapping
- 噪声/鬼影处理

**加分**
- 手机 burst 数据
- 色彩校正
- 与单张 HDR 对比

**关键参考**：HDR+ <https://hdrplusdata.org>

**注意**：不能直接交 CS180 项目；必须明显超出课程项目深度。

---

# Animation and Simulation

## 25. 2D Grid Based Fluid Dynamics Simulation — 2.0

**核心任务**：实现二维不可压缩流体，最好用 GLSL 在 GPU 上交互运行。

**必须做**
- Navier-Stokes 方程
- 对流（advection）
- 压力投影（Poisson solver）
- 边界条件
- 可视化（染料/速度场）

**加分**
- 涡量约束（vorticity confinement）
- 交互式鼠标力场
- 3D 版本
- 与 CPU 版本性能对比

**参考**：Stam, Stable Fluids；GPU Gems 流体章节

**4 人分工建议**
1. 网格与 advection
2. 压力投影
3. 边界/涡量/交互
4. 渲染、性能、视频

---

## 26. Animation using Spatial Keyframing — 2.0

**核心任务**：实现空间关键帧动画：在 3D 空间中定义关键姿态，角色在空间中移动时自然插值。

**必须做**
- 3D 关键姿态
- 空间插值/权重
- 角色或简单骨骼
- 与时间关键帧对比

**关键参考**
- Spatial keyframing：<https://www-ui.is.s.u-tokyo.ac.jp/~takeo/papers/squirrel.pdf>
- 动画示例：<https://www-ui.is.s.u-tokyo.ac.jp/~takeo/gallery/animations/index.html>

---

## 官方推荐的其他灵感来源

- NVIDIA GPU Gems：<https://developer.nvidia.com/gpugems/gpugems/contributors>
- Ray Tracing Gems：<https://www.realtimerendering.com/raytracinggems/>
- PBRT（免费在线）：<https://pbr-book.org/>
- 最新 SIGGRAPH 论文与 Two Minute Papers
- 本学期 guest lecture 主题
