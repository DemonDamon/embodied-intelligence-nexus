# 具身智能研究源注册表

在触发 `embodied-intel-updater` 的“Source Selection”阶段读取本文件。该注册表用于优先级调度，不替代对单篇内容的逐项核验。

## 1. 证据等级与使用规则

| 级别 | 来源类别 | 可用于 | 不可用于 |
| :--- | :--- | :--- | :--- |
| A | 原始论文（arXiv、OpenReview、DOI、会议 proceedings）、官方代码/模型/数据页、正式基准页面 | 技术机制、推导、数据、实验、复现命令、许可证 | 无。仍需记录版本和访问日期。 |
| B | 作者/实验室主页、大学与研究机构公告、公司官方研究博客与产品文档 | 发布状态、项目背景、演示、官方披露的工程指标 | 不可将公司披露当作同行评审结论。 |
| C | 微信公众号、新闻媒体、聚合榜单、知乎/CSDN/论坛转述 | 发现候选、确定关键词、找出原始实体 | 不可单独支撑技术、实验、融资、产能或性能事实。 |

任何进入仓库的量化结论都必须至少有 A 级来源，或明确标为“公司官方披露”。若 A、B 级来源均不存在，仅写入“待核验线索台账”，不得制作成技术报告。

## 2. 学术与研究机构入口

| 名称 | 地址 | 用法 |
| :--- | :--- | :--- |
| arXiv robotics | https://arxiv.org/list/cs.RO/recent | 扫描新论文，回到具体论文页及源码链接。 |
| OpenReview | https://openreview.net/ | ICLR、CoRL 等评审稿、附录与 rebuttal。 |
| ICRA | https://2026.ieee-icra.org/ | 会议论文、workshop 与官方资料。 |
| RSS | https://roboticsconference.org/ | 机器人系统与理论论文。 |
| CoRL | https://www.corl.org/ | 机器人学习、操控与基础模型论文。 |
| MIT Embodied Intelligence | https://ei.csail.mit.edu/ | 感知、语言、学习与规划研究线索。 |
| 清华大学具身智能与机器人研究院 | https://eir.tsinghua.edu.cn/ | 机构研究和公开活动线索。 |
| 北京大学具身智能与机器人研究中心 | https://www.ai.pku.edu.cn/kxyj1/tyrgznyjs/jsznyjqryjzx.htm | 机构研究线索。 |
| 复旦大学可信具身智能研究院 | https://teai.fudan.edu.cn/ | 可信具身研究线索。 |
| AIRS Center for Embodied AI | https://airs.cuhk.edu.cn/en/research/1138 | 多模态具身系统研究线索。 |

## 3. 代码、模型、数据与基准入口

| 类型 | 优先入口 | 核验动作 |
| :--- | :--- | :--- |
| 代码 | GitHub 原作者/机构组织 | 检查 README、LICENSE、release、commit 活跃度、issue、复现脚本。 |
| 模型 | Hugging Face、ModelScope 官方组织页 | 检查模型卡、基座模型、权重许可、推理硬件、版本与安全说明。 |
| 数据 | Hugging Face Datasets、官方项目页、论文附录 | 检查数据卡、样本量、模态、split、访问条件、许可、隐私与复现脚本。 |
| 基准 | 官方 benchmark 主页/提交仓库 | 检查任务定义、评分函数、评测硬件、是否真机、排行榜版本与提交协议。 |

优先追踪的开源生态包括：LeRobot、OpenVLA、Octo、Isaac Lab、MuJoCo、Genesis、Habitat、AI2-THOR、Open X-Embodiment、D4RL、Minari 及其官方仓库。

## 4. 工业界官方入口

| 公司 / 平台 | 官方入口 | 关注点 |
| :--- | :--- | :--- |
| NVIDIA Robotics / Isaac | https://developer.nvidia.com/isaac | 仿真、GR00T、Cosmos、部署工具。 |
| Google DeepMind Robotics | https://deepmind.google/discover/blog/ | RT 系列、Gemini Robotics、数据与评测。 |
| Unitree | https://www.unitree.com/ | 硬件、赛事、SDK、真机评测。 |
| AgiBot | https://www.agibot.com/ | 本体、数据与模型的官方披露。 |
| Galbot | https://www.galbot.com/ | 机器人产品与技术公告。 |
| Galaxea | https://galaxea-ai.com/ | 本体与具身基础模型。 |
| UBTECH | https://www.ubtrobot.com/ | 工业人形产品与部署。 |
| Figure | https://www.figure.ai/ | 人形产品与官方研究发布。 |
| Tesla AI & Robotics | https://www.tesla.com/AI | 公开 AI / Robotics 工程信息。 |
| Generalist AI | https://generalistai.com/blog | 官方研究博客；须标注为公司披露。 |
| Dyna Robotics | https://www.dyna.co/research | 官方研究博客；须标注为公司披露。 |
| Robbyant | https://technology.robbyant.com/ | LingBot 系列技术、代码、模型入口。 |
| YOUIBOT | https://zh.youibot.com/ | 工业具身平台与官方公告。 |

## 5. 发现源：只作线索，不作证据

下列来源可用于扩大候选池，但每条候选都必须回溯至 A/B 级来源：机器人大讲堂、具身研习社、古月居、具身智能之心、量子位、新智元、机器之心、36氪·硬科技、公众号/媒体聚合榜单、知乎、CSDN、百度百科和营销博客。

## 6. 本轮已验证的示范资源

- Khora: https://arxiv.org/abs/2608.08600
- LingBot-VLA 2.0: https://arxiv.org/abs/2607.06403
- FabriVLA: https://arxiv.org/abs/2607.08575
- UniBot: https://unibot.unitree.com/
- MotionDecode: https://huggingface.co/datasets/CMRobot/MotionDecode
- World Models: https://arxiv.org/abs/1803.10122
- DIAMOND: https://arxiv.org/abs/2405.12399

更新本表时，优先添加稳定的一级入口而非单篇新闻链接。
