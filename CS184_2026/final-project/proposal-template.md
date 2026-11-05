# Final Project Proposal 模板（Fall 2026）

> 官方要求：创建一个 proposal webpage，然后把网页导出成 PDF 提交到 Gradescope。
> 截止：**2026-11-10（周二）11:59 PM PT**，无 late days。
> 提交时确保 PDF 里有可点击的网页链接；Safari 用 `Print -> Save as PDF`，不要用 `File -> Export as PDF`（会变成一张超大页面）。

---

## 标题

**项目名（短、好记、相关）**

一句话副标题：例如 “A volumetric path tracer for participating media”。

---

## 1. Summary

2–3 句话说明：

- 我们要解决什么图形学问题？
- 我们准备怎么做？
- 最终会交付什么可展示的结果？

**示例**

> We will extend our Homework 3 path tracer with volumetric scattering to render fog, smoke, and clouds. We will implement free-flight distance sampling, a Henyey–Greenstein phase function, and importance sampling for heterogeneous media, then compare equal-time renders against surface-only path tracing.

---

## 2. Team Members

| 姓名 | 邮箱 | CS184 / CS284A | 主要职责 |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

> 必须正好 4 人。组里有 CS284A 学生时，最终要交 ACM SIGGRAPH 格式的 4–6 页论文。

---

## 3. Problem Description

回答：

1. **背景**：这个效果/问题为什么重要？在哪些场景出现？
2. **问题定义**：输入是什么，输出是什么？
3. **技术难点**：为什么不是简单调库？难在哪里？
4. **现有方法**：你参考了哪些论文/实现？它们的局限是什么？
5. **我们的方法**：一句话概括你的技术路线。

**写作提示**

- 不要写成“我们想做很酷的渲染器”；要写清楚具体技术问题。
- 引用 2–4 篇关键论文，并说明你准备实现哪部分、简化哪部分。

---

## 4. Goals and Deliverables

官方说这是**最重要**的部分。分成两部分写。

### 4.1 What We Plan to Deliver（baseline，必须完成）

逐条列出可验收的交付物：

- [ ] 功能 1：例如“均匀介质的体积路径追踪”
- [ ] 功能 2：例如“HG phase function + 重要性采样”
- [ ] 功能 3：例如“3 个测试场景：雾、烟、云”
- [ ] 功能 4：例如“与 surface-only path tracing 的 equal-time 对比”
- [ ] 功能 5：例如“最终网页 + 1–2 分钟视频”

每条尽量带**量化指标**：

| 指标 | 目标 |
|---|---|
| 渲染时间 | 单帧 ≤ X 分钟 @ 800×600, 256 spp |
| 噪声 | 同 spp 下比 baseline 噪声降低 X% |
| 场景数 | ≥ 3 |
| 对比图 | ≥ 5 组 |

### 4.2 What We Hope to Deliver（stretch，加分）

- [ ] 非均匀介质 / 体积光
- [ ] 多次散射近似
- [ ] 与材质（BSSRDF / cloth）耦合
- [ ] 交互式预览
- [ ] 额外场景/动画

### 4.3 Questions We Plan to Answer

- 在相同时间预算下，体积渲染比 surface-only 慢多少？
- 重要性采样对噪声的改善有多大？
- 均匀 vs 非均匀介质在什么场景下差异明显？

---

## 5. Schedule（按周）

必须覆盖从 proposal 到 final 的 4 周，建议每周写具体任务和负责人。

| 周 | 日期 | 任务 | 负责人 | 交付/检查点 |
|---|---|---|---|---|
| Week 1 | 11/10–11/16 | 搭框架、读论文、实现介质采样 | | 能渲染一个均匀雾场景 |
| Week 2 | 11/17–11/23 | phase function、重要性采样、场景 | | Milestone：可出图 + 1 分钟视频 |
| Week 3 | 11/24–11/30 | 非均匀介质、优化、对比实验 | | 3 个场景 + 性能数据 |
| Week 4 | 12/01–12/06 | 最终渲染、网页、视频、答辩 | | Final deliverables |

**Milestone（11/22）检查清单**

- [ ] 至少一个能跑通的核心效果
- [ ] 1 分钟进度视频（每个成员出镜/发声）
- [ ] 2–3 页 slides
- [ ] 更新后的 schedule
- [ ] Milestone 网页

---

## 6. Resources

### 论文 / 书籍

1. 作者，标题，会议/期刊，年份。链接。
2. …
3. …

### 代码 / 框架

- Starting point：Homework 3 path tracer / Homework 4 / 自建 / Unity / pbrt / OptiX
- 第三方库：OpenGL / CUDA / OptiX / Embree / stb_image / tinyobjloader …
- 明确说明：**哪些是已有代码，哪些是我们自己写的**

### 硬件 / 软件

- 开发机器：macOS / Windows / Linux；GPU 型号
- 构建工具：CMake / Make / Visual Studio / Xcode
- 版本控制：GitHub（每个成员用自己的账号提交）

### 数据 / 场景

- 模型来源（Stanford 3D Scanning Repository、Blender、Poly Haven 等）
- 纹理来源与许可证
- 如果是自己拍摄/生成，说明方法

---

## 7. 提交前检查

- [ ] 正好 4 名成员
- [ ] 项目名好记
- [ ] Summary 2–3 句
- [ ] Problem Description 说清楚技术难点
- [ ] Goals 分成 baseline / stretch
- [ ] 有量化指标
- [ ] 每周 schedule 具体到人
- [ ] Resources 列出论文、代码、硬件
- [ ] 明确 starting point 和自己写的部分
- [ ] PDF 含可点击链接
- [ ] 11/10 11:59 PM PT 前提交到 Gradescope

---

## 8. 一个完整示例（Volumetric Scattering）

**Title**: Foggy Bunny — Volumetric Path Tracing for Participating Media

**Summary**: We extend our Homework 3 path tracer to support participating media, enabling fog, smoke, and cloud rendering. We implement free-flight sampling, Henyey–Greenstein phase functions, and transmittance estimation, then compare equal-time quality against surface-only path tracing.

**Problem**: Surface-only rendering cannot reproduce volumetric effects such as god rays, haze, and smoke. The rendering equation becomes an integral over volumes as well as surfaces, and naively ray marching is too noisy/slow.

**Baseline deliverables**:
1. Homogeneous medium with free-flight sampling
2. HG phase function + importance sampling
3. Three scenes: foggy Cornell box, smoke plume, cloud layer
4. Equal-time comparison vs surface-only path tracing
5. Web report + 1–2 min video

**Stretch**:
- Heterogeneous medium with delta tracking
- Volumetric god rays
- Coupling with subsurface scattering

**Schedule**: Week 1 medium sampling; Week 2 phase function + first scene; Week 3 heterogeneous + comparisons; Week 4 final render/video.

**Resources**: Jarosz thesis ch. 4; Lafortune & Willems 1996; PBRT ch. 11; Homework 3 code; 4 machines with RTX 3060.
