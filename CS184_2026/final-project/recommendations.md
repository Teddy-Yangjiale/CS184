# 选题推荐与避坑（4 人 / 4 周）

> 官方难度是 1.0–3.0 的相对参考；真正的风险来自**平台、数据、调参、出图时间**。

---

## 一、先按兴趣选方向

| 你喜欢 | 优先看 | 原因 |
|---|---|---|
| 渲染、光照、物理正确 | Volumetric Scattering、BDPT+MIS、Photon Mapping | 直接延续 Homework 3，出图效果最直观 |
| 材质、外观、真实感 | Subsurface Scattering、Cloth Rendering、Glints、Iridescent | 有大量论文可参考，Showcase 视觉冲击强 |
| 实时、GPU、性能 | GPU Path Tracer、GPU Cloth、Fluid Simulation | 容易做出可交互 demo 和性能曲线 |
| 几何、建模 | Point Cloud to Mesh、Subdivision、Remeshing | 数学清晰，结果可量化；但要注意工作量偏小 |
| 成像、相机 | Light Field、Multi-shot HDR、Lenses/Autofocus | 与相机/颜色课程衔接好，demo 直观 |
| 风格化、艺术 | NPR、Shaders Only、Font Rendering | 视觉效果好，但必须有技术深度 |
| 游戏/交互 | Game Demo、Game Mods | 有趣，但工具链风险高，必须突出图形学技术 |

---

## 二、最推荐的 6 个（平衡难度、效果、可控性）

### 1. Rendering Volumetric Scattering（官方 2.0）★★★★★

**为什么推荐**：Homework 3 的直接扩展；雾、云、烟效果非常出片；有一篇很清楚的 Jarosz 章节可跟着做。

**4 人范围**
- 均匀介质 + 非均匀介质
- HG phase function
- 体积光/god rays
- 3 个场景 + 与表面渲染对比

**风险**：噪声。必须做重要性采样；否则渲染时间爆炸。

---

### 2. Subsurface Scattering（官方 2.0）★★★★★

**为什么推荐**：皮肤、玉石、蜡烛效果辨识度高；dipole approximation 论文经典且可实现。

**4 人范围**
- BSSRDF 采样
- 至少 2 种材质
- 与 diffuse 对比
- 参数扫描（scattering radius / albedo）

**风险**：数学偏多，但实现路径清晰。

---

### 3. 2D Grid Fluid Simulation（官方 2.0）★★★★★

**为什么推荐**：Stable Fluids 经典；GPU 交互 demo 很直观；可量化性能。

**4 人范围**
- advection + pressure projection
- vorticity confinement
- 鼠标交互力场
- CPU vs GPU 性能对比

**风险**：压力求解器调参；建议先做 CPU 小网格，再上 GPU。

---

### 4. GPU Path Tracer using OptiX（官方 2.0）★★★★★

**为什么推荐**：工程亮点强，10x 加速很容易讲清楚；适合放作品集。

**4 人范围**
- OptiX BVH + 求交
- 材质/光照
- 降噪（可选）
- benchmark + 与 CPU 对比

**风险**：必须有 NVIDIA GPU；Mac 团队不要选。

---

### 5. Light Field Camera（官方 1.5）★★★★★

**为什么推荐**：概念优雅，refocus demo 非常直观；可与相机/成像课程结合。

**4 人范围**
- 微透镜模型
- 方向采样
- refocus + 光圈形状
- GUI

**风险**：数据量和采样率；需要设计好存储格式。

---

### 6. Cloth Rendering（官方 2.0）★★★★

**为什么推荐**：视觉效果好，microcylinder 模型实现难度适中；可与布料模拟结合。

**4 人范围**
- cloth BRDF
- 纹理/参数
- 与 diffuse/specular 对比
- 多层布料

**风险**：需要 texture 基础；可先做简单 procedural 纹理。

---

## 三、想冲 Showcase 的选题

| 选题 | 官方难度 | 冲奖理由 | 风险 |
|---|---:|---|---|
| BDPT + MIS | 2.5 | 技术深度高，caustics 对比强 | pdf/MIS 容易错 |
| Progressive Photon Mapping | 2.5 | 焦散效果惊艳 | KD-tree + 调参 |
| Rendering Glints | 2.5 | 微表面细节视觉独特 | 需要 normal map / ray differential |
| Iridescent Path Tracing | 未标 | 肥皂泡/蝴蝶翅膀非常出片 | 光谱渲染改动大 |
| GPU Path Tracer | 2.0 | 性能曲线 + 实时 demo | 平台限制 |
| Fluid + Cloth 组合 | 2.0+ | 物理模拟视觉强 | 工作量叠加 |

---

## 四、偏简单、必须加料的选题

官方标 1.5 的题目，对 4 人 4 周通常不够。建议至少加一个“深度模块”：

| 基础题 | 建议加料 |
|---|---|
| Add Texture Support | normal mapping + mipmap + 程序化纹理 |
| NPR | 动画时序稳定 + 交互参数 + 3 种风格 |
| Shaders Only | raymarching GI + 体积 + 后处理管线 |
| Solid Texture Synthesis | 自己写体积渲染器 + 动画 |
| Mesh Simplification | 保特征 + 纹理保持 + 交互 |
| Alternate Subdivision | 3 种方案 + 连续性/质量分析 |
| Remeshing | 各向异性 + 特征保持 + 质量指标 |
| Light Field | 复杂镜头 + 交互 GUI + 与薄透镜对比 |

---

## 五、不建议作为主项目

| 类型 | 原因 |
|---|---|
| 纯游戏 / 纯 UI | 官方 FAQ 要求必须有 graphics 技术成分 |
| 纯 ML 项目 | 必须有图形学组件；训练时间不可控 |
| 纯 Shader 堆砌 | 容易视觉炫但技术浅，答辩会被问穿 |
| Game Mods | 工具链/文档风险高，难度方差极大 |
| 纯 Mesh 简化 | 官方明说对 4 人偏简单 |

---

## 六、4 人团队怎么分工

推荐角色（可兼职）：

1. **渲染/算法负责人**：核心公式、采样、积分器
2. **几何/数据负责人**：场景、模型、网格、点云、纹理
3. **工程/性能负责人**：构建、GPU、并行、benchmark
4. **呈现/验证负责人**：出图、对比实验、视频、网页、答辩

每周至少一次集成，不要最后一周才合并。

---

## 七、Proposal 拿高分的关键

官方明确说 Proposal 最重要的部分是 **Goals and Deliverables**。写的时候：

1. **必须交付（baseline）** 写清楚，保证能完成。
2. **希望交付（stretch）** 写 2–3 个加分项。
3. **量化指标**：速度提升、误差、噪声、帧率、面数、PSNR。
4. **每周 schedule**：具体到“谁做什么”。
5. **明确 starting point**：基于 Homework 3 / Homework 4 / 自建框架。
6. **明确自己写的部分**：如果用了 Unity/pbrt/OptiX，写清楚边界。
7. **风险与备选方案**：至少写一个“如果某模块失败，怎么降级”。

---

## 八、往届 Showcase 的可复刻方向

Spring 2025 获奖项目包括：

- Implicit deformable thin-sheet dynamics（薄片/布料模拟）
- Lightning Simulation（闪电）
- Lumen: GI in Unreal Engine（实时全局光照）
- Monet-ification（风格化）
- Semi-Automated Vector 2D Cel Shading（矢量 cel shading）
- CUDA-Accelerated Neural Pathtracing
- Interactive Fluid Simulation
- Jack of All Waters（水体）
- N3CTAR（神经 3D 渲染）
- Paint by Numbers（图像风格化）
- Minecraft 球体物理
- Realistic Sunset Rendering（大气散射）

规律：
- **视觉结果强** + **技术点清晰** + **视频打磨好** 最容易获奖。
- 纯技术但出图差，或纯视觉但技术浅，都不占优。
- Showcase 很看 final video，提前规划镜头和对比图。

详见 `past-projects.md`。
