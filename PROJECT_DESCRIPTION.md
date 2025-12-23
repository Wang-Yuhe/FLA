# Assemblies 项目说明

## 项目概述

这是一个**大脑计算模型（Assembly Model）**的模拟项目，用于研究神经元集合（assemblies）如何在大脑中工作，以及如何用这种机制来实现认知功能，特别是**语言学习**。

## 核心概念：Assembly（神经元集合）

### 什么是 Assembly？

Assembly 是大脑中一组相互连接的神经元，它们作为一个整体来代表某个概念、记忆或模式。关键特性：

1. **稀疏激活**：在大量神经元（n）中，只有少数神经元（k）同时激活
2. **可塑性**：当神经元一起激活时，它们之间的连接会增强（Hebbian 学习）
3. **稳定性**：经过训练后，assembly 可以稳定地代表某个概念
4. **可组合性**：多个 assembly 可以组合、关联、合并

### Assembly 的核心操作

1. **投影（Projection）**：将一个区域的 assembly 投射到另一个区域
2. **模式完成（Pattern Completion）**：从部分激活恢复完整的 assembly
3. **关联（Association）**：将两个独立的 assembly 关联到第三个区域
4. **合并（Merge）**：将两个 assembly 合并到第三个区域

## 项目结构

### 1. 核心模块

#### `brain.py` - 大脑模型核心
- **`Area` 类**：代表大脑的一个区域
  - `n`: 区域中的神经元总数
  - `k`: 每次激活的神经元数量
  - `w`: 曾经激活过的神经元总数（支持集大小）
  - `winners`: 当前激活的神经元列表
  - `beta`: 学习率（可塑性参数）

- **`Brain` 类**：整个大脑模型
  - 管理多个区域（`area_by_name`）
  - 管理连接组（`connectomes`）：区域之间的连接
  - 实现投影操作（`project` 方法）

#### `simulations.py` - 基础模拟实验
包含多种模拟实验：
- **投影模拟**：测试 assembly 的稳定性和收敛性
- **模式完成模拟**：测试从部分信息恢复完整模式的能力
- **关联模拟**：测试两个 assembly 关联学习的能力
- **合并模拟**：测试两个 assembly 合并的能力

### 2. 高级应用模块

#### `learner.py` - 语言学习模型
实现了基于 assembly 的语言学习系统：

- **`LearnBrain` 类**：扩展了 `Brain`，专门用于语言学习
  - **区域设计**：
    - `PHON`：语音区域（存储单词的语音表示）
    - `VISUAL`：视觉区域（存储名词的视觉表示）
    - `MOTOR`：运动区域（存储动词的运动表示）
    - `NOUN` / `VERB`：词汇区域（存储名词和动词的语义）

  - **学习过程**：
    - `train_simple()`：简单训练，学习单词和语义
    - `test_verb()` / `test_word()`：测试是否能识别单词
    - `parse()`：解析句子，学习语法结构

- **语言学习原理**：
  1. 单词学习：将语音、视觉/运动信息关联到词汇区域
  2. 语法学习：学习词序和语法规则
  3. 语义理解：通过 assembly 的关联实现语义理解

#### `parser.py` / `recursive_parser.py` - 语法解析器
实现基于 assembly 的语法解析，可以：
- 解析句子结构
- 学习语法规则
- 处理递归结构

### 3. 其他模块

- **`turing_sim.py`**：图灵机相关的模拟
- **`overlap_sim.py`**：研究 assembly 重叠度保持的模拟
- **`brain_util.py`**：工具函数（计算重叠度等）

## 项目能做什么？

### 1. 基础认知功能模拟

**投影（Projection）**
```python
# 模拟：刺激 → 区域A → 区域A（自循环）
# 结果：assembly 逐渐稳定，支持集大小收敛
w = simulations.project_sim(n=100000, k=317, p=0.001, beta=0.05, t=25)
```

**模式完成（Pattern Completion）**
```python
# 模拟：只激活50%的神经元，看能否恢复完整assembly
# 结果：重叠度 >= 300，说明模式完成成功
(_, winners) = simulations.pattern_com(..., alpha=0.5)
```

**关联（Association）**
```python
# 模拟：两个独立assembly（A和B）关联到第三个区域（C）
# 结果：A→C 和 B→C 有高重叠，说明关联成功
(_, winners) = simulations.association_sim(...)
```

**合并（Merge）**
```python
# 模拟：两个assembly合并到第三个区域
# 结果：合并后的assembly大小接近两者之和
(w_a, w_b, w_c) = simulations.merge_sim(...)
```

### 2. 语言学习

```python
# 创建学习大脑
brain = learner.LearnBrain(0.05, LEX_k=100)

# 训练：学习单词和语义
brain.train_simple(30)

# 测试：能否识别动词"RUN"
brain.test_verb("RUN")
```

### 3. 语法解析

可以学习并解析简单的语法结构，如：
- 名词-动词顺序（NV）
- 动词-名词顺序（VN）
- 疑问句结构

## 科学意义

这个项目展示了：

1. **计算神经科学**：如何用简单的神经元机制实现复杂的认知功能
2. **语言学习**：如何从感知信息（视觉、听觉）学习语言
3. **记忆机制**：assembly 如何作为记忆和概念的基础
4. **可组合性**：简单的 assembly 操作如何组合成复杂的行为

## 技术特点

1. **高效模拟**：使用稀疏采样技巧，不需要模拟所有神经元
2. **可配置**：可以调整各种参数（n, k, p, beta）
3. **可扩展**：可以添加新的区域和操作

## 运行项目

### 快速开始

```bash
# 运行测试
python simulations_test.py

# 运行示例
python run_examples.py
```

### 主要实验

1. **基础模拟**：`simulations.py` 中的各种函数
2. **语言学习**：`learner.py` 中的 `LearnBrain` 类
3. **语法解析**：`parser.py` 中的解析功能

## 相关论文

这个项目基于以下研究：
- Assembly calculus（神经元集合演算）
- 稀疏连接和可塑性的神经网络模型
- 基于 assembly 的语言学习理论

## 总结

这个项目是一个**计算神经科学**和**认知科学**的研究工具，展示了：
- 如何用简单的神经元机制模拟复杂的认知功能
- 如何实现语言学习和理解
- Assembly 作为大脑计算基本单元的作用

它不仅是代码实现，更是一个**理论模型**，帮助我们理解大脑如何工作。
