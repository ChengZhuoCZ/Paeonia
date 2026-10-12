# v1.22 explanatory review

Review mode: manual, same agent that developed the patch. No fresh-agent or blind-reader evaluation was performed. Deterministic fixtures check decisions and graph structure; they do not establish natural-language comprehension. The source mathematics was trusted, not independently proved. The supplied TeX was not edited.

## Motivating source read

The v1.21 Introduction already has the correct ingredients: disk localization, atomic data, inverse-cubic energy, cubic cancellation, compatible transport, exact constraints, and equality recovery. The diagnosis is insufficient explanatory hierarchy and connection, not total absence of a proof idea.

The actual source labels in `large_n_proof_explanation.yaml` were checked against the supplied TeX. Its dependency record keeps coarse localization before mesh recovery, and distinguishes the atomic representation from the controlled spectral comparison. This record is planning material, not a prose-comprehension certificate.

## Narrow prose exercise

The following is new editorial test prose in Chinese, not a replacement Introduction or a claim that the original proof has been verified:

圆盘极限提供了展开谱泛函的参照，却不能回答同一个有限 N 下顶点应怎样排列。一个多边形即使已经十分接近圆盘，仍可能有很短的边和不均匀的顶点间距。因此，证明需要一种既保留有限边数的信息、又能与谱展开相接的描述。

关键改写把顶点方向作为原子位置，把归一化外角作为原子质量。这样，凸性给出质量的正性，有限边数成为原子个数的限制，而正多边形对应等质量、等间距的原子配置。真正赋予这个表示力量的是配套的原子不等式：它给出一个非负缺陷，且零缺陷恰好刻画该规则配置。此时得到的是一个可以精确识别离散对称性的量；它还不等于原来的谱差。

连接二者要经过谱展开。在线性化层面，从转角数据恢复径向位移需要两次积分；再代入圆盘上具有一阶频率权重的谱 Hessian，便得到逆三次幂的主权重。这解释了原子能量的选择。精确的 Bessel 系数比较负责保住二次项的正性，非线性重构和更高阶谱项则是尚未处理的误差。

不能先假设顶点已经均匀，再用这一假设解释全局极小值。正文先用粗估计和第一次三次项比较改善缺陷，使微观刚性能够推出质量与间距接近规则值。取得这些新信息后，第二次比较才利用完整循环表达式中的抵消。两次比较的目的不同：前一次取得可用的离散几何，后一次保住谱差的符号。

即使一个绝对误差随 N 趋于零，它也可能比某个非正多边形的缺陷更大。要排除任意接近正多边形的竞争者，误差必须受“趋于零的系数乘以同一个缺陷”控制。相容的端点比较和精确约束坐标把这种相对估计延伸到所需局部类的所有正缺陷；于是谱差在正缺陷处严格为正。极小性迫使缺陷为零，再由转角重构和面积归一化恢复正多边形。

## Same-agent reader-side answers

| Question | Answer available in the test prose |
|---|---|
| What information does the disk limit lose? | The arrangement at fixed finite N, including irregular gaps and short edges. |
| What does the new measure record? | Vertex directions and normalized turning; positivity and number of atoms express geometric restrictions. |
| What does the reformulation enable? | A nonnegative discrete defect whose zero set selects the regular configuration. |
| Is the spectral functional exactly the atomic energy? | No. The prose explicitly separates the auxiliary defect, principal Fourier motivation, exact coefficient comparison, and nonlinear costs. |
| Why inverse-cubic weights? | Two integrations and the order-one Hessian combine at principal order. |
| Why two rounds of cubic analysis? | One obtains a near-regular mesh; the next uses that geometry to compare relatively. |
| Why is an additive small error insufficient? | A competitor's defect can be smaller; a coefficient multiplying that defect preserves the sign. |
| How does the original equality case return? | The local strict comparison applies to localized minimizers; atomic zero defect, reconstruction, and area normalization identify the polygon. |

## Ablation observations

- Remove the second paragraph's gain: the measure becomes a list of symbols, with no reason to choose it.
- Remove the sentence separating the atomic defect from the spectral difference: the reader may infer an unjustified exact reduction.
- Remove the fourth paragraph: the route can appear to assume mesh regularity before obtaining it.
- Replace relative control in the last paragraph by an additive error: the stated argument no longer explains exact equality for arbitrarily tiny positive defects.

The exercise tests selected causal links, not the entire theorem or a finished English Introduction. Detailed construction of the material coordinate remains a later explanatory obligation in a full outline; this narrow sample only states its role.

## Cross-problem control

The rules allow a short direct proof with no central reformulation to remain short. The critical-set held-out paper uses effective tangent uniqueness where the harmonic-map setting cannot assume it. Accordingly no theorem-specific obstruction, Fourier exponent, number of stages, or outline subsection pattern becomes a universal rule.
