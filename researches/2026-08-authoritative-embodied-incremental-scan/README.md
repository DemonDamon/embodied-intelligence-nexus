# 2026年8月权威来源增量扫描：候选台账与跨章节导航

> 作者：Damon Li | 更新日期：2026年8月27日
> 扫描窗口：2026年8月20日—2026年8月27日；较早论文仅在近期出现可核验项目/代码/数据或具有未覆盖的复现价值时补档。
> 证据口径：论文、官方项目/代码/模型/数据页为 A 级；大学、机构和公司官方发布为 B 级；公众号、媒体和聚合榜单仅为 C 级发现源。

本台账只记录本轮增量扫描的筛选过程与最终路径，不复述技术正文。其目的在于把“公众号或媒体发现”“官方公告”“论文实验”和“可复现 artifact”分开。没有命名的公众号文章或仅有二手报道的候选，不会被提升为技术事实。

## 1. 扫描范围与方法

本轮检查了 `cs.RO` 的近期预印本、作者/项目页、官方 GitHub、Hugging Face 资源页和具身智能生态的官方机构发布。候选必须同时满足相关性、新颖性/近期资源价值、至少一个 A 级来源和可写清方法/实验/复现边界的条件；核心技术文档优先要求两类独立一手来源。[1] [2]

| 来源类别 | 处理方法 | 本轮用途 |
|---|---|---|
| arXiv / HTML 原文 | 读取版本、方法、目标函数、任务与实验协议 | 验证 Pointing-VLA、GlanceWAM、VLA-REPLICA、TrAct、DECOWAM |
| 官方代码 / 模型 / 数据页 | 核验 LICENSE、发布物、环境、训练和评测脚本 | 验证 GlanceWAM、Embodied-R1.5、VLA-REPLICA、AIRSEAI |
| 大学项目页 / Linux Foundation | 核验项目归属、公开范围、生态或 workshop 状态 | 验证 VLA-REPLICA 与 AIRSEAI 的非论文事实 |
| 公众号、媒体和社交讨论 | 只提取候选实体和关键词，再回溯 A/B 级来源 | 没有单独构成技术结论 |

## 2. 已入选并完成独立归档的更新

| 条目 | 证据状态 | 归档位置 | 纳入原因 |
|---|---|---|---|
| AIRSEAI 1.0 / Linux Foundation 接纳 | B 级官方公告 + A 级代码 | [第 1 章 1.7](../../course/01-robot-grasping-intro/1.7-airseai-open-source-robot-stack-2026.md) | 2026-08-26 官方治理更新；1.0 代码、Apache-2.0 与明确硬件/ROS 依赖可核验。2.0/3.0 只作路线图。 [3] [4] |
| VLA-REPLICA | 预印本 + 大学项目页 + A 级代码/数据入口 | [第 5 章 5.12](../../course/05-imitation-learning/5.12-vla-replica-reproducible-real-world-benchmark-2026.md) | 低成本 SO-101 真机 VLA 评测的硬件、动作校准、ID/OOD 场景与代码可核验；论文虽早于本窗口，但项目资源具持续更新价值。 [5] [6] [7] |
| Pointing-VLA | 预印本 + A 级母项目代码/模型 | [第 7 章 7.29](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.29-pointing-vla-typed-spatial-grounding-2026.md) | 2026-08-24 新预印本，将点、功能区域和轨迹改为类型化隐藏状态读出；独立 Pointing-VLA artifact 未找到，已在正文标注。 [8] [9] [10] |
| GlanceWAM | 预印本 + A 级代码 + A 级 bundle | [第 7 章 7.30](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.30-glancewam-asynchronous-test-time-imagination-2026.md) | 2026-08-25 新预印本；异步 lookahead 想象、MIT 代码与公开 checkpoint/数据 bundle 同时可核验。 [11] [12] [13] |

## 3. 暂不制作技术文档的候选

| 候选 | 当前可核验证据 | 暂缓原因与后续触发条件 |
|---|---|---|
| TrAct（arXiv:2608.24101） | 论文原文与 HTML | 新近且相关，但本轮没有定位到独立项目页、代码、模型或数据入口。待至少出现第二类独立一手资源再进入核心文档。 [14] |
| DECOWAM（arXiv:2608.20114） | 论文页 | 论文自述 ARMDOG 数据和方法，但本轮未发现官方代码、模型、数据或独立项目资源；保留为观察候选。 [15] |
| Eximo、GOAG、Golem 等 | 搜索阶段候选 | 没有同时完成 A/B 级来源和实验/复现审计；不进入仓库正文。 |

## 4. 复核与后续跟踪

后续扫描应优先检查 TrAct、DECOWAM、Pointing-VLA 是否发布独立代码、checkpoint、数据卡、项目页或正式会议版本；并对 GlanceWAM 的真机评测、VLA-REPLICA 的跨实验室重复结果、AIRSEAI 2.0 的正式 release 进行版本化追踪。任何新增的公众号结论必须继续先进入线索层，再获得 A/B 级支持后归档。

## 5. 参考资料

[1]: https://arxiv.org/list/cs.RO/recent "arXiv Robotics 近期论文列表"
[2]: https://github.com/DemonDamon/embodied-intelligence-nexus/blob/main/skills/embodied-intel-updater/references/source-registry.md "本仓库具身智能信源注册表与证据等级"
[3]: https://www.linuxfoundation.org/press/lf-ai-data-foundation-welcomes-airseai-to-unite-open-source-embodied-ai-ecosystem "Linux Foundation：AIRSEAI 加入 LF AI & Data Foundation，2026-08-26"
[4]: https://github.com/AIRSEAI/AIRSEAI-1.0 "AIRSEAI 1.0 官方代码与 Apache-2.0 许可证"
[5]: https://arxiv.org/abs/2605.20774 "VLA-REPLICA arXiv 摘要与版本记录"
[6]: https://irvlutd.github.io/VLAReplica/ "UT Dallas VLA-REPLICA 项目页"
[7]: https://github.com/IRVLUTD/VLAReplica "IRVLUTD/VLAReplica 官方代码"
[8]: https://arxiv.org/abs/2608.23138 "Pointing-VLA arXiv 摘要与版本记录"
[9]: https://github.com/pickxiguapi/Embodied-R1.5 "Embodied-R1.5 官方代码与数据发布说明"
[10]: https://huggingface.co/IffYuan/Embodied-R1.5 "Embodied-R1.5 官方模型卡"
[11]: https://arxiv.org/abs/2608.23927 "GlanceWAM arXiv 摘要与版本记录"
[12]: https://github.com/linhanwang/GlanceWAM "GlanceWAM 官方代码（MIT）"
[13]: https://huggingface.co/datasets/LinhanWang/GlanceWAM "GlanceWAM 官方 checkpoint 与数据 bundle"
[14]: https://arxiv.org/abs/2608.24101 "TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks"
[15]: https://arxiv.org/abs/2608.20114 "DECOWAM: Decoupled Whole-Body World-Action Model"
