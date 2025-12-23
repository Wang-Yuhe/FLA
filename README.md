# 实验记录

1. 检查项目依赖，检查后发现需要：

   ```sh
   numpy>=1.19.0
   scipy>=1.5.0
   matplotlib>=3.3.0
   pptree>=3.1.0
   ```

2. 运行`simulations_test`，运行后发现出错（属性名称错误），修改后运行，测试通过

3. 后来发现各测试文件中都有这个问题（turing_sim、overlap_sim、tests.py），修改完成。

4. 运行`parser.py`可以得到结果：

   ```sh
   ...
   defaultdict(<class 'set'>, {'SUBJ': {'LEX'}, 'VERB': {'OBJ', 'LEX', 'SUBJ'}, 'OBJ': {'LEX'}})
   Got dependencies: 
   [['chase', 'mice', 'OBJ'], ['chase', 'cats', 'SUBJ']]
   ```

   含义为：句式——主谓宾，依赖关系——mice是chase的主语；cats是chase的宾语。

5. 替换`brain.py`中的制表符为2个空格，其他文件中的制表符为4个空格。

6. 为`overlap_sim.py`中的`print`增加括号。

7. 将所有python文件中的`xrange`替换为`range`。



# 各文件作用一览（仓库根目录）

- README.md：项目概览、运行说明入口。
- PROJECT_DESCRIPTION.md：更详细的项目背景与实验设计说明。
- requirements.txt：Python 依赖列表。
- tests.py：简单测试入口，验证主要功能是否正常。
- simulations.py：核心仿真实验集合，包含多种组装体/网络模拟逻辑。
- simulations_test.py：针对 simulations.py 的测试或示例运行。
- overlap_sim.py：计算装配/激活重叠度的模拟脚本。
- project.py：一个小型示例（装配演化），展示 winners/support 变化的过程。
- parser.py：基于组装体的句法解析器（英文/俄文），提供 parse 入口和读出依存关系。
- recursive_parser.py：递归版解析器，实现更复杂句法（如从句）解析。
- learner.py：词汇/语义/简单句法的学习与测试大脑，实现训练、测试、读出等逻辑。
- word_order_int.py：词序/语序的组装体实验（整数/索引形式）。
- turing_sim.py：图灵机相关的组装体模拟示例。
- brain.py：核心神经区/连接体的数据结构与投射、可塑性机制实现。
- brain_util.py：辅助函数（如重叠度计算、工具方法）。
- cpp/：

  - brain.cc/.h、brain_util.h、brain_test.cc：C++ 版本的核心实现与测试。

  - BUILD、WORKSPACE：Bazel 构建配置。

  - matlab/：Matlab 版的组装体投射/合并等函数（assembly_sim.m 等）。

  - recursive_parser.py：递归解析器（同上，支持更复杂结构）。
- LICENSE：许可证。
