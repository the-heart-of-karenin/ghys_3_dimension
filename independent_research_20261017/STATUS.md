# 研究状态与可审查结果

日期：2026-10-17。

**当前已经写出一般命题的完整独立证明。正文见 `proof.md`，最终逐项自检见 `12_final_audit.md`。以下较早的条件性结果和缺口清单保留为历史快照，不再表示当前证明状态。**

本次闭合使用整体 (L^2) 收缩，不需要预先证明保体积：取迭代后，记稳定复奇异值 (s_1\ge\cdots\ge s_k>0)，(s_1\le q<1)，不稳定复奇异值 (u>1)。实 Jacobian 为 (u^2\prod s_i^2)。分裂丛的完整 ̅∂ 推送系数至多为 (s_1/(u s_k))，逐叶联络的完整 ̅∂ 推送系数至多为 (1/(u s_k))。平方乘 Jacobian 后分别至多为 (q^{2k})、(q^{2(k-1)})。

这依次证明不稳定线丛全纯、规范逐叶仿射联络全纯。遗漏点由联络系数给出全纯函数；拉回对角 Möbius 不变二形式，用同一 (L^2) 估计证明遗漏点为常数。共同遗漏点给出平移 monodromy 与环面拓扑模型，再由全纯不稳定平移作用的紧群闭包得到复环面。复维二使用 Ghys Theorem A，复维至少三时上述第二个估计严格收缩。

完整正文没有附加 Kähler、射影、保体积、稠密轨道或分布全纯的假设，也不需要把拓扑共轭提高到 (C^1)。此处“完整”指推导已闭合并经本工作区自检，不表示外部同行审查。全程未联网或查阅近期证明。

## 较早状态的历史快照

## 研究目标

设 \(X\) 是复维数 \(n\ge 2\) 的紧致连通复流形，\(f:X\to X\) 是全纯 Anosov 微分同胚，且稳定或不稳定复子丛之一的秩为 \(1\)。目标是证明存在

\[
T=\mathbb C^n/\Lambda,\qquad A\Lambda=\Lambda,
\qquad \operatorname{Spec}(A)\cap S^1=\varnothing,
\]

以及双全纯映射 \(h:X\to T\)，满足 \(h\circ f=A\circ h\)。

全过程不联网；没有检索近期证明。只读了用户提供的三篇固定旧期刊版及配套索引，并使用明确标出的经典背景知识。原始材料仍在 `../historical_literature/`，工作记录与它们分开。

## 已完成的论证

1. **复环面有限覆盖可以下降。** 若先证明 X 有复环面有限无分歧覆盖，则秩为 1 的条件迫使所有有限覆盖变换的线性部分为恒等，故 X 本身为复环面。证明见 `02_conditional_lemmas.md` 引理 A。

2. **环面上的平移项可以消去。** 用提升的导数周期性及 Liouville 定理得到仿射表达，再用 I-A 可逆换原点。见同文件引理 B。

3. **不存在正维紧致稳定复子流形；不存在非平凡等变全纯满下沉。** 后者目前只证明到光滑 fibration，不含任意奇异/亚纯 fibration。见同文件引理 C、D。

4. **如果射影 monodromy 有有限轨道，就能去掉传递性前提而取得环面拓扑模型。** 证明通过排除紧致稳定叶，把 developing 像降为 C，再用完备不稳定叶取得全局乘积。见 `03_two_rigidity_reductions.md` A。

5. **如果已有 C^1 infranil 共轭，就能得到全部双全纯结论。** 把复结构搬到模型，用混合性使不变连续张量成为左不变张量；一维复不稳定空间迫使导出 Lie 代数完全收缩，与格上的行列式条件矛盾，因此幂零群交换。见同文件 B。

6. **横向仿射情形的不稳定平移作用等度连续且轨道稠密。** 这是由拓扑共轭与 developing 周期的比较严格推出的附加约化；没有据此断言作用变换全纯。见 `05_affine_case_translation_action.md`。

7. **原题设直接给出两侧叶的多项式体积增长与 Liouville 性。** 每片叶上的有界全纯函数为常数，内蕴 Kobayashi–Royden 伪度量为零。见 `06_leaf_growth_and_liouville.md`。

8. **已构造一个复四维几何反模型，排除“等度连续平移作用自动全纯”的捷径。** 它不是 Anosov 命题的反例，但已经具备忠实平移 monodromy、C^3 稳定型叶、C 横截叶和稠密等度连续作用。见 `07_affine_geometry_countermodel.md`。

## 尚未证明的关键步骤

目前考虑的两条路线是：

\[
\text{原题设}
\xrightarrow{\;?\;}
\text{射影 monodromy 有有限轨道}
\longrightarrow
\text{横向仿射与环面拓扑模型}
\xrightarrow{\;?\;}
C^1\text{ 共轭}
\longrightarrow
\text{目标结论},
\]

或

\[
\text{原题设}
\xrightarrow{\;?\;}
\text{不变仿射联络、两侧光滑及传递性}
\longrightarrow
\text{Benoist–Labourie 的光滑 infranil 模型}
\longrightarrow
\text{目标结论}.
\]

问号处均未补齐。特别是：

- Ghys 的横向射影结构尚不能无条件降为横向仿射。
- 已知一侧分布全纯及另一侧每片叶为 C，不能直接推出另一侧分布全纯。
- 拓扑共轭尚未提高到 C^1；因此不能把搬运复结构的不变张量论证用在仅有的拓扑共轭上。
- 没有构造整个切丛上的不变光滑/全纯仿射联络。

## 已核对的特殊情形与边界

复维二可直接使用 Ghys Theorem A。Cantat 的射影定理以及 Kähler 推广讨论保留各自的几何假设。它们不能覆盖这里的一般非 Kähler 命题。

用户确认的是三维命题最近获得证明；任意维数的扩大目标仍需要本次独立论证。本工作既未证明扩大目标，也不根据三篇旧文献的覆盖范围断言它在数学界的真实解决状态。

## 文件导航

- `README.md`：范围与信息边界。
- `01_known_results_and_gaps.md`：旧文献准确输入与页码。
- `02_conditional_lemmas.md`：有限覆盖下降、线性化与无 fibration 引理。
- `03_two_rigidity_reductions.md`：两个条件性刚性约化。
- `04_rejected_shortcuts.md`：失败路线；含一个明确的局部非全纯补丛模型。
- `05_affine_case_translation_action.md`：等度连续平移作用的约化。
- `06_leaf_growth_and_liouville.md`：从双曲性直接推出的叶性质。
- `07_affine_geometry_countermodel.md`：为什么仿射叶状几何仍不足以完成证明。
- `source_extracts/`：原 PDF 的文本提取，仅为阅读辅助。
- `figures/`：核对关键定理假设所用的原文页面图像。

本记录的作用是准确保存已证明内容和剩余缺口，不是论文，也不是完整证明。
