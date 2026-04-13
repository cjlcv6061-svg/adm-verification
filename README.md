# ADM Paper Verification Suite

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Companion code for:** "Holographic Complexity in Cosmology: Positive Results, No-Go Theorems, and the Memory Integral Obstruction" (Revised April 2026)

This repository contains the complete symbolic and numerical verification of every mathematical claim in the paper. All algebraic identities are verified by [SymPy](https://www.sympy.org/); all numerical results are computed by [NumPy](https://numpy.org/) and [SciPy](https://scipy.org/).

## Quick Start

```bash
git clone https://github.com/cjlcv6061-svg/adm-verification.git
cd adm-verification
pip install -r requirements.txt
python adm_verification.py
```

Expected output:
```
OVERALL: ALL VERIFICATIONS PASSED ✓
```

## What is Verified

| Paper Section | Claim | Verification Method | 
|---|---|---|
| §3 | $f_C = t_0 H_0/\pi^2 \approx 0.100$ | SymPy symbolic simplification |
| §3 | $\dot{f} = 0$ in Einstein–de Sitter | SymPy substitution |
| §3 | $\dot{f}/H \approx 0.057$ in ΛCDM | SymPy + numerical evaluation |
| §3.3 | $f_C/f_S \sim 10^{16}$ (Capacity Dichotomy) | Numerical evaluation |
| §3.3 | $f_C \approx 0.057$ from exact ΛCDM integral | SciPy numerical integration |
| §4 | $\rho_{\rm DE} < 0$ for $S = (A/4G)(1+\lambda f)$ | SymPy factorisation |
| §4 | $\Omega_{\rm DE} \approx -0.128$, $H_0 \approx 29$ km/s/Mpc | Numerical evaluation |
| §5 | Product rule: $d/dt[(1-\lambda f)H^2]$ has $-\lambda\dot{f}H^2$ | SymPy `diff` + `expand` |
| §5 | Raychaudhuri RHS has $+\lambda\dot{f}H^2$ | SymPy verification |
| §5 | Residual = $+2\lambda\dot{f}H^2 \neq 0$ | SymPy `simplify` |
| §5 | $[I] = T^{-2} = [H^2]$ (dimensional consistency) | Analytical |
| §5 | Recollapse at $z \approx 1.75$ for $\kappa = 1$ | SciPy ODE integration |
| §5 | No positive $\kappa$ yields $H(0) = H_0$ | Exhaustive numerical scan |
| §5.5 | $f$ depends on both $A$ and $t$ (not $S(A)$) | SymPy partial derivatives |
| §6 | $f_C(\text{EdS}) = 1/(3\pi^2) \approx 0.034$ | Numerical evaluation |
| §8 | $H = H_\infty$ in de Sitter | SymPy symbolic differentiation |
| §8 | Conformal time $\eta_\infty = 1/H_\infty$ is finite | SymPy definite integral |
| §8 | $L_{\max} \approx 8.2 \times 10^{60}$ | Numerical evaluation |
| §9 | $w_{\rm QEC} = -1 + 1/(3\pi^2) \approx -0.966$ | Numerical evaluation |
| §9 | $H_0^{\rm QEC} \approx 66.4$ km/s/Mpc (6.3$\sigma$ tension) | CMB calibration |
| §9 | Dynamic/static suppression ratio $\sim 10^{-17}$ | Numerical evaluation |
| Supp. | $\rho_{\rm DE} > 0$ for $S = (A/4G)(1-\lambda f)$ | SymPy sign analysis |
| Supp. | $H_0 \approx 70$ km/s/Mpc with corrected sign | Numerical evaluation |

## Running Individual Sections

```bash
python adm_verification.py --section 3    # Complexity filling fraction
python adm_verification.py --section 3.3  # Holographic Capacity Dichotomy
python adm_verification.py --section 4    # No-Go Theorem I
python adm_verification.py --section 5    # Memory Integral Catastrophe
python adm_verification.py --section 5.5  # Distinction from Barrow/Tsallis
python adm_verification.py --section 6    # Class C/U Partition
python adm_verification.py --section 8    # de Sitter Exclusion Theorem
python adm_verification.py --section 9    # QEC No-Go Theorem (Theorem 3)
python adm_verification.py --section S    # Corrected sign verification
```

## Requirements

```
sympy>=1.12
numpy>=1.24
scipy>=1.11
```

## Repository Structure

```
adm-verification/
├── README.md                              # This file
├── requirements.txt                       # Python dependencies
├── adm_verification.py                    # Complete verification suite
├── paper/
│   ├── ADM_paper_v4.tex                   # v1 LaTeX source (preserved)
│   ├── ADM_paper_v4.pdf                   # v1 compiled PDF (preserved)
│   ├── Holographic_Complexity_v3.tex      # v3 LaTeX source (current)
│   ├── references.bib                     # BibTeX database (new)
│   └── Holographic_Complexity_v3.pdf      # v3 compiled PDF (new)
└── LICENSE                                # MIT License
```

## Citation

If you use this verification suite, please cite:

```bibtex
@article{Cheng2026,
  title   = {Holographic Complexity in Cosmology: Positive Results, 
             No-Go Theorems, and the Memory Integral Obstruction},
  author  = {Cheng, John Shun Leong},
  journal = {Foundations of Physics},
  year    = {2026},
  doi     = {10.5281/zenodo.19242134},
  note    = {Verification code: https://github.com/cjlcv6061-svg/adm-verification}
}
```

## License

MIT License. See [LICENSE](LICENSE) for details.
