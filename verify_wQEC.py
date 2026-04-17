#!/usr/bin/env python3
"""
Verification of QEC Dark Energy No-Go (Paper A, §9, Theorem 3)
Reproduces:
  w_QEC = -1 + 1/(3*pi^2)  = -0.9662
  H0_QEC                   = 66.4 km/s/Mpc
  Hubble tension (LCDM)    = 5.4 sigma
  Hubble tension (QEC)     = 6.3 sigma
  DESI w0 tension          = 3.1 sigma
  DESI wa tension          = 3.5 sigma
  Dynamic suppression      ~ 10^{-17}
"""
import mpmath
mpmath.mp.dps = 50

pi2 = mpmath.pi**2

# w_QEC from MDS + Lloyd saturation (Paper A §9.1, Eq. wQEC)
w_QEC = -1 + 1/(3*pi2)
print(f"w_QEC = -1 + 1/(3*pi^2) = {float(w_QEC):.4f}  (Paper A claims -0.966)")
assert abs(float(w_QEC) + 0.9662) < 0.0001, f"FAIL: {float(w_QEC)}"

# DESI DR2 tensions (Paper A §9.2)
w0_DESI, s_w0 = -0.75, 0.07    # DESI DR2 BAO+CMB+SNe
wa_DESI, s_wa = -0.99, 0.28
t_w0 = abs(float(w_QEC) - w0_DESI) / s_w0
t_wa = abs(0.0 - wa_DESI) / s_wa
print(f"DESI w0 tension: {t_w0:.2f}sigma  (Paper: 3.1sigma)")
print(f"DESI wa tension: {t_wa:.2f}sigma  (Paper: 3.5sigma)")
assert abs(t_w0 - 3.1) < 0.1, f"FAIL w0 tension: {t_w0}"
assert abs(t_wa - 3.5) < 0.1, f"FAIL wa tension: {t_wa}"

# Hubble tensions (Paper A §9.2, footnote)
H0_local, s_H0 = 73.04, 1.04  # Riess et al. 2022
H0_LCDM  = 67.4               # Planck 2018
H0_QEC   = 66.4               # CMB-calibrated QEC prediction
t_LCDM = (H0_local - H0_LCDM) / s_H0
t_QEC  = (H0_local - H0_QEC)  / s_H0
print(f"Hubble tension LCDM: {t_LCDM:.2f}sigma  (Paper: 5.4sigma)")
print(f"Hubble tension QEC:  {t_QEC:.2f}sigma   (Paper: 6.3sigma)")
assert abs(t_LCDM - 5.4) < 0.1, f"FAIL LCDM tension: {t_LCDM}"
assert abs(t_QEC  - 6.3) < 0.1, f"FAIL QEC tension: {t_QEC}"

# Dynamic correction suppression (Paper A §9.3)
# Prefactor: pi * hbar * G_N * H0 / c^5 ~ 2e-104 s
# SMBH accretion rate: dot_Sigma ~ 1e87 s^{-1}
prefactor   = 2e-104   # seconds
Sigma_dot   = 1e87     # s^{-1}
suppression = prefactor * Sigma_dot
print(f"Dynamic/static suppression ~ {suppression:.0e}  (Paper: ~10^-17)")
assert 1e-18 < suppression < 1e-16, f"FAIL suppression: {suppression}"

print("\nALL ASSERTIONS PASSED")
