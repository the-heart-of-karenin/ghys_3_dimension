# 复秩一全纯 Anosov 微分同胚的环面刚性

## 命题

设 \(X\) 是复维数 \(n\ge2\) 的紧致连通复流形，\(f:X\to X\) 是全纯 Anosov 微分同胚，且稳定或不稳定子丛之一的复秩为 \(1\)。则存在复环面 \(T=\mathbb C^n/\Lambda\)、满足 \(A\Lambda=\Lambda\) 且谱不交单位圆的复线性映射 \(A\)，以及双全纯映射 \(h:X\to T\)，使

\[
h\circ f=A\circ h.
\]

证明不预设 Kähler、射影、保体积、传递性或两侧分布全纯。

## 文献输入

主要文献输入为 Ghys《Holomorphic Anosov systems》（Invent. Math. 119, 1995）的下列结果；其中稳定叶状结构全纯的准确表述也由 Cantat（2004）Proposition 1.2 核对：

1. Lemma 2.1：两侧分布对复结构不变，各叶为复子流形；作为通常的 Anosov 叶，它们单连通且微分同胚于欧氏空间。
2. Proposition 2.2：若不稳定复秩为 1，稳定叶状结构为全纯叶状结构，因而 \(E^s\) 是全纯子丛。参见 Cantat《Difféomorphismes holomorphes Anosov》Proposition 1.2 的同一定理表述。
3. Proposition 3.1：一维不稳定叶有连续变化的唯一动力学不变完备复仿射结构，沿每片叶全纯。
4. Proposition 4.1 及 §5 开头：稳定 holonomy 对这些仿射坐标射影，故存在等变的全纯横向 developing submersion \(D:\widetilde X\to\mathbb P^1\)；每条提升的不稳定叶通过 \(D\) 双全纯映到 \(\mathbb P^1\) 减去一个点。
5. 复维二直接使用 Ghys Theorem A。证明后段的环面拓扑刚性与 Franks–Manning 定理，是 Ghys §5 在得到共同无穷远点之后所用的经典拓扑输入。

以下补足一般维数的关键正则性与共同无穷远点；不使用 Theorem B 的传递性假设。

## 1. 一个仿射丛的全纯正则性引理

设 \(M\) 紧致复，\(F\) 全纯自同构，\(\mathcal A\to M\) 为全纯仿射丛，差向量丛为 \(W\)。设 \(\widehat F\) 是覆盖 \(F\) 的全纯仿射丛自同构，在线性差向量丛上的作用为 \(L_x:W_x\to W_{Fx}\)。在截面上记

\[
(\mathcal P s)(Fx)=\widehat F(s(x)).
\]

假设：

- \(\mathcal P\) 在连续截面的统一距离下严格收缩；
- 对 \(W\) 值 \((0,1)\)-形式，诱导推送

\[
(\mathcal P B)_{Fx}
 =L_x\circ B_x\circ\overline{DF_x}^{-1}
\]

在某个 \(L^2\) 范数下严格收缩。

则唯一连续不变截面是全纯截面。

**证明。** 取光滑截面 \(s_0\)，令 \(s_j=\mathcal P^j s_0\)。仿射丛的光滑截面由分片单位构造。第一项假设给出一致极限 \(s_\infty\)。仿射转移函数和 \(\widehat F\) 都全纯，所以 \(\bar\partial s_j\) 是内蕴的 \(W\) 值形式，且

\[
\bar\partial s_j=\mathcal P^j(\bar\partial s_0).
\]

第二项假设使它在 \(L^2\) 中趋零。在局部全纯仿射平凡化中，一致收敛给出分布导数收敛，故 \(\bar\partial s_\infty=0\)。由 \(\bar\partial\) 的 Weyl 引理，\(s_\infty\) 全纯。这里的度量及体积只需连续且处处正，与光滑选择统一等价；不对它们求导。证毕。

## 2. 范数和 Jacobian

把 \(f\) 换成逆映射后，可设 \(\operatorname{rank}_{\mathbb C}E^u=1\)。复维二已由 Ghys Theorem A 解决，故下设

\[
n\ge3,\qquad k=n-1\ge2.
\]

由文献输入，\(E^s\) 为全纯子丛。取连续 Hermitian 度量使 \(E^s,E^u\) 正交，并取充分大的迭代 \(F=f^r\)，使其稳定复奇异值与不稳定复奇异值满足

\[
0<s_k(x)\le\cdots\le s_1(x)\le q<1,
\qquad u(x)\ge u_0>1.
\]

令 \(dV\) 为这个度量的体积。因为 \(DF\) 在两分布上复线性，其相对于 \(dV\) 的**实** Jacobian 为

\[
J_F(x)=u(x)^2\prod_{i=1}^k s_i(x)^2. \tag{1}
\]

不假设 \(dV\) 不变。以下各积分均使用换元公式和 (1)。

## 3. 不稳定子丛为全纯子丛

记全纯直线丛 \(N=T^{1,0}X/E^s\)。全纯正合列

\[
0\longrightarrow E^s\longrightarrow T^{1,0}X
 \xrightarrow{p}N\longrightarrow0
\]

的右分裂 \(\sigma:N\to T^{1,0}X\) 构成全纯仿射丛，其差向量丛为

\[
W=\operatorname{Hom}(N,E^s).
\]

不变连续分裂 \(\sigma_u=(p|_{E^u})^{-1}\) 的像为 \(E^u\)。用 \(E^u\) 给 \(N\) 赋予诱导度量。\(F\) 的分裂推送为

\[
(\mathcal P\sigma)_{Fx}=DF_x\circ\sigma_x\circ (DF_N)_x^{-1}.
\]

在线性差向量上范数至多为 \(s_1/u\le q/u_0<1\)，故第一项收缩成立。

对 \(B\in\overline{T^{1,0}X}^{\,*}\otimes W\)，按其反全纯自变量属于 \(\overline{E^s}\) 或 \(\overline{E^u}\) 分解为 \(B^s,B^u\)。两分量在所选度量中正交，且

\[
\begin{aligned}
\|(\mathcal P B)^s_{Fx}\|&\le\frac{s_1}{u s_k}\|B^s_x\|,\\
\|(\mathcal P B)^u_{Fx}\|&\le\frac{s_1}{u^2}\|B^u_x\|.
\end{aligned}
\]

平方后乘以 (1)，分别得到

\[
\begin{aligned}
\left(\frac{s_1}{u s_k}\right)^2J_F
 &=s_1^2\prod_{i=1}^{k-1}s_i^2\le q^{2k},\\
\left(\frac{s_1}{u^2}\right)^2J_F
 &=\frac{s_1^2}{u^2}\prod_{i=1}^ks_i^2
 \le\frac{q^{2k+2}}{u_0^2}<q^{2k}.
\end{aligned} \tag{2}
\]

因此换元给出

\[
\|\mathcal P B\|_{L^2}^2\le q^{2k}\|B\|_{L^2}^2.
\]

应用第 1 节引理，\(\sigma_u\) 全纯，因而 \(E^u\) 全纯。

这里对 \(B^s,B^u\) 的分解只用于逐点范数估计，不对原先只有连续正则性的 \(E^u\) 求导。趋零的是完整的 \(\bar\partial\sigma_j\)，所以分布极限不涉及与不光滑分布相乘。

## 4. 逐叶仿射连接在整个流形上全纯

现在 \(E^u\) 是全纯一维叶状结构。沿其叶的复连接构成一个全纯仿射直线丛 \(\mathcal C\)。若局部全纯标架为 \(V\)，连接写为

\[
\nabla_VV=\gamma V.
\]

换标架 \(V'=gV\) 时，\(\gamma'=g\gamma+V(g)\)，所以差向量丛为 \((E^u)^*\)，且转移函数全纯。

\(F\) 推送连接，在线性差向量上范数为 \(1/u\)。因此从任意光滑连接迭代所得连续不变极限唯一，并且就是 Ghys 的逐叶仿射连接 \(\nabla\)。

对其 \(\bar\partial\) 张量，稳定、非稳定自变量的推送范数分别至多为

\[
\frac1{u s_k},\qquad \frac1{u^2}.
\]

平方后乘 Jacobian 得

\[
\begin{aligned}
\left(\frac1{u s_k}\right)^2J_F
 &=\prod_{i=1}^{k-1}s_i^2\le q^{2(k-1)}<1,\\
\left(\frac1{u^2}\right)^2J_F
 &=\frac1{u^2}\prod_{i=1}^{k}s_i^2
 \le\frac{q^{2k}}{u_0^2}<1.
\end{aligned} \tag{3}
\]

第 1 节引理再次适用，故 \(\nabla\) 为全纯逐叶连接。每条叶的连接仍是原来的完备仿射连接；这里没有构造或假定整个 \(TX\) 上的仿射连接。

## 5. 所有不稳定叶具有同一个 developing 无穷远点

取 developing map 与 monodromy

\[
D:\widetilde X\to\mathbb P^1,
\qquad \rho:\pi_1(X)\to\operatorname{PSL}(2,\mathbb C).
\]

每条提升不稳定叶 \(L\) 的像为 \(\mathbb P^1\setminus\{\Omega(L)\}\)。这些点定义一个函数 \(\Omega:\widetilde X\to\mathbb P^1\)，沿不稳定叶常值。

它实际上全纯。局部取有限 projective 坐标 \(z=D\)，并令 \(V\in E^u\) 满足 \(dz(V)=1\)，写 \(\nabla_VV=\gamma V\)。沿叶的仿射坐标 \(t\) 是 \(z\) 的 Möbius 函数，极点为 \(\Omega\)，故

\[
\gamma=\frac{t''(z)}{t'(z)}=-\frac2{z-\Omega},
\qquad \Omega=z+\frac2\gamma. \tag{4}
\]

这是一个全纯 \(\mathbb P^1\)-值函数：\(\gamma=0\) 时取无穷远，齐次表达 \([z\gamma+2:\gamma]\) 没有未定点。换 projective 坐标时表达一致，因为它始终是该叶 developing 像的唯一缺失点。并且 \(D\ne\Omega\) 处处成立。

覆盖变换使 \((D,\Omega)\) 同时按 \(\rho\) 等变。\(F\) 保持逐叶仿射结构和横向射影结构，故任一提升 \(\widetilde F\) 满足

\[
D\widetilde F=gD,
\qquad \Omega\widetilde F=g\Omega
\]

其中 \(g\) 是一个 Möbius 变换。

在 \((\mathbb P^1\times\mathbb P^1)\setminus\Delta\) 上，全纯二形式

\[
\Xi=\frac{dz\wedge dw}{(z-w)^2}
\]

对对角 Möbius 作用不变。故 \((D,\Omega)^*\Xi\) 下降为 \(X\) 上的 \(F\)-不变全纯二形式 \(\eta\)。因为 \(dD\) 消灭 \(E^s\)，\(d\Omega\) 消灭 \(E^u\)，\(\eta\) 只有 \((E^u)^*\wedge(E^s)^*\) 分量。因此

\[
\|\eta_{Fx}\|\le\frac1{u s_k}\|\eta_x\|.
\]

用 (3) 的第一个估计换元，

\[
\|\eta\|_{L^2}^2
\le q^{2(k-1)}\|\eta\|_{L^2}^2.
\]

所以 \(\eta=0\)。由于 \(dD|_{E^u}\) 非零，而 \(d\Omega|_{E^u}=0\)，这迫使 \(d\Omega|_{E^s}=0\)，故 \(d\Omega=0\)。\(\widetilde X\) 连通，\(\Omega\) 是常数。

把该常数置于无穷远，得到

\[
D:\widetilde X\longrightarrow\mathbb C,
\]

每一不稳定叶通过 \(D\) 双全纯映满 \(\mathbb C\)。至此共同无穷远点已经直接证明，没有使用传递性。

## 6. 平移 monodromy 与环面拓扑模型

monodromy 固定无穷远，因而位于 \(\operatorname{Aff}(\mathbb C)\)。沿完整不稳定叶移动到指定 \(D\)-值，给出

\[
\widetilde X\cong D^{-1}(0)\times\mathbb C.
\]

具体地，在万有覆盖上，以 \(dD(\widetilde V)=1\) 规范化 \(E^u\) 中的全纯向量场。因为 \(D\) 在每条不稳定叶上是到 \(\mathbb C\) 的双全纯映射，\(\widetilde V\) 的复时间流 \(\widetilde T_t\) 完整。乘积映射为 \((y,t)\mapsto\widetilde T_t(y)\)，逆映射为 \(x\mapsto(\widetilde T_{-D(x)}x,D(x))\)；二者全纯。连通性使 \(D^{-1}(0)\) 连通。\(\ker dD=E^s\)，故每个纤维是单条稳定叶，微分同胚于 \(\mathbb R^{2k}\)，因而可缩。

若非平凡覆盖变换 \(\gamma\) 的仿射像 \(\rho(\gamma)\) 固定某个 \(z\in\mathbb C\)，它就保持稳定叶 \(D^{-1}(z)\)。原稳定叶单连通，所以覆盖投影在每条提升稳定叶上一一，非平凡覆盖变换不能保持它。故 \(\rho\) 忠实，且其每个非平凡元素都是非零平移。

因此 \(\pi_1(X)\cong\mathbb Z^b\)。万有覆盖可缩；比较 \(K(\mathbb Z^b,1)\) 的同调与闭可定向实 \(2n\) 维流形的最高同调，得到 \(b=2n\)。与 Ghys §5 中得到共同无穷远点后的论证相同，环面拓扑刚性及 Franks–Manning 定理给出：\(X\) 同胚于实 \(2n\) 维环面，\(F\) 拓扑共轭于其双曲线性自同构 \(A_0\)。

这些经典拓扑结论只用于本段；未在此前假定 \(X\) 是环面或 \(F\) 传递。

## 7. 拓扑平移闭包实际上由全纯自同构组成

平移 monodromy 使 \(dD\) 下降为无零点闭全纯一形式 \(\theta\)。由全纯子丛 \(E^u\) 和条件 \(\theta(V)=1\) 定义的向量场 \(V\) 全纯，生成完整全纯 \(\mathbb C\) 作用 \(T_t\)。在万有覆盖上，\(D(T_t x)=D(x)+t\)。

由于 \(F\) 保持结构，\(F^*\theta=a\theta\)。记 \(\alpha(x)=\|\theta_x|_{E^u_x}\|>0\)，则 \(|a|^m=u_m(x)\alpha(F^m x)/\alpha(x)\)，其中 \(u_m(x)\ge u_0^m\) 是 \(DF^m|_{E^u}\) 的范数。由紧致性令 \(m\to\infty\)，得到 \(|a|\ge u_0>1\)。

下面核对这个作用的等度连续性。\(A_0\) 的原点是不动点，所以 \(F\) 也有相应不动点。选其提升，并令 \(\widetilde F\) 固定该提升。选拓扑共轭的提升 \(H:\widetilde X\to\mathbb R^{2n}\) 将该点送到原点，再平移 \(D\) 使该点的 \(D\)-值为零，便有

\[
H\widetilde F=A_0H,
\qquad D\widetilde F=aD.
\]

平移周期 \(\rho:\mathbb Z^{2n}\to\mathbb C\) 延拓为实线性映射 \(P:\mathbb R^{2n}\to\mathbb C\)，满足 \(PA_0=aP\)。其秩为 2：否则可取非零常数 \(c\)，使 \(c\rho\) 的像包含于实轴，故实闭一形式 \(\operatorname{Im}(c\theta)\) 的所有周期为零，因而正合。非零复线性一形式的虚部作为实一形式处处非零；但紧致流形上实函数的微分必在极值点为零，矛盾。

\(P\) 消灭 \(A_0\) 的稳定空间，并在实二维不稳定空间 \(U_0\) 上为同构。\(D-PH\) 对覆盖群周期，故有界，又满足

\[
(D-PH)\widetilde F=a(D-PH).
\]

由 \(|a|>1\) 得 \(D=PH\)。共轭把不稳定叶送到线性不稳定叶，故

\[
HT_tH^{-1}(y)=y+(P|_{U_0})^{-1}t. \tag{5}
\]

所以 \(T_t\) 与线性环面平移作用拓扑共轭，因而等度连续。\(U_0\) 在实环面中稠密：其最小有理包络若真包含于 \(\mathbb R^{2n}\)，商环面上的 \(A_0\) 将全部收缩，违反其行列式绝对值为 1。

由 (5)，\(\{T_t\}\) 在 \(\operatorname{Homeo}(X)\) 中的闭包是一个紧致阿贝尔传递群 \(G\cong\mathbb T^{2n}\)。每个极限及其逆都是全纯自同构的一致极限，所以仍全纯。故 \(G\subset\operatorname{Aut}(X)\)。

紧致复流形的自同构群为复 Lie 群，拓扑为紧开拓扑，故 \(G\) 是其紧致 Lie 子群。传递性使其基本实向量场张成每一点的实切空间；相应全纯向量场因此张成复切空间。取其中在一点复线性无关的 \(n\) 个；由于 \(G\) 阿贝尔且传递，它们处处无关并彼此交换。紧致性使这些全纯向量场的复时间流完整，给出 \(\mathbb C^n\) 在 \(X\) 上的传递全纯作用，稳定子为离散子群 \(\Lambda\)。由紧致性，\(\Lambda\) 为满格，因而

\[
X\cong\mathbb C^n/\Lambda
\]

为双全纯同构。

## 8. 原映射的线性化

复环面上的全纯自同构提升为 \(z\mapsto Az+b\)：提升的导数为格周期整矩阵函数，故有界而为常数。自同构性给出 \(A\Lambda=\Lambda\)，Anosov 性给出 \(\operatorname{Spec}(A)\cap S^1=\varnothing\)。

\(I-A\) 可逆，平移原点到 \((I-A)^{-1}b\) 即消去 \(b\)，得到 \(h\circ f=A\circ h\)。若开始时换成了 \(f^{-1}\)，最后用 \(A^{-1}\) 即得到原映射的结论。证毕。

---

**信息范围。** 以上关键 L2 推导为本工作区的独立推导；未联网，也未查阅近期证明。文献输入为用户提供的 1995 年 Ghys 文章（全纯叶状结构的表述以所附 Cantat 2004 Proposition 1.2 交叉核对）及 Ghys 明确使用的经典环面拓扑刚性工具。仿射丛正则性引理、两次正则化、遗漏点二形式及全纯平移闭包的论证均已在上文写出。
