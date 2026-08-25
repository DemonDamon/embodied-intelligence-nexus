# 七篇公众号具身智能线索的一手来源台账

> 作者：Damon Li | 更新日期：2026年8月25日
> 作用：本文件只登记输入线索、证据等级、访问限制与最终归档位置；**不重复存放技术推导、实验审计或复现说明**，相关内容必须阅读链接的独立文档。

## 1. 输入处理与访问限制

用户提供 8 项输入，其中第 3、4 项 URL 完全相同，故去重为 7 个主题。浏览器访问全部原始微信公众号链接均遇到微信验证；文本读取仅获得标题和发布主体。依照本仓库的信源规则，公众号材料均为 **C 级发现线索**，不得单独支持技术、性能、开源或部署事实。

## 2. 线索—证据—归档映射

| 编号 | 公众号线索 | 一手/官方核验对象 | 证据状态 | 最终独立文档 |
|---:|---|---|---|---|
| 1 | [小鹏再推 XCoT-VLA：这次解决的是推理延迟问题][w1] | XCoT-VLA 预印本；小鹏 X-World 官方技术页 | 预印本 + 官方披露 | [7.22 XCoT-VLA][d1] |
| 2 | [AstraTennis 时刻来了！人形机器人全球首次挑战单打、混双][w2] | LATENT 预印本、项目页、官方代码 | 预印本 + 部分开源；赛事叙述待核验 | [5.9 LATENT][d2] |
| 3/4 | [拆解 MoE 混合专家模型在具身中的应用][w3] | AdaMoE-VLA、Worldscape-MoE | 两篇预印本；AdaMoE 代码公开 | [7.23 具身 MoE][d3] |
| 5 | [RSS26｜中山大学等闭环多智能体框架让多机器人协同操作无惧现实干扰][w5] | RSS 2026 Paper 36、arXiv 论文 | 正式会议页 + 预印本；端到端代码待核验 | [RSS 多机器人闭环框架][d4] |
| 6 | [李飞飞团队全新统一世界模型：15小时数据兼顾正向仿真、逆向动作生成][w6] | Masked Visual Actions 论文、项目页、代码 | 预印本 + 代码/权重入口 | [7.24 MVA][d5] |
| 7 | [一文梳理具身智能必读 6 篇综述：从 VLA、VLN 到世界模型][w7] | VLA、世界模型、广义具身 AI 综述 | 阅读图谱；原“六篇”清单未能核验 | [7.25 综述图谱][d6] |
| 8 | [中科院&长安开源 DriveVLA-M0：26ms超低延迟，零训练持续涨点！][w8] | DriveVLA-M0 预印本、官方代码 | 预印本 + Apache-2.0 代码 | [8.4 DriveVLA-M0][d7] |

## 3. 归档原则

技术正文按“最贴近的课程/研究主题”分别落在：模仿学习（LATENT）、VLA/世界模型（XCoT-VLA、MoE、MVA、综述）、工程经验（DriveVLA-M0）和研究专题（RSS 多机器人闭环框架）。这样可避免将自动驾驶时延、人形模仿学习、生成世界模型和多机器人 agent workflow 混放在单一报告中。

| 主题类型 | 归档原因 | 不应混放的对象 |
|---|---|---|
| 模仿学习与 sim-to-real | LATENT 的核心是从不完美动作片段学习全身技能 | 不能与自动驾驶规划或视频世界模型共用实验表 |
| VLA/世界模型 | XCoT、MoE、MVA 的方法层与控制接口可对照学习 | 不能与赛事新闻或行业宣传混写 |
| 工程时延与部署 | DriveVLA-M0 的 TTT 开销必须单列解释 | 不能当作 VLA 通用实时性结论 |
| 多机器人系统 | RSS 论文核心是闭环 agent workflow | 不能化约为单模型训练损失 |

## 4. 参考入口

[w1]: https://mp.weixin.qq.com/s/hinTiDyAtqhBx5BZ4ndLMw
[w2]: https://mp.weixin.qq.com/s/gCNJS4aJxPGon8Nq1sxoEg
[w3]: https://mp.weixin.qq.com/s/-vi2f03oOcgCyFq-SEkeNg
[w5]: https://mp.weixin.qq.com/s/bkm1kgB1cjqsAWyMwuZMmQ
[w6]: https://mp.weixin.qq.com/s/5fNqnoxSiskyAamN0EfBSA
[w7]: https://mp.weixin.qq.com/s/TQGIbJYUfwdmLqtxP-0WiQ
[w8]: https://mp.weixin.qq.com/s/WkXaLD6dhKNIGpcZFNPTvg
[d1]: ../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.22-xcot-vla-executable-cot-driving-2026.md
[d2]: ../../course/05-imitation-learning/5.9-latent-humanoid-tennis-imitation-2026.md
[d3]: ../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.23-moe-for-vla-and-world-models-2025-2026.md
[d4]: ../2026-08-rss-closed-loop-multi-robot-manipulation.md
[d5]: ../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.24-masked-visual-actions-unified-world-model-2026.md
[d6]: ../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.25-vla-world-model-survey-reading-map-2026.md
[d7]: ../../course/08-engineering-experience/2026-08-vla-inference-performance/8.4-drivevla-m0-failure-aware-memory-2026.md
