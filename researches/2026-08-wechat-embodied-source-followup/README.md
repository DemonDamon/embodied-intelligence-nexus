# 2026年8月公众号具身智能线索：来源台账与跨章节导航

> 作者：Damon Li | 更新日期：2026年8月25日
> 证据状态：公众号文章仅作 C 级发现线索；技术事实已回溯至论文、正式会议页、官方项目页或官方代码页。

本目录**不再承担单一大而全的技术报告**。它只保存用户输入的公众号线索、访问约束和跨课程归档导航。7 个主题的理论推导、实验审计、复现资源和局限性已分别写入最贴近的课程章节或研究专题，避免将自动驾驶、人形模仿学习、世界模型和多机器人系统混写。

## 目录内容

| 文档 | 内容 | 适用用途 |
|---|---|---|
| [七篇公众号线索的一手来源台账](./source-ledger-seven-wechat-entries.md) | 原始链接、去重关系、证据等级、最终独立归档位置 | 追溯来源与定位研究文档 |

## 最终归档导航

| 主题 | 最终文档 | 归档理由 |
|---|---|---|
| XCoT-VLA | [7.22 可执行思维链驾驶 VLA](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.22-xcot-vla-executable-cot-driving-2026.md) | VLA 的推理接口、轨迹生成与世界模型边界 |
| LATENT / AstraTennis 线索 | [5.9 人形网球模仿学习](../../course/05-imitation-learning/5.9-latent-humanoid-tennis-imitation-2026.md) | 不完美人类运动片段、动作跟踪与 sim-to-real |
| 具身 MoE | [7.23 VLA 与世界模型中的 MoE](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.23-moe-for-vla-and-world-models-2025-2026.md) | 动作专家与异构控制世界模型的机制对照 |
| RSS 2026 多机器人闭环系统 | [闭环多智能体多机器人操作](../2026-08-rss-closed-loop-multi-robot-manipulation.md) | LLM agent workflow、验证与恢复的系统研究 |
| MVA | [7.24 Masked Visual Actions 世界模型](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.24-masked-visual-actions-unified-world-model-2026.md) | 像素空间动作接口、前向 rollout 与逆向动作生成 |
| VLA/VLN/世界模型综述 | [7.25 综述阅读图谱](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.25-vla-world-model-survey-reading-map-2026.md) | 区分 VLA、VLN 和世界模型的任务/评测 |
| DriveVLA-M0 | [8.4 故障记忆与测试时适配](../../course/08-engineering-experience/2026-08-vla-inference-performance/8.4-drivevla-m0-failure-aware-memory-2026.md) | NAVSIM 协议、TTT 开销与部署边界 |

## 重要证据边界

原始公众号正文受到访问验证限制，因而所有线索均未被直接当作事实。特别地，XCoT-VLA 尚无可核验的端到端硬件时延公开证据；LATENT 的完整高层策略、数据与 sim-to-real 代码未完全开放；DriveVLA-M0 的 26.44 ms 仅为特定基准中 TTT 反向传播额外开销；MVA 的视频 rollout 相关性并不等于真实机械控制成功率。详见各独立文档。
