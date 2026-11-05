# CS184 与光传输研究

本仓库保存 CS184 课程材料，以及面向宏观场景光照与渲染的研究资料。当前研究从光镊实验中的可控扰动和响应测量获得启示，重点评估神经重打光、鲁棒焦散设计和波动光学精度选择。

**当前阶段：文献调研与实验设计。尚未实现候选算法，也没有实验结果证明其优于已有方法。** 已知可用研究硬件为用户的一台 RTX 5090 服务器，远程环境尚未检查。

| 入口 | 内容 |
|---|---|
| [Idea 意见报告](light-transport-survey/notes/IDEA_REVIEW.md) | 三个方向的定位、近邻工作、修订意见、实验方案及继续条件 |
| [异地开发交接](light-transport-survey/DEVELOPMENT.md) | 完整克隆、资料校验、工具环境、下一步开发任务 |
| [文献资料库](light-transport-survey/README.md) | 26 篇核心论文、提取文本、来源索引、检索工具 |
| [课程材料](CS184_2026/README.md) | 原有 CS184 课程资料和 final project 选题材料 |

**完整下载需要 Git LFS。** 仅下载 GitHub 的 ZIP 包不应作为已完整获取论文资料的依据。

```bash
git lfs install
git clone https://github.com/Teddy-Yangjiale/CS184.git
cd CS184
git lfs pull
python light-transport-survey/tools/verify_snapshot.py
```

上述校验命令只依赖 Python 标准库，检查文献资料快照中的文件大小和 SHA-256。论文、课程资料和第三方代码分别保留原作者的权利与许可；本仓库不为第三方内容另行授予许可。
