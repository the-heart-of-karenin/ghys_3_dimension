# L2 收缩路线：候选完整证明的核验记录

状态：已由 `proof.md` 的完整证明及 `12_final_audit.md` 的最终自检取代。以下保留发现过程；A、B 两段最初只估计稳定方向的 ̅∂，最终证明改为估计完整 ̅∂，因而完全不需要这里最初提出的 ODE/Hartogs 补充步骤。

## 最终修订：完整的 ̅∂ 直接收缩

所选正交度量下 (\|DF^{-1}\|=1/s_k)，因为 (s_k<1<u)。故对任何差向量丛 (W)，若垂直推送范数为 (w(x))，完整的 (W) 值 ((0,1))-形式的推送范数至多 (w(x)/s_k(x))。采用 Hilbert–Schmidt 范数没有维数常数。

分裂丛取 (w=s_1/u)，逐叶联络丛取 (w=1/u)，平方乘实 Jacobian 后分别为

\[
s_1^2\prod_{i<k}s_i^2\le q^{2k},\qquad
\prod_{i<k}s_i^2\le q^{2(k-1)}.
\]

因此光滑推送截面的完整 ̅∂ 在 (L^2) 趋零。截面本身一致收敛，局部全纯仿射平凡化中直接得到极限的分布 ̅∂ 为零。这个论证不求未知 (E^u) 的导数，不需要限制分布到 (E^u)，也不使用分别全纯或横向 ODE 的推论。正文保留稳定/不稳定分量两个更精细的估计作为核查。

## 统一记号

设 rank_C E^u=1，k=n-1。Ghys 给出 E^s 全纯、E^u 连续，所有叶为复子流形；每条不稳定叶有完备不变复仿射结构，稳定 holonomy 相对于这些坐标为射影。

选连续 Hermitian 度量使 E^s,E^u 正交。取迭代 F，使稳定复奇异值

    s_1 >= ... >= s_k >0,  s_1<=q<1,

而不稳定复奇异值 u>1。相对于此连续体积的实 Jacobian 是

    J_F = u^2 (product_i s_i)^2.

不假设体积不变。

## A. 全纯切丛扩张的分裂

令 N=TX/E^s（全纯复直线丛）。连续不变分裂 sigma:N->TX 的像为 E^u。全体分裂构成全纯仿射丛，差向量丛为 Hom(N,E^s)。

取光滑初始分裂 sigma_0，按 F 推送得到 sigma_m。垂直差向量变换 As Z Au^{-1}，故 sigma_m 一致收敛到 sigma。

因为仿射丛与 F 的作用全纯，

    B_m=(bar-partial sigma_m)|bar(E^s)

是 Hom(bar(E^s) tensor N,E^s) 中的光滑张量，并满足

    ||B_{m+1}(Fx)|| <= (s_1/(u s_k)) ||B_m(x)||.

积分换元后，

    (s_1/(u s_k))^2 J_F
      =s_1^2 (product_{i=1}^{k-1}s_i)^2
      <=q^{2k}<1.

因此 B_m 在 L2 中趋零。一致收敛给出 bar-partial sigma 在稳定方向为零（分布意义）。局部稳定全纯坐标中可卷积验证，sigma 的系数在稳定变量中全纯。

将其与不稳定叶本身全纯结合，用 holomorphic-dependence-of-ODE/Hartogs 论证，得到 E^u 为全纯子丛。具体自检：局部 E^s=ker dz，E^u=C(partial_z+a(z,w)partial_w)；a 连续且对 w 全纯。叶图 w=Phi(z,w_0) 已对 z 全纯；ODE 的初值依赖使其对 w_0 全纯，故 Phi 联合全纯，E^u 全纯。

## B. 不变逐叶仿射连接的全纯性（k>=2）

E^u 全纯后，一维叶方向的连接构成全纯仿射丛，其差向量丛为 (E^u)^*。从光滑连接出发推送，因垂直权重 1/u，一致收敛到 Ghys 的连续不变连接。

稳定方向的 bar-partial 张量位于 (bar E^s)^* tensor (E^u)^*，逐点系数不超过 1/(u s_k)。平方乘 Jacobian 为

    (1/(u s_k))^2 J_F
      =(product_{i=1}^{k-1}s_i)^2
      <=q^{2(k-1)}<1.

所以连接在稳定变量全纯。它沿不稳定叶已全纯，两个叶状结构现在均全纯，故 Hartogs 给出全局全纯。

## C. 全纯无穷远截面与不变二形式

在 developing D 的局部有限 projective 坐标 z 中，以 V 属于 E^u、dz(V)=1 规范化。令连接系数为 Gamma，即 nabla_V V=Gamma V。每叶的 D 是完整仿射参数的 Möbius 函数，所以其缺失点 omega 满足

    Gamma=-2/(z-omega),  omega=z+2/Gamma.

因为 Gamma 全纯，omega 是全纯 P1 值函数（Gamma=0 时 omega=infinity），且 omega != D。它沿 E^u 常值，并与 D 同样地在覆盖变换和 F 下 Möbius 等变。

Conf_2(P1) 上有对角 PSL(2,C) 不变的全纯二形式

    omega_0=dz wedge dw/(z-w)^2.

拉回得到 X 上 F 不变的全纯二形式 eta。它只具有 (E^u)^* wedge (E^s)^* 混合分量。于是

    ||eta(Fx)|| <=1/(u s_k) ||eta(x)||,

同一 L2 换元给出 ||eta||_2^2<=q^{2(k-1)}||eta||_2^2，故 eta=0。因 dD 在 E^u 非零、d omega 在 E^u 为零，eta=0 强迫 d omega=0。

所以无穷远点全局一致，monodromy 固定该点，D 值域为 C。已有 03.A、05 和 09 第 3 步即可完成环面拓扑模型、全纯稠密等度连续 C 作用以及复环面均匀化。

## 必须逐项确认的潜在错误点

1. 连续度量与连续体积只用于范数与换元，不对它们求导；换元 Jacobian 的因子确为实平方。
2. 分裂丛的差确为 Hom(N,E^s)，推送含一个 N 的逆导数，不能漏 u^{-1}。
3. 对分裂取 bar-partial 不出现额外非齐次项：投影 TX->N 全纯且分裂为其右逆；F 的仿射作用全纯。
4. 只在已经全纯、因而光滑的 E^s 方向取弱导数，未将分布与未知正则性的 E^u 相乘。
5. 从稳定方向全纯到整个 E^u 全纯的 ODE 初值/Hartogs 论证须完整写出。
6. 叶方向连接的差确为 (E^u)^*，不是其平方或 N。
7. 逐叶连接先有连续不变完整极限，再证明横向全纯；不在构造前假定全局连接。
8. 最后只构造逐叶连接，未误用需要整个 TX 上连接的 Benoist–Labourie 定理。
9. F 对横向 projective 结构的作用以及 omega 的等变性须由 Ghys 构造明确解释。
10. n=2 时第二个 L2 系数不严格，直接使用旧文献 Ghys Theorem A；n>=3 时 k>=2 保证严格。
