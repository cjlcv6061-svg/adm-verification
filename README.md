# ADM Verification Repository

Verification scripts for all mathematical claims in:

- **Paper A**: *Holographic Complexity in Cosmology: Positive Results, No-Go Theorems,
  and the Memory Integral Obstruction*
  Zenodo DOI: [10.5281/zenodo.19242134](https://doi.org/10.5281/zenodo.19242134)
- **Letter B**: *Complexity-Inspired Quintessence with Holographic Screening: A Null Result*
- **Paper D**: *Intrinsic Geodesic Bias of the CPL Parameterization on the BAO Fisher Manifold*

All scripts are self-contained and require only standard scientific Python:
`numpy`, `scipy`, `sympy`, `mpmath`.

---

## Scripts

| File | Paper | Claims verified |
|------|-------|----------------|
| `verify_fc_integral.py` | A §3 | `f_C = 0.05696`; shortcut overestimates by factor 1.7; EdS `1/(3π²)`; `f_C/f_S ~ 10¹⁶` |
| `verify_fc_ceiling.py` | A §3 Thm 4 | f_C Ceiling Theorem: 12-model scan + pointwise-H failure demo |
| `verify_wQEC.py` | A §9 Thm 3 | `w_QEC = -0.9662`; Hubble tensions 5.4σ/6.3σ; DESI tensions 3.1σ/3.5σ; `~10⁻¹⁷` suppression |
| `verify_memory_integral.py` | A §5 Thm 2 | Recollapse redshifts κ = 0.5, 1, 2, 5 (Table 1) |
| `verify_v4_scaling.py` | Letter B §4 | V₄ = 3π/55·t⁴ (matter); 8π/105·t⁴ (radiation); w_eff = 0; Ω_cs(CMB) ≫ EDE bound |
| `verify_BBN_alpha_bound.py` | Letter B §2 | Complete JT ODE integration; BBN nonlinear bound; α < 2.33 (exact IC) and α < 6.93 (shortcut IC) |

---

## Key derivations

### Eq. (3) of Paper A — denominator clarification

The z-integral form of f_C has denominator
`[Ω_m(1+z)³ + Ω_Λ] = H(z)²/H₀²`
(the **square** of the dimensionless Hubble rate, not the square root).
This arises because the variable change `dt = −dz/[(1+z)H(z)]` introduces
one factor of H while the integrand `1/H` contributes the other.
Confirmed numerically: gives `f_C = 0.0570`.

### BBN α bound for Letter B §2 — full derivation

**Formula** (exact nonlinear):
```
|(1 + α·Ψ_today)/(1 + α·Ψ_BBN) − 1| < 0.05
```
where `G_eff(z) = G_N/(1 + α·Ψ(z))`.

Ψ is frozen by Hubble friction at high z, so `Ψ_BBN ≈ Ψ_init`.

Two EdS initial conditions:

| Scenario | Ψ_BBN | Ψ_today | α_max | Letter B |
|----------|-------|---------|-------|----------|
| A: exact EdS f_C = 1/(3π²) | 0.034 | Ψ_* (full relax) | **2.33** | ~2 ✓ |
| B: shortcut (2/3)/π² | 0.068 | Ψ_* (full relax) | **6.93** | ~7 ✓ |

Scenario B is looser because larger Ψ_BBN → smaller ΔG_eff → more room for α.

**Key**: w₀ ≈ −1 regardless of α. The bound only constrains the gravitational coupling,
not the equation of state prediction.

### f_C Ceiling Theorem (Paper A §3, Theorem 4)

For any dark energy model with w(z) > −1, `f_C < f_C(ΛCDM)`.
Verified for 12 representative models. Note: pointwise H(z) > H_ΛCDM(z) fails at z > 0.7
for the DESI best-fit, so the theorem requires an **integral** argument, not a pointwise bound.

---

## Running all scripts

```bash
python verify_fc_integral.py
python verify_fc_ceiling.py
python verify_wQEC.py
python verify_memory_integral.py
python verify_v4_scaling.py
python verify_BBN_alpha_bound.py
```

Each script prints verified quantities and exits with a non-zero code if any assertion fails.

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03 | Initial release with Paper A v1 |
| v2 | 2026-04 | Added: f_C Ceiling Theorem (Thm 4), arithmetical hierarchy, V₄ scaling (Letter B), Eq.(3) denominator note, BBN α bound full derivation; removed Paper C dependency |

| `verify_paper_d.py` | Paper D | Christoffel $>0$; $d_{FR}/T_{1D}\approx 2$; $h(z)$ threshold $\Omega_m=1/9$ (exact); Jeffreys scaling $\propto 1/\lambda$ |
