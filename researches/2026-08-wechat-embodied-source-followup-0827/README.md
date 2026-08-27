# 2026年8月两篇公众号具身智能线索：来源台账与跨章节导航

> 作者：Damon Li | 更新日期：2026年8月27日
> 用途：保存用户输入、文章可访问性、证据等级和最终归档位置；技术推导、实验审计和资源边界仅保存在相应课程文档中。

两篇输入文章仅取得标题与发布主体，未获得可用于技术验证的完整正文。因此它们都按 C 级发现线索处理。每个主题均已回溯到论文、官方项目页、官方代码或官方数据卡；下表明确最终技术事实的来源位置。

| 编号 | 输入线索 | 可核验主题 | 最终独立文档 | 关键 A/B 级来源 |
|---:|---|---|---|---|
| 1 | [具身数据有了全模态的转向](https://mp.weixin.qq.com/s/-g6Kfpo_ZMFWbrnf1cWYAg) | 同步多模态数据契约、跨本体采集、触觉/移动操作、人类第一视角到机器人转换 | [5.11 全模态具身数据](../../course/05-imitation-learning/5.11-multimodal-embodied-data-infrastructure-2026.md) | AGIBOT WORLD 2026 数据卡；RoboMIND 2.0 论文/项目页；Open-AoE 论文/官方仓 |
| 2 | [具身智能四大核心模型分析（VA / VLA / WM / WAM）](https://mp.weixin.qq.com/s/sWOtJoHuO7qCtWc3RVSI7g) | VA 术语消歧、VLA 条件策略、WM 条件动态、Cascaded/Joint WAM | [7.28 VA/VLA/WM/WAM 分类](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.28-va-vla-wm-wam-taxonomy-2026.md) | VLA Survey；WAM Survey；LingBot-VA/2.0 论文与官方代码；NVIDIA 技术说明 |

## 归档判定

“全模态具身数据”落在第 5 章模仿学习，因为它回答如何把观察、演示和动作监督组织为可训练 episode，涉及 human-to-robot retargeting 与行为策略训练。VA/VLA/WM/WAM 术语比较落在第 7 章，因为其核心是条件策略、预测动态和世界—动作联合建模，而不是单个数据集或特定本体的实现细节。

> **术语边界。** 本台账不把 VA 作为确定的第四类学术标准。它在不同材料中可能指 Vision-Action 或 Video-Action；技术文档仅对具有完整论文名称、输入/输出和目标函数的具体用法作出定义。

| 不应混同的概念 | 正确处理 |
|---|---|
| 更多模态与可用数据 | 只有同步、坐标/单位、缺失掩码、质量标记和许可齐备，模态才可安全进入训练。 |
| 人类第一视角与机器人动作 | 人手/相机轨迹必须经过本体相关的 action-semantics adaptation，不能直接当作 robot action。 |
| WM 与 WAM | WM 可以独立预测动态；WAM 要求预测的 future 在产生、筛选、训练或验证动作的路径中发挥作用。 |
| WAM 与 VLA 的性能优劣 | 不同本体、动作空间、数据和推理预算的分数不可直接比较。 |
