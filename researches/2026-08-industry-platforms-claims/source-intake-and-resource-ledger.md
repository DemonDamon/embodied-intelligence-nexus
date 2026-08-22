# 2026年8月具身智能资料入口与资源追溯台账

> 作者：Damon Li
> 更新日期：2026年8月22日
> 用途：记录本次用户提供的入口、已核验一手资源、归档位置与未公开边界。该台账不是论文目录的替代品；具体技术说明见各归档文档。

## 1. 处理原则

本台账按“入口—实体—一手来源—落盘位置”建立可追溯关系。微信公众号、媒体或个人网页可以提供选题线索，但对于模型参数、训练数据规模、实验指标、量产计划、融资和开源状态，均需回到论文原文、官方项目页、官方仓库或官方数据托管页交叉确认。若无法确认，则在“状态”栏标为**未公开 / 待核验**。

## 2. 入口归档总表

| # | 用户入口 | 主题与主要实体 | 证据状态 | 已归档位置 |
| :---: | :--- | :--- | :--- | :--- |
| 1 | [Khora](https://mp.weixin.qq.com/s/ONS1M4qMnh5xMRV_sB69Ug) | RhOS-World: Khora、多智能体世界模型 | A：有 arXiv 与项目页 | [7.11](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.11-world-action-models-2026.md) |
| 2 | [LingBot-VLA 2.0](https://mp.weixin.qq.com/s/srAP6fl30SqMfOOXUW__wQ) | LingBot-VLA 2.0 | A：论文、代码、HF、ModelScope | [7.10](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.10-lingbot-and-fabrivla-2026.md) |
| 3 | [LingBot-VA 2.0](https://mp.weixin.qq.com/s/UfyQkKHechSYr3MkK8orGQ?scene=1) | LingBot-VA 2.0 | B/A：官方技术页与技术报告 | [7.10](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.10-lingbot-and-fabrivla-2026.md) |
| 4 | [UniBot](https://mp.weixin.qq.com/s/WNntWcVaPqlKagEWeWkNMg) | UniBot-V1、Unitree G1、DAPTO 2 | A：赛事与提交资源；DAPTO 2 未确认 | [7.12](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.12-humanoid-vla-and-real-robot-evaluation.md) |
| 5 | [世界模型历史](https://mp.weixin.qq.com/s/YHr0X2tXk6R9h1TCObWMJA) | World Models、Dreamer、MuZero、JEPA、IRIS、Genie、GAIA、DIAMOND | A：经典论文/部分开源；企业模型权重不全公开 | [7.13](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.13-world-models-and-simulators-resource-map.md) |
| 6 | [Tesla / Terafab](https://mp.weixin.qq.com/s/XoIIN-eR59nebjTx4m4zDA) | Optimus、Terafab、AI5、Grok | B：官方概述；量化数字未确认 | [Tesla 核验](./tesla-optimus-terafab-ai5-grok-verification.md) |
| 7 | [FabriGym](https://mp.weixin.qq.com/s/or6JEEvLS3C2HW7TTVRMhw) | FabriGym、FabriX、FabriVLA | A/B：FabriVLA 论文、企业平台页；平台代码未公开 | [7.10](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.10-lingbot-and-fabrivla-2026.md) |
| 8 | [共生知行 DPC](https://mp.weixin.qq.com/s/bhtdsYxarxgZqvC1ufJ1Lw) | DPC、QUAR-VLA、Humanoid-VLA、VLA-Adapter、OpenWBC | A：多项论文/代码；DPC 产品细节未确认 | [7.12](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.12-humanoid-vla-and-real-robot-evaluation.md) |
| 9 | [丁鹏翔主页](https://dingpx.github.io/) | QUAR-VLA、CARP、TrajBooster 等 | A：作者主页和多项项目资源 | [7.12](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.12-humanoid-vla-and-real-robot-evaluation.md) |
| 10 | [GEN-1.5](https://mp.weixin.qq.com/s/O8AYpvyGz1ywrvMeh4mKrw) | Generalist AI GEN-1.5 | B：官方博客；论文/权重未公开 | [7.11](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.11-world-action-models-2026.md) |
| 11 | [Dyna-2](https://mp.weixin.qq.com/s/_1nWy6AZLkqMfj5W4aHQ_g) | Dyna Robotics Dyna-2 | B：官方研究博客；论文/权重未公开 | [7.11](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.11-world-action-models-2026.md) |
| 12 | [物理仿真到世界模型](https://mp.weixin.qq.com/s/ju2ymeVW75WnJsExEErpLw) | 具身智能综述、Genesis、MuJoCo、Isaac Lab、Habitat、AI2-THOR | A：论文与官方平台资源 | [7.13](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.13-world-models-and-simulators-resource-map.md) |
| 13 | [MotionDecode](https://chingmudata.github.io/MotionDecode/) | ChingMu 1000-Hour Embodied Motion Dataset | A：项目主页、HF 数据页 | [5.7](../../course/05-imitation-learning/2026-08-motiondecode-dataset/5.7-motiondecode-embodied-motion-dataset.md) |
| 14 | [Xiaomi-Robotics-1](https://arxiv.org/abs/2607.15330) | 100K+ 小时 UMI 预训练 VLA | A：arXiv 论文、项目页；代码/模型承诺开源 | [7.14](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.14-xiaomi-robotics-1-vla-2026.md) |
| 15 | [NebulaVLA](https://arxiv.org/abs/2608.16503) | 双频 VLA + GESTURE-7 | A：arXiv 论文 | [7.15](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.15-vla-architecture-innovations-2026.md) |
| 16 | [ExToken](https://arxiv.org/abs/2607.12931) | VLA-RL 结构化探索 | A：arXiv 论文 | [7.16](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.16-vla-post-training-rl-2026.md) |
| 17 | [Robot-Factored WM](https://arxiv.org/abs/2607.22535) | URDF 渲染解耦世界模型 | A：arXiv 论文、项目页 | [7.17](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.17-world-models-for-robotics-2026.md) |
| 18 | [ω-0](https://arxiv.org/abs/2608.06375) | 人形并发 loco-manipulation WAM + ω-HOME 数据集 | A：arXiv 论文 | [7.18](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.18-humanoid-world-models-2026.md) |
| 19 | [Handroid](https://arxiv.org/abs/2607.16187) | 27-DoF 可重构双本体平台 | A：arXiv 论文、项目页 | [4.7](../../course/04-deep-learning-grasping/4.7-dexterous-manipulation-2026.md) |
| 20 | [FM-VLA](https://arxiv.org/abs/2607.18231) | 力记忆 VLA | A：arXiv 论文、项目页 | [4.7](../../course/04-deep-learning-grasping/4.7-dexterous-manipulation-2026.md) |
| 21 | [Open-AoE](https://arxiv.org/abs/2607.14183) | 2000h 手机采集第一人称操纵数据集 | A：arXiv 论文 | [5.8](../../course/05-imitation-learning/5.8-embodied-datasets-benchmarks-2026.md) |
| 22 | [DexVerse](https://arxiv.org/abs/2607.08751) | 100任务/3臂/6手灵巧操作基准 | A：arXiv 论文、项目页 | [5.8](../../course/05-imitation-learning/5.8-embodied-datasets-benchmarks-2026.md) |
| 23 | [AGIBOT WAIC 2026](https://www.agibot.com/article/231/detail/85.html) | A3 Ultra、X2 Edu、G2 Max、OmniHand 3 | B：官方产品发布 | [产业补充](./industry-supplement-august-2026.md) |
| 24 | [Galbot ET1](https://www.xinhuanet.com/digital/20260821/e172222483dc4d75a357145caa74d9d0/c.html) | 双足人形 + 银河星脑 | B/C：新华网报道 | [产业补充](./industry-supplement-august-2026.md) |
| 25 | [NVIDIA GR00T N1.7](https://github.com/nvidia/isaac-gr00t) | GR00T N1.7 GA + Cosmos 3 + Isaac Lab v2.3.2 | B：GitHub + 官方博客 | [产业补充](./industry-supplement-august-2026.md) |

## 3. 关键论文、代码、模型与数据入口

### 3.1 已公开论文与代码

- Khora：[论文](https://arxiv.org/abs/2608.08600)、[项目页](https://rhos.ai/research/khora)。
- LingBot-VLA 2.0：[论文](https://arxiv.org/abs/2607.06403)、[代码](https://github.com/robbyant/lingbot-vla-v2)、[HF 集合](https://huggingface.co/collections/robbyant/lingbot-vla-v2)、[ModelScope 集合](https://modelscope.cn/collections/Robbyant/LingBot-VLA-V2)。
- FabriVLA：[论文](https://arxiv.org/abs/2607.08575)。
- UniBot：[官方主页](https://unibot.unitree.com/)、[提交仓库](https://github.com/unitreerobotics/unibot_submission)、[HF 集合](https://huggingface.co/collections/unitreerobotics/unibot-v1-challenge)。
- QUAR-VLA：[论文](https://arxiv.org/abs/2312.14457)、[项目页](https://sites.google.com/view/quar-vla/quar-vla-eccv24)。
- Humanoid-VLA：[论文](https://arxiv.org/abs/2502.14795)。
- CARP：[论文](https://arxiv.org/abs/2506.13725)、[项目页](https://carp-robot.github.io/)、[代码](https://github.com/ZhefeiGong/carp)。
- VLA-Adapter：[项目页](https://vla-adapter.github.io/)、[代码](https://github.com/OpenHelix-Team/VLA-Adapter)、[模型组织](https://huggingface.co/VLA-Adapter)。
- TrajBooster：[论文](https://arxiv.org/abs/2509.11839)、[代码](https://github.com/jiachengliu3/OpenTrajBooster)。
- OpenWBC：[代码](https://github.com/jiachengliu3/WBC_Deploy)。

### 3.2 已公开数据与仿真平台

- MotionDecode：[项目页](https://chingmudata.github.io/MotionDecode/)、[Hugging Face](https://huggingface.co/datasets/CMRobot/MotionDecode)。
- MuJoCo：[官方代码](https://github.com/google-deepmind/mujoco)。
- Isaac Lab：[官方代码](https://github.com/isaac-sim/IsaacLab)。
- Genesis：[官方代码](https://github.com/Genesis-Embodied-AI/genesis-world)。
- Habitat：[官网](https://aihabitat.org/)。
- AI2-THOR：[官网](https://aithor.allenai.org/)。

## 4. 未公开或不能确认的内容

| 条目 | 处理结论 |
| :--- | :--- |
| Khora 代码和权重 | 论文与项目页可访问；未在官方组织中确认公开训练代码和权重。 |
| GEN-1.5 与 Dyna-2 | 有企业官方技术披露；未确认同行评审论文、官方代码或权重下载。 |
| FabriGym / FabriX | 有企业平台信息；未确认官方开源代码、模型权重或数据下载。 |
| DPC 产品技术细节 | 仅获得媒体线索；未确认完整一手论文、项目页或开源实现。 |
| DAPTO 2 | 未发现与 UniBot 相关的一手赛事、论文或数据集来源。 |
| Tesla Terafab 量化数据 | 投资额、算力、量产时间等未在本次核验的官方页面中完整确认。 |

## 5. 维护约定

新增资料时，应保留原始入口 URL，并补充官方论文/项目/代码/数据链接和访问日期。若后来出现原先未公开的权重、数据或论文，应修改本台账中对应的“未公开”状态，并在专题文档中加入版本与许可证说明。
