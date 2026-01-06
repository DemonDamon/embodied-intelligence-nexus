# 2025年世界模型最新研究项目清单

**作者**: Damon Li  
**日期**: 2026年1月6日  
**来源**: https://github.com/Li-Zn-H/AwesomeWorldModels

本文档整理了2025年1月至今在世界模型（World Models）领域的最新研究成果，涵盖机器人操作、自动驾驶、导航等多个应用领域。

---

## 分类说明

- 🤖 **机器人操作** (Robotic Manipulation)
- 🚗 **自动驾驶** (Autonomous Driving)
- 🧭 **导航** (Navigation)
- 🎬 **视频生成** (Video Generation)

---

## 一、决策耦合/序列/全局潜在向量 (Decision-Coupled / Sequential / Global Latent Vector)

### 2025年研究项目

#### 1. DisWM: Disentangled World Models
**会议**: ICCV 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2503.08751  
**项目页**: https://qiwang067.github.io/diswm  
**代码**: https://github.com/qiwang067/DisWM  
**数据集**: https://huggingface.co/datasets/MrSC320/DisWM-Pretrain-Datasets/tree/main

**核心贡献**: 学习从干扰视频中迁移语义知识用于强化学习

---

#### 2. FOUNDER: Grounding Foundation Models in World Models
**会议**: ICML 2025  
**领域**: 🤖 机器人操作  
**论文**: https://openreview.net/forum?id=UTT5OTyIWm  
**项目页**: https://sites.google.com/view/founder-rl

**核心贡献**: 将基础模型植根于世界模型中，实现开放式具身决策

---

#### 3. SENSEI: Semantic Exploration Guided by Foundation Models
**会议**: ICML 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2503.01584  
**项目页**: https://sites.google.com/view/sensei-paper  
**代码**: https://github.com/martius-lab/sensei

**核心贡献**: 由基础模型引导的语义探索，学习通用世界模型

---

#### 4. SR-AIF: Solving Sparse-Reward Robotic Tasks
**会议**: ICRA 2025  
**领域**: 🤖 机器人操作  
**论文**: https://ieeexplore.ieee.org/abstract/document/11127713  
**代码**: https://github.com/NACLab/self-revising-active-inference

**核心贡献**: 使用主动推理和世界模型从像素解决稀疏奖励机器人任务

---

#### 5. LUMOS: Language-Conditioned Imitation Learning with World Models
**会议**: ICRA 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2503.10370  
**项目页**: http://lumos.cs.uni-freiburg.de/  
**代码**: https://github.com/nematoli/lumos

**核心贡献**: 语言条件下的模仿学习与世界模型结合

---

#### 6. WMP: World Model-Based Perception for Visual Legged Locomotion
**会议**: ICRA 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2409.16784  
**项目页**: https://wmp-loco.github.io/  
**代码**: https://github.com/bytedance/WMP

**核心贡献**: 基于世界模型的视觉腿式运动感知

---

#### 7. X-MOBILITY: End-to-end Generalizable Navigation
**会议**: ICRA 2025  
**领域**: 🧭 导航  
**论文**: https://arxiv.org/abs/2410.17491  
**项目页**: https://nvlabs.github.io/X-MOBILITY/  
**代码**: https://github.com/NVlabs/X-Mobility

**核心贡献**: 通过世界建模实现端到端泛化导航

---

#### 8. AdaWM: Adaptive World Model based Planning
**会议**: ICLR 2025  
**领域**: 🚗 自动驾驶  
**论文**: https://arxiv.org/abs/2501.13072

**核心贡献**: 自适应世界模型规划用于自动驾驶

---

#### 9. DreamerV3: Mastering Diverse Control Tasks
**会议**: Nature 2025  
**领域**: 🤖 机器人操作  
**论文**: https://www.nature.com/articles/s41586-025-08744-2  
**项目页**: https://danijar.com/project/dreamerv3/  
**代码**: https://github.com/danijar/dreamerv3

**核心贡献**: 通过世界模型掌握多样化控制任务（Nature顶刊发表）

---

#### 10. GLAM: Global-Local Variation Awareness in Mamba-based World Model
**会议**: AAAI 2025  
**领域**: 🤖 机器人操作  
**论文**: https://ojs.aaai.org/index.php/AAAI/article/view/33880  
**代码**: https://github.com/GLAM2025/glam

**核心贡献**: 基于Mamba的世界模型中的全局-局部变化感知

---

#### 11. WMR: Learning Humanoid Locomotion with World Model Reconstruction
**期刊**: arXiv 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2502.16230

**核心贡献**: 通过世界模型重建学习人形机器人运动

---

#### 12. VL-SAFE: Vision-Language Guided Safety-Aware RL
**期刊**: arXiv 2025  
**领域**: 🚗 自动驾驶  
**论文**: https://arxiv.org/abs/2505.16377  
**项目页**: https://ys-qu.github.io/vlsafe-website/  
**代码**: https://github.com/ys-qu/vl-safe/tree/main

**核心贡献**: 视觉-语言引导的安全感知强化学习与世界模型

---

#### 13. CALL: Ego-centric Learning of Communicative World Models
**期刊**: arXiv 2025  
**领域**: 🚗 自动驾驶  
**论文**: https://arxiv.org/abs/2506.08149

**核心贡献**: 自我中心学习通信世界模型用于自动驾驶

---

#### 14. Latent Policy Steering with Embodiment-Agnostic Pretrained World Models
**期刊**: arXiv 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2507.13340

**核心贡献**: 使用与具身无关的预训练世界模型进行潜在策略引导

---

#### 15. ReDRAW: Adapting World Models with Latent-State Dynamics Residuals
**期刊**: arXiv 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2504.02252  
**项目页**: https://redraw.jblanier.net/

**核心贡献**: 使用潜在状态动力学残差适应世界模型

---

#### 16. OSVI-WM: One-Shot Visual Imitation
**期刊**: arXiv 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2505.20425

**核心贡献**: 使用世界模型引导轨迹生成的一次性视觉模仿

---

#### 17. Robotic World Model: A Neural Network Simulator
**期刊**: arXiv 2025  
**领域**: 🤖 机器人操作  
**论文**: https://arxiv.org/abs/2501.10100

**核心贡献**: 用于机器人鲁棒策略优化的神经网络模拟器

---

## 待深入调研的重点项目

基于影响力和创新性，以下项目值得深入调研：

### 高优先级（顶会/顶刊）

1. **DreamerV3** (Nature 2025) - 世界模型领域的里程碑工作
2. **FOUNDER** (ICML 2025) - 基础模型与世界模型结合
3. **SENSEI** (ICML 2025) - 语义探索与基础模型
4. **AdaWM** (ICLR 2025) - 自适应世界模型规划
5. **DisWM** (ICCV 2025) - 解耦世界模型

### 中优先级（ICRA/AAAI）

6. **LUMOS** (ICRA 2025) - 语言条件模仿学习
7. **WMP** (ICRA 2025) - 视觉腿式运动
8. **X-MOBILITY** (ICRA 2025) - 端到端导航
9. **GLAM** (AAAI 2025) - Mamba架构创新

### 特别关注（arXiv前沿）

10. **VL-SAFE** - 视觉-语言安全强化学习
11. **WMR** - 人形机器人运动学习
12. **ReDRAW** - 世界模型适应

---

## 下一步工作

1. 深入调研高优先级项目的技术细节
2. 分析核心算法和架构创新
3. 提取关键技术图表和公式
4. 总结技术趋势和未来方向
