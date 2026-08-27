# 第五章：模仿学习

> 作者：Damon Li | 更新日期：2026年8月27日

本章将深入探讨模仿学习（Imitation Learning）在机器人抓取与操作中的应用。我们将从模仿学习的介绍、行为克隆、交互式模仿学习、逆强化学习以及其他相关方法等方面进行详细阐述，展示机器人如何通过观察和模仿人类或专家行为来学习复杂技能。

## 章节目录

- [5.1 回顾](./5.1-recap.md)
- [5.2 模仿学习介绍](./5.2-intro-to-imitation-learning.md)
- [5.3 行为克隆](./5.3-behavior-cloning.md)
- [5.4 交互式模仿学习](./5.4-interactive-imitation-learning.md)
- [5.5 逆强化学习](./5.5-inverse-reinforcement-learning.md)
- [5.6 其他方法与讨论](./5.6-other-methods-and-discussions.md)
- [2026年8月具身动作数据集更新：MotionDecode](./2026-08-motiondecode-dataset/README.md)
  - 覆盖 ChingMu 1000 小时具身动作数据集的模态、下载、许可核验、人形重定向与模仿学习使用边界。
- [5.8 2026年8月具身数据集与基准更新](./5.8-embodied-datasets-benchmarks-2026.md)
  - 覆盖 Open-AoE（2000h 手机采集第一人称操纵数据集与工具链）和 DexVerse（100任务/3臂/6手模块化灵巧操作基准）。
- [5.9 LATENT：从不完美人类运动片段学习人形网球技能](./5.9-latent-humanoid-tennis-imitation-2026.md)
  - 审计动作跟踪、在线蒸馏、高层策略、sim-to-real 与 Unitree G1 真机部署的公开程度；不将赛事新闻替代为论文实验。
- [5.10 从人类视频到机器人操作：VLA 表征桥接综述](./5.10-human-videos-to-vla-survey-2026.md)
  - 以 latent action、预测世界模型、显式 2D 与显式 3D 四类 bridge 组织人类视频到机器人动作迁移；区分第一视角线索与机器人可执行动作监督。
- [5.11 全模态具身数据：从观测—动作对到同步数据基础设施](./5.11-multimodal-embodied-data-infrastructure-2026.md)
  - 以 AGIBOT WORLD 2026、RoboMIND 2.0 与 Open-AoE 审计同步模态、动作语义、质量控制、数据许可与跨本体复用边界。
- [5.12 VLA-REPLICA：低成本可复现真机 VLA 评测基准](./5.12-vla-replica-reproducible-real-world-benchmark-2026.md)
  - 以 SO-101 动作归一化、AprilTag/图像叠加标定、10 项任务与 ID/OOD 场景审计真实评测的可复现条件；它是小规模 target-domain 适配/评测资源，不是大规模预训练数据。
