# 条件性路线：伪有效典范丛可消除传递性缺口

本节增加条件：K_X 在 Bott–Chern 意义下伪有效，即存在 K_X 上曲率为正闭 (1,1) current 的奇异 Hermitian 度量。原题设尚未推出这个条件；不得据此宣称解决一般情形。

## 1. 在一般紧致复流形上构造不变正曲率

取 Gauduchon 度量 omega_G，满足 dd^c(omega_G^{n-1})=0。令 C 为表示 c_1^{BC}(K_X) 的正闭 (1,1) currents 的集合。它非空，凸，且所有元素的质量

    integral_X T wedge omega_G^{n-1}

相同。质量有限性和弱极限下 Bott–Chern 类的封闭性给出紧性。

f^*K_X 与 K_X 典范同构，故 f^* 保持该集合。对 T_0 属于 C 取 Cesaro 平均

    T_N=(1/N) sum_{j=0}^{N-1}(f^j)^* T_0.

任一弱极限 T 仍属于 C，且 f^*T=T：平均的不变性误差为 ((f^N)^*T_0-T_0)/N，其质量趋零。

这里使用 Bott–Chern 类和 Gauduchon 质量，不是把 Kähler 情形的 de Rham 类质量论证直接搬到非 Kähler 情形。

## 2. 正典范曲率给出有限的满支撑不变测度

取曲率 T 的奇异 Hermitian 度量 h。在局部典范标架 eta=dz_1 wedge ... wedge dz_n 下写

    ||eta||_h^2=exp(-phi),  dd^c phi=T.

phi 可取局部 psh。度量的倒数确定测度

    d mu_h = exp(phi) i^{n^2} eta wedge conjugate(eta).

换标架时表达式不变。psh 权局部有上界，故 mu_h 在紧致 X 上总质量有限；phi 在 Lebesgue 几乎处处有限，故该测度与 Lebesgue 测度等价，尤其满支撑。

f^*T=T 说明 f^*h 与 h 的对数比值为全局 pluriharmonic 分布，因而是常数。于是 f^*mu_h=c mu_h。比较总质量给出 c=1。

因此原 f 保持一个有限满支撑测度。每个开集都回返，所以非游荡集为 X；Anosov 谱分解及连通性给出拓扑传递（进一步混合）。

## 3. 对秩一问题的直接后果

Ghys Theorem B 现在适用，无需假定 Kähler：X 同胚于实环面，f 拓扑共轭于双曲线性环面自同构。原文 §5 随之给出横向仿射、忠实平移 monodromy 及全局闭全纯 theta。

这一步已经严格把“传递性”约化为“典范丛伪有效”，但没有证明后者。

## 4. 使用经典光滑密度定理的进一步结论

这里明确列出所用经典动力系统定理：传递的 C-infinity Anosov 微分同胚如果保持与 Lebesgue 等价的有限测度，则它保持一个严格正的 C-infinity 密度；给定的绝对连续不变概率测度就是这个光滑测度。该结论可由 SRB 条件密度、Livsic–Sinai 同调判据及光滑 Livsic 正则性得到。它是截止日前的经典知识，但本批三篇 PDF 没有系统证明这一正则性定理，正式交付时须明确保留这个外部标准输入。

用该定理，mu_h 为严格正光滑密度，h 也为光滑度量，T 为光滑正 (1,1) 形式。由于 f^*T=T，稳定向量 v 满足

    T_x(v,Jv)=T_{f^k x}(Df^k v,J Df^k v) ->0.

对不稳定向量改用 f^{-k}。正 Hermitian 形式在两个互补子空间上均为零，Cauchy–Schwarz 给出 T=0。

因此 K_X 带 f 不变的单位平坦度量。其单位 monodromy character chi:pi_1(X)->U(1) 满足

    chi o f_*=chi.

已知 pi_1(X)=Z^{2n}，f_* 的谱不交单位圆，故 Z^{2n}/(f_*-I)Z^{2n} 有限。chi 因而有限像，所以 K_X 是挠线丛。

## 5. 路线尚未完成的位置

- 原题设未推出 K_X 伪有效；也不能使用一般非 Kähler 情形下未经证明的“非伪有效就有有理 fibration”替代条件。
- 即使取得 K_X 挠性及拓扑环面，仍未在任意维数非 Kähler 情形证明复环面均匀化。
- 本节不使用 Bogomolov 分解；该分解的 Kähler 前提仍不能删除。
