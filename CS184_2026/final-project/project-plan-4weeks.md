# 4 周项目执行计划（Fall 2026）

关键日期：
- **11/10（周二）** Proposal 截止
- **11/22（周日）** Milestone 截止
- **12/06（周日）** Final Report & Video 截止
- **12/07–12/08** Final Presentations

> 没有 late days。以下计划默认 11/10 前完成 proposal，11/11 开始正式开发。

---

## Week 0：11/03–11/09（Proposal 周）

| 任务 | 产出 |
|---|---|
| 定题，查 3–5 篇关键论文 | 选题 + 参考列表 |
| 确认 4 人分工 | 角色表 |
| 写 proposal 网页 | 标题/Summary/Problem/Goals/Schedule/Resources |
| 内部评审 | 删掉不现实的目标 |
| 导出 PDF，检查链接 | 11/10 前提交 Gradescope |

**定题检查**
- [ ] 有明确的图形学技术点
- [ ] 有可展示的视觉结果
- [ ] 有 baseline + stretch
- [ ] 4 周内 baseline 可完成
- [ ] starting point 明确（HW3 / HW4 / 自建 / Unity / OptiX）
- [ ] 没有依赖无法获得的硬件/数据

---

## Week 1：11/11–11/16（核心框架）

目标：**跑通最小闭环**，不追求好看。

| 角色 | 任务 |
|---|---|
| 渲染/算法 | 核心公式、采样、积分器最小实现 |
| 几何/数据 | 场景/模型/纹理导入，坐标系与单位统一 |
| 工程/性能 | 构建、日志、参数面板、benchmark 脚本 |
| 呈现/验证 | 测试场景、对比 baseline、记录数据 |

**周五检查**
- [ ] 能渲染一张“丑但正确”的图
- [ ] 参数可调，不需要改代码
- [ ] Git 主分支可构建
- [ ] 已记录 baseline 时间/质量

**常见坑**
- 一开始就追求高质量 → 进度停滞
- 四个人各自写一套代码 → 无法合并
- 没有 baseline → 后面无法证明提升

---

## Week 2：11/17–11/22（Milestone）

目标：**有一个能演示的核心效果** + 完成 milestone 交付。

| 任务 | 产出 |
|---|---|
| 完成核心功能 1–2 | 可演示 demo |
| 出 2–3 组对比图 | milestone 网页 |
| 录 1 分钟视频 | 每个成员出镜/发声 |
| 做 2–3 页 slides | 进度 + 技术点 + 计划 |
| 更新 schedule | 根据实际进度调整 |

**Milestone 提交（11/22 11:59 PM PT）**
- [ ] Milestone 网页（CS184）或 SIGGRAPH 格式报告（CS284A）
- [ ] 1 分钟视频（unlisted YouTube / Berkeley 可见 Google Drive）
- [ ] 2–3 页 slides
- [ ] 所有链接可访问
- [ ] PDF 提交到 Gradescope

**Milestone 评分重点**
- 有没有实际进展，而不是只有计划
- 技术路线是否清晰
- 视频/slides 是否讲清楚“你们做了什么”

---

## Week 3：11/23–11/30（扩展与验证）

目标：**把 baseline 做完整，开始 stretch**。

| 任务 | 产出 |
|---|---|
| 补齐 baseline 功能 | 完整功能列表 |
| 做 stretch 1–2 个 | 加分效果 |
| 系统实验 | 性能/质量/误差曲线 |
| 开始最终网页 | 结构 + 结果图 |
| 开始最终视频分镜 | 脚本 |

**周末检查**
- [ ] baseline 全部完成
- [ ] 至少 3 个场景/案例
- [ ] 至少 1 组量化对比
- [ ] 最终视频脚本确定
- [ ] 网页骨架完成

**取舍原则**
- 如果时间不够，**砍 stretch，保 baseline 和呈现质量**。
- Showcase 很看视频和结果图，不要最后一天才做。

---

## Week 4：12/01–12/06（收尾）

目标：**打磨呈现**，不是加新功能。

| 日期 | 任务 |
|---|---|
| 12/01–12/02 | 最终渲染、补图、补实验 |
| 12/03 | 网页完成（Abstract / Approach / Results / References / Contributions） |
| 12/04 | 视频剪辑、配音、字幕 |
| 12/05 | 内部预答辩，计时 5 分钟 |
| 12/06 | 提交 Final Deliverables（11:59 PM PT） |

**Final 提交检查**
- [ ] 最终网页（CS184）或 4–6 页 SIGGRAPH 论文（CS284A）
- [ ] 1–2 分钟最终视频，每个成员出镜/发声
- [ ] 网页含最终 gif/clip（官方要求）
- [ ] 所有链接可访问
- [ ] 贡献说明（每个人做了什么）
- [ ] PDF 提交 Gradescope

---

## 答辩准备（12/07–12/08）

官方格式：**5 分钟 presentation（含 1 分钟 demo）+ 3 分钟 Q&A**。

建议结构：
1. Title（15s）：项目名 + 一句话
2. Background（30s）：问题、为什么重要、starting point
3. Demo/Results teaser（30s）：先放最惊艳的结果
4. Technical approach（1–1.5 min）：核心算法、你们自己写的部分
5. More results（0.5–1 min）
6. Conclusion（15–30s）

**注意事项**
- 先放最好的结果，防止超时
- 每页一个主要观点，标题就是结论
- 图多字少
- 提前测试 demo/录屏，准备 backup video
- 必须参加至少 8 个其他组的 presentation（占 project 10%）

---

## 风险管理

| 风险 | 应对 |
|---|---|
| 核心算法调不通 | 第 1 周结束前必须有简化版；第 2 周仍失败则换方案 |
| GPU/平台问题 | Week 1 就验证环境；准备 CPU fallback |
| 数据/模型拿不到 | 提前准备 2 个替代场景 |
| 性能太慢 | 降低分辨率/spp 做对比；记录 equal-time |
| 合并冲突 | 每天 push；按模块分文件；周五集成 |
| 视频来不及 | Week 3 就开始分镜和录素材 |
| 成员进度不一致 | 每周站会；任务拆到 1–2 天粒度 |

---

## 团队协作规则（建议）

- GitHub 每人用自己的账号 commit，方便 peer review
- 主分支始终可构建
- 每个功能一个分支/PR，至少一人 review
- 实验参数和结果写进 `experiments.md`
- 每周五 30 分钟同步：完成/阻塞/下周计划
- 所有外部代码/模型/纹理记录来源和许可证
