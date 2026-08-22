# 九篇推文：一手来源、资源与证据边界台账

> 作者：Damon Li
> 更新日期：2026年8月23日
> 使用规则：每一行的“可归档事实”只来自链接的一手来源或同行评审论文。推文 URL 被保留以维持发现链路，但不单独支撑技术结论。

## 1. 主题—来源映射

| 入口 | 候选实体 | 已核验的一手来源 | 可归档事实 | 资源状态 |
| :--- | :--- | :--- | :--- | :--- |
| [推文 1][w1] | τ₀-VLA | [论文][p1]、[项目页][p2]、[官方代码][p3]、[模型卡][p4] | 高层以 proposal/world/value/reflection 和自适应 TTC 选择子任务；低层以 40 维统一空间和掩码流匹配执行动作块 | 代码、低层模型与示例数据已公开；高层组件仍逐步发布 |
| [推文 2][w2] | Lumo-2 | [技术报告][p5]、[官方项目页][p6] | 以潜在世界动态 $\phi$ 作为预测性动作生成中介，并以三阶段预对齐提升动作—视觉—语言一致性 | 未发现官方 GitHub、模型权重或完整训练数据 manifest |
| [推文 3][w3] | VLA-Perf | [论文][p7]、[NVlabs 代码][p8] | 用 Roofline 模型估计 VLA 组件计算与跨设备传输上界；包含 Pi0 七类部署分析 | Apache-2.0 代码公开；输出是性能上界而非任务成功率 |
| [推文 4][w4] | Patch Policy | [论文][p9]、[官方代码][p10]、[官方数据][p11] | 冻结 ViT dense patch + block-causal Transformer，在四个仿真和三个真机任务验证 | MIT 代码与四套仿真数据公开；真机演示原始数据未见下载 |
| [推文 5][w5] | 医疗、四足与外骨骼系统 | [磁控介入][p12]、[ANYmal][p13]、[EPIC][p14]、[软体肩部][p15] | 案例展示磁控连续体遥操作、Sim-to-Real 层级运动、TCN 力矩估计和穿戴式气动辅助 | EPIC Code Ocean 与软体肩部 Zenodo 有公开资源；其他系统公开程度不同 |
| [推文 6][w6] | VLA/WAM 综合线索 | [本仓库 2026 VLA/WAM 专题][p16] | 无法从推文本身稳定定位单一新项目；将其作为对既有模型/世界模型专题的发现入口 | 不独立产生技术条目 |
| [推文 7][w7] | Tesla FSD/Optimus | [Tesla AI 页][p17]、[ICCV workshop][p18] | Tesla 官方页面表明其在车辆、机器人等领域开发和部署自主性；工作坊确认相关 keynote 身份 | 没有公开模型、数据、代码、控制接口或可复现实验 |
| [推文 8][w8] | 前沿综合线索 | 本轮可回溯实体见推文 1–7 对应一手来源 | 未在无一手引用的情况下新增独立算法结论 | 保留为 C 级发现入口 |
| [推文 9][w9] | 前沿综合线索 | 本轮可回溯实体见推文 1–7 对应一手来源 | 未在无一手引用的情况下新增独立算法结论 | 保留为 C 级发现入口 |

## 2. 必须拒绝写成“已证实事实”的内容

对 Tesla 相关讨论，以下说法没有从 Tesla AI 页面或 ICCV workshop 页面得到原始技术披露支撑，因此不能在知识库中当作事实：FSD 与 Optimus 采用相同 VLA、某一明确参数规模、AI5 的具体部署、固定的八相机输入、Grok 已集成到 Optimus 控制栈、反思 token、特定训练数据规模、内部世界模型闭环协议。若未来获得 Tesla 官方论文、演讲录像/讲义、监管文件或源码，应以新 A/B 级证据单独更新。[p17] [p18]

Lumo-2 的公式和实验设置已有论文依据，但公开复现链条不完整：不能把公司演示等同于可下载权重或完整数据；也不能将报告中的原始数据集列举等同于完整训练样本、采样配比和许可证均已公开。[p5] [p6]

## 3. 开源资源下载清单

| 资源 | 获取入口 | 用途 | 关键限制 |
| :--- | :--- | :--- | :--- |
| τ₀-VLA | [GitHub][p3]、[模型卡][p4] | 后训练、适配、joint-control serving | EEF serving 未在公开 v1 支持；高层 TTC 不完整开放 |
| Patch Policy 数据 | [Hugging Face][p11] | Push-T、Cube、LIBERO Goal、Block Pushing 仿真复现 | 数据含反序列化文件，仅从可信官方源下载；DINOv3 权重需额外 gated access |
| VLA-Perf | [NVlabs/vla-perf][p8] | 扫描硬件/网络/架构延迟设计空间 | 是分析模型，需用真实 profiler 校准 |
| EPIC | [Code Ocean capsule][p19] | 导出/复现与关节力矩估计相关计算 | 不包含硬件制造、人体实验批准和代谢测试环境 |
| 软体肩部机器人 | [Zenodo 数据与代码][p20] | 2.6 GB 数据代码包 | 下载较大；应阅读 README、核对许可和参与者数据治理 |

## 4. 引用与入口

[w1]: https://mp.weixin.qq.com/s/k9vyCrMuX37rJr56tLBzVw
[w2]: https://mp.weixin.qq.com/s/iCJ8-EVd7TeTDKpUfZP_4Q
[w3]: https://mp.weixin.qq.com/s/LAvUDnRE43l7_e10fuatzQ
[w4]: https://mp.weixin.qq.com/s/Ag5h-0pbTG8UUwsIz4kseA
[w5]: https://mp.weixin.qq.com/s/chMBDQeiSywAn73E3yHwyg
[w6]: https://mp.weixin.qq.com/s/sTiy-qLmNHbNskSuGh2OyQ
[w7]: https://mp.weixin.qq.com/s/Q2uZgbOWf1-Xaey0Z5cf4Q
[w8]: https://mp.weixin.qq.com/s/PCkiMd6H54ITyRghmpPsBg
[w9]: https://mp.weixin.qq.com/s/d4svbd4PZG6EQLqYl1qBfQ
[p1]: https://arxiv.org/html/2608.16885v1 "τ₀-VLA 论文"
[p2]: https://tau0-vla.github.io/ "τ₀-VLA 项目页"
[p3]: https://github.com/sii-research/tau-0-vla "τ₀-VLA 代码"
[p4]: https://huggingface.co/sii-research/tau-0-vla "τ₀-VLA 模型卡"
[p5]: https://arxiv.org/html/2607.11270v1 "Lumo-2 技术报告"
[p6]: https://www.astribot.com/research/Lumo2 "Lumo-2 官方项目页"
[p7]: https://arxiv.org/html/2602.18397v1 "VLA-Perf 论文"
[p8]: https://github.com/NVlabs/vla-perf "VLA-Perf 代码"
[p9]: https://arxiv.org/html/2607.18236v1 "Patch Policy 论文"
[p10]: https://github.com/gaoyuezhou/patch_policy "Patch Policy 代码"
[p11]: https://huggingface.co/datasets/gaoyuezhou/patch-policy-datasets "Patch Policy 数据"
[p12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9254892/ "磁控神经介入论文"
[p13]: https://www.science.org/doi/10.1126/scirobotics.adi7566 "ANYmal Parkour 论文"
[p14]: https://doi.org/10.1126/scirobotics.adi8852 "EPIC 论文"
[p15]: https://doi.org/10.1126/scirobotics.adi2377 "软体肩部机器人论文"
[p16]: ../../course/07-vla-vlm-models/2026-08-verified-embodied-ai-updates/README.md "本仓库世界模型专题"
[p17]: https://www.tesla.com/AI "Tesla AI 官方页"
[p18]: https://wdfm-ad.github.io/iccv25/ "ICCV 2025 WDFM-AD workshop"
[p19]: https://codeocean.com/capsule/5421243/tree/v2 "EPIC Code Ocean"
[p20]: https://doi.org/10.5281/zenodo.11199453 "软体肩部外骨骼 Zenodo"
