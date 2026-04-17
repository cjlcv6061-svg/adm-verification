#!/usr/bin/env python3
"""
Verification of the complexity filling fraction f_C (Paper A, §3, Eq. 3)
Reproduces:
  f_C(LCDM exact)     = 0.05696
  f_C shortcut        = 0.09636  (algebraic approximation)
  Overestimate factor = 1.69 ≈ 1.7
  EdS f_C             = 1/(3*pi^2) = 0.03377
  f_C / f_S           ~ 10^16  (Holographic Capacity Dichotomy)

NOTE on Eq.(3): The denominator [Om*(1+z)^3 + OL] is H(z)^2/H0^2
(the SQUARE of the dimensionless Hubble rate, not its square root).
This arises because the variable change dt = -dz/[(1+z)*H(z)] introduces
one factor of H while the integrand 1/H contributes another.
"""
import mpmath
import scipy.integrate as sci
import numpy as np

mpmath.mp.dps = 50
Om, OL = 0.315, 0.685
pi2 = float(mpmath.pi)**2

# --- Exact integral (Eq. 3 of Paper A) ---
# Denominator is H^2/H0^2 = Om*(1+z)^3 + OL  (NOT the square root)
def integrand_exact(z):
    return 1.0 / ((1 + z) * (Om*(1+z)**3 + OL))

I_exact, _ = sci.quad(integrand_exact, 0, np.inf)
fc_exact = I_exact / pi2
print(f"f_C (exact LCDM integral) = {fc_exact:.5f}")
assert abs(fc_exact - 0.057) < 0.001, f"FAIL: {fc_exact}"

# --- Algebraic shortcut: H0*t0/pi^2 ---
def integrand_t0(z):
    return 1.0 / ((1 + z) * np.sqrt(Om*(1+z)**3 + OL))

H0t0, _ = sci.quad(integrand_t0, 0, np.inf)
fc_shortcut = H0t0 / pi2
print(f"f_C shortcut (H0*t0/pi^2) = {fc_shortcut:.5f}")
assert abs(fc_shortcut - 0.096) < 0.002, f"FAIL: {fc_shortcut}"

factor = fc_shortcut / fc_exact
print(f"Overestimate factor        = {factor:.3f}  (Paper A claims ~1.7)")
assert abs(factor - 1.7) < 0.05, f"FAIL: {factor}"

# --- EdS case (n=2/3 power law) ---
fc_EdS = 1.0 / (3 * pi2)
print(f"EdS f_C = 1/(3*pi^2)      = {fc_EdS:.5f}  (Paper A claims ~0.034)")
assert abs(fc_EdS - 0.034) < 0.001

# --- Holographic Capacity Dichotomy ---
fS = 1e-18          # S_actual/S_Hubble (Egan & Lineweaver 2010)
ratio = fc_exact / fS
print(f"f_C/f_S = {ratio:.2e}    (Paper A claims ~10^16)")
assert 1e15 < ratio < 1e17

print("\nALL ASSERTIONS PASSED")
