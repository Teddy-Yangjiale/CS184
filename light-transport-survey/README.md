# light-transport-survey

为「宏观场景光照与渲染（借鉴光镊的光场控制 / 扰动响应 / 稳定性优化）」这一课题建立的文献与实现基线。

- 建立日期：2026-11-06
- 规模：**26 篇论文，388 页，1.60 M 字符提取文本，591 MB 核心 PDF**（不含排除项和网页快照 PDF）
- 主题簇：实时重采样与神经缓存 / 前馈神经渲染 / 可微渲染与焦散逆设计 / 波动光学渲染 / 方法学基础 / 光镊物理

**当前研究判断以 [Idea 意见报告](notes/IDEA_REVIEW.md) 为准。** 优先验证光源编辑响应学习，鲁棒焦散设计作为备选，波动光学精度选择暂缓。三项均为待验证假设。初始 `notes/PROGRESS.md` 保留作历史记录，其中空白、新颖性和物理类比的强结论已在新报告中修订。

换机器继续开发请先阅读 [异地开发交接](DEVELOPMENT.md)。全部新增 PDF 使用 Git LFS 保存；克隆后执行 `git lfs pull`，再执行 `python light-transport-survey/tools/verify_snapshot.py`（在仓库根目录）。

## 目录结构

```
light-transport-survey/
├── pdf/            26 份论文 PDF（arXiv 原始版）
├── text/           26 份全文纯文本，逐页标记 ===== slug | page i/N =====
├── meta/
│   ├── papers.json         人工策展的清单（slug / arXiv / 簇 / 备注）
│   ├── download_log.json   下载结果与页数校验
│   ├── extract_stats.json  提取统计
│   ├── github_probe.json   GitHub 关键词检索原始结果
│   ├── repo_status.json    重点仓库状态（stars / 最近提交 / 根目录）
│   ├── web/                项目页与实现文档快照（RTXDI、Mitsuba、EG 等）
│   └── excluded/           误命中文献（非本主题）
├── notes/          精读笔记与进度报告
├── SOURCES.md      文献索引表
└── tools/          可复现脚本
```

## 文献工具的迁移与复现

| 环节 | 工具与配置 |
|---|---|
| 网络 | 默认使用系统环境代理，可通过 `SURVEY_PROXY` 覆盖；不依赖固定的本机端口 |
| 下载 | Python + `requests`，自动定位项目目录 |
| 文本提取 | `PyMuPDF (fitz)` 文本层 |
| OCR 兜底 | 可选安装 `rapidocr_onnxruntime`（CPU ONNX） |
| 仓库核查 | GitHub REST API（只读，无 token） |

```bash
# 在仓库根目录，并使用已选择的独立 Python 环境
python -m pip install -r light-transport-survey/requirements-survey.txt
python light-transport-survey/tools/arxiv_search.py
python light-transport-survey/tools/download_pdfs.py
python light-transport-survey/tools/extract_text.py
python light-transport-survey/tools/github_probe.py
python light-transport-survey/tools/check_repos.py
python light-transport-survey/tools/make_index.py
```

依赖版本记录来自源机器；新服务器安装尚待验证。重新执行脚本会刷新相应索引或历史快照。渲染模型与 CUDA 环境需单独配置，本依赖文件仅用于文献工具。

## 关于 OCR

`extract_text.py` 的规则是：**每页先取文本层，字符数 < 120 才渲染成 200 dpi 图像交给 RapidOCR**。

实测结果：26 篇全部是 arXiv 原生数字版，**文本层完整，OCR 触发 0 页**。这不是跳过 OCR，而是按你的要求把本机 OCR 接进了管线并验证可跑（`rapidocr_onnxruntime` 加载与单页推理均通过）；对已有文本层的 PDF 强行 OCR 只会引入错字。

## 已知偏差与排除项

| 条目 | 情况 |
|---|---|
| `2310.01829 Active Caustics` | **误命中**：活性物质物理（自驱动粒子在湍流中的密度焦散），非图形学焦散设计，已移入 `meta/excluded/` |
| `2606.03262 Let There Be Light` | 并非渲染论文，而是 PDE 神经算子（LiNO）；"反射/折射/散射"是隐空间算子的类比，无光源与图像。保留在 C5 作方法参考 |
| `2606.30380 RenderFormer++` | 代码"接收后公开"，暂不可得；光源参数范围原文未给出 |
| Cloth ray-wave 论文 | 初始采集时 NVIDIA 页面访问失败，未进入 26 篇 PDF 集合；后续已核实 [ACM 正式页面](https://doi.org/10.1145/3763359)，纳入意见报告 |

## 引用合规

所有 PDF 来自 arXiv 公开预印本，仅用于个人研究阅读。正式引用请以期刊/会议版本为准（TVCG、CGF、PACMCGIT、ICCV 等）。

## 统计记录修正

2026-11-06 的迁移校验发现旧提取统计包含已排除的 active-caustics-2023，却未记录 dynamic-caustics-2025。现已按核心 PDF 重新提取并生成统计，26 篇共 388 页，未出现空白页或 OCR 触发。旧统计保留于 `meta/excluded/extract_stats_initial.json` 供追溯。
