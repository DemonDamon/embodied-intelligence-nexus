# 2026 年 7—8 月产业平台与赛事补充：AGIBOT、Galbot、NVIDIA 生态与 WHRG

> 作者：Damon Li | 更新日期：2026年8月22日
> 证据状态：官方披露（B 级）/ 媒体报道（C 级）

## 1. 结论与证据等级

本文件补充归档 2026 年 7—8 月产业端的新发布与新动态，包括 AGIBOT 在 WAIC 2026 的多平台发布、Galbot ET1 双足人形发布、NVIDIA GR00T N1.7 / Cosmos 3 / Isaac Lab 更新，以及第二届世界人形机器人运动会（WHRG）场景赛。这些信息多为**官方披露或媒体报道**，不等于同行评审结论。[1] [2] [3] [4] [5]

| 条目 | 类型 | 证据等级 | 核心内容 |
| :--- | :--- | :--- | :--- |
| AGIBOT WAIC 2026 发布 | 产品发布 | B | A3 Ultra、X2 Edu、G2 Max、OmniHand 3 Ultra-M |
| Galbot ET1 | 产品发布 | B/C | 双足人形 + 银河星脑 + AstraBrain-Agent |
| NVIDIA GR00T N1.7 GA | 平台更新 | B | 新 VLM backbone + 端到端开发平台 |
| NVIDIA Cosmos 3 | 基础模型 | B | 物理 AI 世界基础模型，开源 |
| NVIDIA Isaac Lab v2.3.2 | 仿真平台 | B | 触觉传感器、多旋翼、OpenArm 环境 |
| WHRG 2026 场景赛 | 赛事 | B/C | 酒店整理、图书上架、灵巧手微操作 |

## 2. 问题设定、符号与假设

本文件不涉及算法推导，聚焦产业披露信息的核验与记录。核心假设是公司官方页面和赛事官方报道可作为 B/C 级证据，但量化指标需要回到一手技术文档确认。

## 3. 方法与完整推导

本文件为产业信息归档，不涉及完整算法推导。以下为 NVIDIA GR00T/Cosmos 3 统一框架的概念性描述：

NVIDIA 的 GR00T + Cosmos 3 组合将物理推理、世界生成和动作生成统一到一个框架中。GR00T 作为机器人策略 $\pi_\theta(a_t \mid o_t, \ell)$ 的开发平台，Cosmos 3 作为物理世界基础模型提供 $\hat{o}_{t+1} = W_\phi(o_t, a_t)$ 的世界预测能力：

$$
\hat{o}_{t+1} = W_\phi(o_t, a_t), \qquad a_t = \pi_\theta(o_t, \ell, \hat{o}_{t+1})
$$

其中 $W_\phi$ 是 Cosmos 3 世界模型，$\pi_\theta$ 是 GR00T 策略。两者在仿真环境搭建、teleoperation 数据采集、post-training 和真实部署的端到端流程中协同工作。

## 4. 训练和推理算法

不适用。

## 5. 实验设计、基线与结果

### 5.1 AGIBOT WAIC 2026 发布

| 产品 | 定位 | 关键参数 | 一手来源确认状态 |
| :--- | :--- | :--- | :--- |
| A3 Ultra | 商业服务与长时间运行 | 未完整披露 | 官方发布页可访问 [1] |
| G2 Max | 重载工业任务 | 未完整披露 | 官方发布页可访问 |
| OmniHand 3 Ultra-M | 直接驱动灵巧操作 | 未完整披露 | 官方发布页可访问 |
| X2 Edu | 教学、科研与竞赛 | 未完整披露 | 官方发布页可访问 |

### 5.2 Galbot ET1

Galbot ET1 在 WRC 2026 发布，搭载自研具身大模型"银河星脑"和物理世界原生智能体 AstraBrain-Agent。报道提及自主打网球和通用"小脑"运动控制能力。[2]

### 5.3 NVIDIA 生态更新

| 组件 | 版本/状态 | 核心更新 | 来源 |
| :--- | :--- | :--- | :--- |
| GR00T | N1.7 GA | 新 VLM backbone（Cosmos-Reason2-2B / Qwen3-VL）；端到端开发平台 | [GitHub](https://github.com/nvidia/isaac-gr00t) [3] |
| Cosmos | 3 | 物理 AI 世界基础模型；统一 physical reasoning、world generation、action generation | [NVIDIA 博客](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3) [4] |
| Isaac Lab | v2.3.2 | 多旋翼/推进器支持；visual-based tactile sensor；OpenArm 环境；Mimic pipeline 改进 | [GitHub](https://github.com/isaac-sim/IsaacLab) [5] |

### 5.4 WHRG 2026 场景赛

第二届世界人形机器人运动会扩展到真实场景：酒店整理、图书馆图书上架、家庭收纳、洗衣晾衣、取快递。灵巧手类别包含捡豆子、拧螺丝等微操作。评分体系中自主运行权重高于遥操作。[6]

## 6. 失败模式、局限性与复现条件

1. **AGIBOT 产品技术细节**：官方发布页可访问，但关键参数（DoF、负载、控制频率、模型/算法）未完整披露。
2. **Galbot ET1**：报道来自新华网，属于 C 级来源；"银河星脑"和"AstraBrain-Agent"的技术细节、论文或开源代码未确认。
3. **NVIDIA GR00T/Cosmos 量化指标**：官方博客和 GitHub 可访问，但 VLA 预训练数据规模、训练成本和真机评测的完整统计需以官方 release notes 为准。
4. **WHRG 赛事结果**：媒体报道为 C 级来源；完整赛果和评测协议需以赛事官方页面为准。
5. **产业发布的时效性**：产品发布不代表已量产或可购买；技术能力展示不等同于产品级可靠性。

## 7. 代码、模型、数据与许可证

| 资源 | 状态 | 链接 |
| :--- | :--- | :--- |
| AGIBOT 产品页 | 官方可访问 | [agibot.com](https://www.agibot.com/article/231/detail/85.html) |
| Galbot ET1 报道 | 新华网报道 | [新华网](https://www.xinhuanet.com/digital/20260821/e172222483dc4d75a357145caa74d9d0/c.html) |
| NVIDIA GR00T | GitHub 公开 | [github.com/nvidia/isaac-gr00t](https://github.com/nvidia/isaac-gr00t) |
| NVIDIA Cosmos 3 | 官方博客 | [developer.nvidia.com](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3) |
| Isaac Lab | GitHub 公开 | [github.com/isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) |
| WHRG 报道 | 人民日报/Global Times | [peoplesdaily](https://peoplesdaily.pdnews.cn/china/er/30052962261) |

## 8. 参考资料

[1]: https://www.agibot.com/article/231/detail/85.html "AGIBOT WAIC 2026 新品发布"
[2]: https://www.xinhuanet.com/digital/20260821/e172222483dc4d75a357145caa74d9d0/c.html "银河通用 Galbot ET1 发布"
[3]: https://github.com/nvidia/isaac-gr00t "NVIDIA Isaac GR00T"
[4]: https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3 "NVIDIA Cosmos 3"
[5]: https://github.com/isaac-sim/IsaacLab "NVIDIA Isaac Lab"
[6]: https://peoplesdaily.pdnews.cn/china/er/30052962261 "第二届世界人形机器人运动会"
