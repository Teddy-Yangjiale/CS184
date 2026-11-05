# 异地开发交接

更新日期：2026-11-06。项目处于文献调研与实验设计阶段。当前选择是优先验证方向 A，方向 B 为备选，方向 C 暂缓；这是一项研究建议，尚无性能结果支持。先阅读 [Idea 意见报告](notes/IDEA_REVIEW.md)，再使用历史笔记。

**完整获取项目**

已有远程仓库为 `https://github.com/Teddy-Yangjiale/CS184`。使用 Git 和 Git LFS 克隆，LFS 存放新增调研 PDF 以及原先已采用 LFS 的课程 PDF。

```bash
git lfs install
git clone https://github.com/Teddy-Yangjiale/CS184.git
cd CS184
git lfs pull
git status --short
python light-transport-survey/tools/verify_snapshot.py
```

Windows 和 Linux 均可使用上面的 Git 命令；Linux 如仅提供 `python3`，将 `python` 替换为 `python3`。访问权限沿用仓库现有设置。看到体积很小、以 `version https://git-lfs.github.com/spec/v1` 开头的 PDF，说明只下载了指针，需要完成 `git lfs pull`。

校验脚本检查文献资料库的大小和 SHA-256，不校验课程资料，也不判断论文结论是否正确。更新资料后，可以有意识地执行 `python light-transport-survey/tools/verify_snapshot.py --write` 更新清单；不应以重新生成清单代替排查下载损坏。

**阅读顺序与目录职责**

1. `notes/IDEA_REVIEW.md`：当前选题判断、证据、实验假设和放弃条件。
2. `SOURCES.md`：26 篇核心论文入口；报告中的补充文献链接扩展了这一集合。
3. `pdf/` 与 `text/`：原文和逐页提取文本。公式、图表和决定选题的局限应回查 PDF。
4. `notes/PROGRESS.md`：初始分析快照，部分推断已被新报告修正。
5. `meta/`：历史检索记录与文件校验清单。旧记录中的本机绝对路径仅代表采集时环境。
6. `tools/`：文献检索、下载、提取和核查工具。不是渲染训练代码。

课程资料保留在 `CS184_2026/`。不存在已完成的候选渲染器、训练权重、实验数据集或服务器部署；不要把文献中描述的能力当作本项目已实现的功能。

**文献工具环境**

只阅读 Markdown、文本、PDF 和执行文件校验，不需要安装渲染依赖。重跑提取工具时建议使用独立 Python 3.11 环境；这是迁移建议，尚未在新机器完成环境安装验证。

Linux：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r light-transport-survey/requirements-survey.txt
```

Windows PowerShell：

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r light-transport-survey/requirements-survey.txt
```

`requirements-survey.txt` 记录源机器上已观察到的直接依赖版本，不是包含全部传递依赖的跨平台锁文件。仅在需要扫描页 OCR 时安装 `requirements-ocr.txt`。当前核心文献提取统计为 26 篇、388 页、OCR 触发 0 页；这代表文本层可用，不是数学公式与图表解释的正确性认证。

脚本自动从自身位置寻找项目目录，不再依赖源机器盘符。网络默认使用 Requests 的标准环境代理设置（`HTTP_PROXY`、`HTTPS_PROXY`、`NO_PROXY`）；也可以设置 `SURVEY_PROXY` 为新机器实际可用的代理 URL。不要复制源机器的本地端口，也不要将带凭据的代理地址提交到 Git。

```bash
python light-transport-survey/tools/make_index.py
python light-transport-survey/tools/extract_text.py
# 以下需要网络，且会刷新相应历史记录
python light-transport-survey/tools/arxiv_search.py
python light-transport-survey/tools/download_pdfs.py
python light-transport-survey/tools/check_repos.py
```

重新运行网络和提取脚本会更新对应快照。若只需要继续阅读，直接使用已提交资料即可。原采集流程曾设置 `KMP_DUPLICATE_LIB_OK` 处理本机运行问题；不要将其作为新环境的常规安装步骤。

**渲染实验环境**

已知硬件是用户提供的一台带 RTX 5090 的服务器，系统、驱动、显存可用量及 CUDA 工具链未实测。建议先建立独立的 Mitsuba 3 与 Dr.Jit 参考渲染环境，以及独立的 PyTorch 模型环境；需要互操作时再验证版本兼容。不要直接将较旧论文的 CUDA 配置视为适配 5090 的已验证配置。

首次接入服务器时记录操作系统、GPU 和驱动、Python、PyTorch/CUDA、Mitsuba/Dr.Jit 版本与代码提交。先验证单场景 GPU 渲染与梯度，再决定训练规模。用本地编辑器通过 SSH 编辑服务器文件，批量运行无界面的实验，保存配置、原始线性图像与统计；Jupyter 可用于分析，批量任务应使用可重复运行的脚本。

| 实现入口 | 用途与边界 |
|---|---|
| [Mitsuba 3](https://github.com/mitsuba-renderer/mitsuba3) | 物理参考与可微渲染；按实际参数选择合适积分器 |
| [RenderFormer V1](https://github.com/microsoft/renderformer) | 官方前馈渲染基线；遵守其材质与场景输入范围 |
| [RenderFormer-Studio](https://github.com/iamNCJ/RenderFormer-Studio) | V1/V2 数据、训练与推理代码；服务器运行待验证 |
| [Radiance cache code](https://github.com/ziyi-zhang/radiance-cache-code) | 可微渲染缓存混合的近邻实现，不是本项目已复现结果 |
| [Light Transformer](https://github.com/bing-xu-graphics/light_transformer) | 光传输 3D embedding 的官方实现入口 |
| [Wave Tracer](https://github.com/ssteinberg/wave_tracer) | 方向 C 的参考实现；暂不作为首个实验依赖 |

**接手后的第一项任务**

实现方向 A 的最小数据与评估管线：固定几何、材质和相机，仅改变一个面光源。先建立平滑响应、遮挡变化与镜面高光三个场景，测量参考差分的噪声底；再扩展训练和测试。比较仅图像监督、随机响应监督、主动响应采样、同成本增加普通图像四组方法。

在这一步完成之前，不需要从头训练通用 RenderFormer、不需要搭建光镊实验，也不应宣称实现了新方法。每次实验应保存场景划分、参数归一化、编辑方向和幅度、随机种子、参考样本量、总时间与模型配置。具体指标和判断条件见意见报告。
