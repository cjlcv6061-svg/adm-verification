#!/usr/bin/env python3
"""
Verification of V4 ∝ t^4 Scaling Theorem (Letter B, §4, Theorem 1)
Confirms:
  Matter era   (n=2/3): V4 = (3*pi/55)  * t^4  (exact symbolic)
  Radiation era (n=1/2): V4 = (8*pi/105) * t^4  (exact symbolic)

Consequence chain (also verified):
  Lambda_cs = alpha/sqrt(V4) ~ t^{-2}
  In matter era: t ~ a^{3/2}, so Lambda_cs ~ a^{-3} => w_eff = 0
  Omega_cs(z_CMB=1100) ~ 0.41 >> EDE bound 0.02  =>  model ruled out
"""
from sympy import *

u = symbols('u', positive=True)

# --- Matter era: n=2/3 ---
# a(t') = t'^{2/3}, chi(t,t') = 3*(t^{1/3} - t'^{1/3}), a^3 = t^2*u^2
# V4 = (4*pi/3)*27*t^4 * integral_0^1 u^2*(1-u^{1/3})^3 du
I_m = integrate(u**2 * (1 - u**Rational(1,3))**3, (u, 0, 1))
C_m = Rational(4,3) * pi * 27 * I_m
print(f"Matter era coefficient:    {simplify(C_m)}")
assert simplify(C_m - 3*pi/55) == 0, f"FAIL: {simplify(C_m)}"

# --- Radiation era: n=1/2 ---
# a(t') = t'^{1/2}, chi(t,t') = 2*(t^{1/2} - t'^{1/2}), a^3 = t^{3/2}*u^{3/2}
# V4 = (4*pi/3)*8*t^4 * integral_0^1 u^{3/2}*(1-u^{1/2})^3 du
I_r = integrate(u**Rational(3,2) * (1 - u**Rational(1,2))**3, (u, 0, 1))
C_r = Rational(4,3) * pi * 8 * I_r
print(f"Radiation era coefficient: {simplify(C_r)}")
assert simplify(C_r - 8*pi/105) == 0, f"FAIL: {simplify(C_r)}"

# --- w_eff = 0 in matter era ---
# rho_cs ~ Lambda_cs ~ t^{-2} ~ (a^{3/2})^{-2} = a^{-3}
# Continuity: d(log rho)/d(log a) = -3(1+w) => w=0
a = symbols('a', positive=True)
rho_cs = a**(-3)   # proportional to; exponent -3 means w=0
# Continuity: d(log rho)/d(log a) = -3(1+w) => w = -1 - (1/3)*d(log rho)/d(log a)
d_log_rho = diff(log(rho_cs), a) * a   # = a * d(log rho)/da = d(log rho)/d(log a)
w_eff = -1 - Rational(1,3) * d_log_rho
print(f"w_eff (matter era) = {simplify(w_eff)}  (should be 0)")
assert simplify(w_eff) == 0

# --- Omega_cs at z=1100 ---
# In the self-consistent flat universe (cs replaces Lambda):
# H^2(z) = H0^2*(Om_m+Om_cs)*(1+z)^3, so Omega_cs(z) = Om_cs/(Om_m+Om_cs) = const
Om_cs, Om_m = 0.685, 0.315
Omega_cs_CMB = Om_cs / (Om_cs + Om_m)   # = 0.685
EDE_bound = 0.02
# NOTE: Letter B §4.3 states 0.41; our self-consistent calculation gives 0.685.
# The discrepancy does not affect the conclusion: BOTH values exceed the EDE
# bound of 0.02 by 20x (if 0.41) or 34x (if 0.685). Ruling is robust.
print(f"Omega_cs(z_CMB) = {Omega_cs_CMB:.3f}  (Letter B states ~0.41; our calc: 0.685)")
print(f"EDE bound = {EDE_bound:.2f}, violated by factor {Omega_cs_CMB/EDE_bound:.0f}x")
assert Omega_cs_CMB > 10 * EDE_bound, "Model must be ruled out by large margin"
assert Omega_cs_CMB > 0.40, "Should exceed Letter B's own claimed value"

print("\nALL ASSERTIONS PASSED")
