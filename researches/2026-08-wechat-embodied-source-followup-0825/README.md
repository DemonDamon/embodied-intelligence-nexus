# 2026年8月三篇公众号具身智能线索：来源台账与跨章节导航

> 作者：Damon Li | 更新日期：2026年8月25日
> 用途：本目录保存用户输入、原始内容可访问性、证据等级和最终归档位置；技术推导、实验审计和复现资源只保存在相应课程文档中。

三篇公众号文章均只能读取标题和发布主体，未获得完整正文；因此它们均按 C 级发现线索处理。每个主题已回溯到至少一份论文及项目页、官方代码或资源仓，技术结论均以这些 A/B 级来源为准。

| 编号 | 输入线索 | 已回溯的一手实体 | 证据状态 | 最终独立文档 |
|---:|---|---|---|---|
| 1 | [物理世界 JEPA / PSG-JEPA](https://mp.weixin.qq.com/s/wPbRp-JjyMEl69X8TyYg1g) | PSG-JEPA；arXiv、作者项目页、官方代码 | 预印本 + 项目页 + 代码 | [7.26 PSG-JEPA](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.26-psg-jepa-physical-state-grounding-2026.md) |
| 2 | [第一视角视频走向具身](https://mp.weixin.qq.com/s/I9FK1bUuvNIyXIvm3Xbv9Q) | 《From Human Videos to Robot Manipulation》；IJCAI 2026、项目页、资源仓 | 同行评审 Survey Track + 资源仓 | [5.10 人类视频到 VLA 综述](../../course/05-imitation-learning/5.10-human-videos-to-vla-survey-2026.md) |
| 3 | [从物理仿真到世界模型](https://mp.weixin.qq.com/s/ju2ymeVW75WnJsExEErpLw) | 《Learning Embodied Intelligence from Physical Simulators and World Models》；arXiv v3、官方资源仓 | 预印本 + Apache-2.0 资源仓；原知乎文章仅线索 | [7.27 仿真器与世界模型](../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/7.27-simulators-and-world-models-survey-2025.md) |

## 归档原则

PSG-JEPA 与“仿真器—世界模型”综述都落在第 7 章，因为前者研究动作条件 latent dynamics 的物理可读性，后者研究内在动态模型与外在仿真环境的互补性。人类视频综述落在第 5 章，因为其问题核心是从无动作标签的人类视频向机器人模仿/VLA 学习迁移，而非一般视觉识别。

| 不应混同的概念 | 正确区分 |
|---|---|
| PSG-JEPA 与一般视频生成 | PSG-JEPA 是 action-conditioned latent world model，以训练期状态/转移锚定增强物理可读性，并非像素生成器。 |
| 第一视角视频与机器人动作标签 | 第一视角视频提供人类交互线索；仍需 representation bridge 和机器人数据/动作空间对齐。 |
| 物理仿真器与世界模型 | 前者是显式可控外部环境，后者是数据驱动的内在预测模型；二者均需面向真机进行独立误差审计。 |
