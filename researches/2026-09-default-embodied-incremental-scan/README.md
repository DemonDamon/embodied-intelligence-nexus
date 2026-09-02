# 2026年9月默认具身智能增量扫描：固定公众号与权威来源台账

> 作者：Damon Li | 更新日期：2026年9月2日
> 扫描窗口：2026年8月28日—2026年9月2日（GMT+8）
> 证据口径：固定公众号合集为 **P1 / C 级发现源**；技术事实只使用 A/B 级论文、项目页、官方代码、模型/数据卡或公司技术资料。

本台账记录首次依据 `embodied-intel-updater` 新增的默认触发规则执行的全流程扫描。其职责是保存来源、候选、排除理由和跨章节链接；不重复承载已归档技术文档的完整正文。

## 固定发现源扫描

两个深蓝具身智能合集已在本次任务开头读取。可见条目的最新时间分别为 2026-08-01 UTC 和 2026-08-27 UTC，均早于本轮扫描窗口的起点。故本轮没有把它们的可见条目当作新的可归档更新；这一判断只表示**本次可读取页面中未发现窗口内候选**，不代表公众号在窗口内绝对没有发布内容。[1]

| P1 合集 | 本次可见主题 | 与窗口的关系 | 本轮处置 |
|---|---|---|---|
| 具身智能深度盘点 | 海内外具身智能实验室与产业盘点 | 最新可见条目早于 2026-08-28 | 已读取并登记为 C 级来源；没有用盘点文字证明技术事实 |
| 技术拆解梳理 | MoE、VAE、人形 RL、机器人学习算法 | 最新可见条目为 2026-08-27 UTC 或更早 | 已读取并登记为 C 级来源；保留为下一轮领域检索线索 |

## 候选筛选与归档

| 候选 | 来源组合 | 窗口状态 | 处置 | 归档 / 观察位置 |
|---|---|---|---|---|
| Facet-0 / ManuFacet-1K | 预印本、NTU/PINE 作者项目页、Hugging Face 模型页、数据卡 | 论文 v1：2026-09-01 | 通过；接触密集精密装配的动作—wrench 表示、价值后训练与公开资源可审计 | [第 7 章 7.31](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.31-facet0-contact-rich-precision-manipulation-2026.md) |
| LeRobot Community Dataset V3 | 官方数据卡/API、LeRobot 官方仓、ICLR 2026 论文 | 数据卡 API 最后修改：2026-08-30 | 通过；作为异构社区数据契约与复现摩擦的独立数据基础设施条目 | [第 5 章 5.13](../../course/05-imitation-learning/5.13-lerobot-community-dataset-v3-2026.md) |
| TrAct v2 | arXiv v2 | 2026-08-30 | 降级观察；论文机制与作者报告结果可读，但项目页仍为占位 URL，未见作者 artifact | 本台账“观察候选” |
| UniArmL1 | Unitree 官方代码、`unitree_lerobot` 官方文档 | 2026-08-28 有 9 个提交 | 降级观察；提交主要为 README、VLA demo 与媒体，未见 release 或可审计算法/硬件/数据版本实质更新 | 本台账“观察候选” |
| Zero-WAM v2 | arXiv、作者项目页、官方 GitHub | 2026-08-27 | 本轮不补档；早于窗口，且代码/模型/数据仍标为计划发布 | 本台账“窗口外” |

## 观察候选与下一步核验

TrAct v2 的论文提出以 2D visual tracks 连接 policy 和 world model，并报告 LIBERO-INTEGRAL 与 Franka 真机改善；但 arXiv HTML 中的项目链接仍是 `your-project-page.github.io/tract/` 占位地址，论文页也没有列出作者代码、数据或演示 artifact。因此本轮不把它升格为核心课程文档。[2]

UniArmL1 的 2026-08-28 提交确实发生在窗口内，但提交说明集中于 README、演示布局、VLA demo 和图像资产；它没有形成可比对的 release 或新算法/数据版本。它保持为官方开源工具链的活动信号，而非本轮新的技术结论。[3] [4]

Zero-WAM 的论文和项目页具备较完整的研究描述，且官方仓为 Apache-2.0；然而其页面明确将代码、模型和数据列为计划在 2026-09-15 前发布，且论文 v2 早于本轮窗口。后续应在承诺日期之后检查实际 artifact，而不把计划误写为可复现资源。[5] [6]

## 质量与可追溯性

核心文档均使用参考式数字引文，并明确模型、数据、许可证、代码与缺口。提交前需再次检查：两个 P1 合集均有已读取/访问受限记录、父级 README 和根 README 均可导航、新增文档通过 `validate_research_docs.py`，且暂存区没有临时台账、Cookie、令牌、`.env` 或下载的数据副本。

## 参考资料

[1]: ../../skills/embodied-intel-updater/references/wechat-discovery-sources.md "深蓝具身智能固定公众号发现源配置"
[2]: https://arxiv.org/html/2608.24101v2 "TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks — arXiv HTML"
[3]: https://github.com/unitreerobotics/UniArmL1 "UniArmL1 — Unitree official GitHub repository"
[4]: https://github.com/unitreerobotics/unitree_lerobot "unitree_lerobot — Unitree official LeRobot integration"
[5]: https://arxiv.org/abs/2608.26103 "Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization"
[6]: https://github.com/robbyant-research/Zero-WAM "Zero-WAM — official GitHub repository"
