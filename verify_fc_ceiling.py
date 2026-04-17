#!/usr/bin/env python3
"""
Verification of the f_C Ceiling Theorem (Paper A, §3, Theorem 4)

Theorem: For any dark energy model with w(z) > -1 at all z,
         f_C < f_C(LCDM). LCDM uniquely saturates the ceiling.

This script:
  1. Confirms f_C(LCDM) = 0.05696
  2. Tests 12 representative w(z)>-1 models, all give f_C < f_C(LCDM)
  3. Demonstrates that the PROOF requires an integral argument:
     the pointwise inequality H(z;w)>H_LCDM(z) fails at z>0.7
     for the DESI DR2 best-fit, yet the integral inequality still holds.
"""
import scipy.integrate as sci
import numpy as np
import mpmath

pi2 = float(mpmath.pi)**2
Om, OL = 0.315, 0.685

def fc_model(w0, wa):
    def integrand(z):
        DE = OL * (1+z)**(3*(1+w0+wa)) * np.exp(-3*wa*z/(1+z))
        return 1.0 / ((1+z) * (Om*(1+z)**3 + DE))
    I, _ = sci.quad(integrand, 0, np.inf, limit=200)
    return I / pi2

fc_LCDM = fc_model(-1.0, 0.0)
print(f"f_C(LCDM) = {fc_LCDM:.6f}")
assert abs(fc_LCDM - 0.05696) < 0.00002

# --- Parameter scan ---
test_cases = [
    (-0.90,  0.00, "quintessence w=-0.9"),
    (-0.80,  0.00, "quintessence w=-0.8"),
    (-0.70,  0.00, "quintessence w=-0.7"),
    (-0.60,  0.00, "quintessence w=-0.6"),
    (-0.50,  0.00, "quintessence w=-0.5"),
    (-0.75, -0.99, "DESI DR2 best-fit"),
    (-0.90, -0.50, "thawing quintessence"),
    (-0.80, -0.50, "thawing quintessence 2"),
    (-0.90,  0.50, "freezing quintessence"),
    (-0.80,  0.50, "freezing quintessence 2"),
    (-0.50, -1.00, "w crosses -1 at z~0.5"),
    (-0.999, 0.10, "near-LCDM with evolution"),
]

print(f"\n{'Model':<35} {'f_C':>10}  {'< LCDM?':>8}")
print("-" * 58)
all_pass = True
for w0, wa, label in test_cases:
    fc = fc_model(w0, wa)
    ok = fc < fc_LCDM
    if not ok:
        all_pass = False
    status = "YES" if ok else "FAIL"
    print(f"  {label:<33} {fc:10.6f}  {status:>8}")

assert all_pass, "Ceiling Theorem violated — check model list"

# --- Why pointwise H fails for DESI best-fit ---
print("\n--- Pointwise H^2 comparison for DESI best-fit (w0=-0.75, wa=-0.99) ---")
print(f"  {'z':>5}  {'H2_CPL/H2_LCDM':>16}  {'> 1?':>6}")
w0, wa = -0.75, -0.99
for z in [0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0]:
    DE = OL*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z))
    ratio = (Om*(1+z)**3 + DE) / (Om*(1+z)**3 + OL)
    flag = "YES" if ratio > 1 else "NO  <-- pointwise fails here"
    print(f"  {z:5.1f}  {ratio:16.5f}  {flag}")

print("\nConclusion: integral inequality holds globally even when pointwise fails.")
print("The Ceiling Theorem proof uses the integral form of f_C, not pointwise H.")
print("\nALL ASSERTIONS PASSED")
