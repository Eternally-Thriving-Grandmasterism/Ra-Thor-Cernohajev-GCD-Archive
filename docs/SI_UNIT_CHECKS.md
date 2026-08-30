# SI unit checks — C-FUS-04, C-FUS-05, C-MAG-02

**Date:** 2026-08-30  
Dimensional consistency ≠ physical validation.

## C-MAG-02 — Ampere-turn vs 16.65 T

Manuscript headline (public Work No. 8 summaries): `n ≈ 8000 turns/m`, `I ≈ 1650 A`, `B_target = 16.65 T`.

Infinite-solenoid estimate:

```
B = μ0 n I
  = (1.256637062e-6) * 8000 * 1650
  = 16.588 T
ratio B / B_target = 0.996
```

**Verdict:** `dimensionally-consistent-with-B=μ0nI`. The headline 16.65 T is the ordinary long-solenoid formula, not a new field law. Finite length, 32-coil sphere, cooling, and quench remain unaddressed. Script: `simulations/dimensional_checks/ampere_turn_note.py`.

## C-FUS-05 — density analog

Public summary uses `M ≈ 2×10³⁰ kg`, `R ≈ 7×10⁸ m` → `ρ ≈ 2×10³ kg/m³` and calls this a solar-*core* analog.

Standard mean-density check:

```
M_☉ ≈ 1.989e30 kg
R_☉ ≈ 6.96e8 m
V = 4/3 π R³ ≈ 1.41e27 m³
ρ_mean ≈ 1.41e3 kg/m³
```

The manuscript number is **solar-mean density**, not core density. Standard solar-core density is order `10⁵ kg/m³`, not `10³`.

**Verdict:** `mislabelled-mean-as-core`. Do not use 2000 kg/m³ as a fusion-chamber analog to the solar core.

## C-FUS-04 — electron number density

Manuscript: `n_e ≳ 0.12×10¹³ m⁻³` = `1.2×10¹² m⁻³`.

Comparison ranges (order of magnitude, not a reactor design):

| Regime | typical n_e (m⁻³) |
|--------|---------------------|
| C-FUS-04 headline | 1.2×10¹² |
| Earth's ionosphere (F-region) | ~10¹¹–10¹² |
| Magnetic-confinement fusion plasma | ~10¹⁹–10²¹ |
| Solar core | ~10³² |

**Verdict:** `seven-to-nine-orders-below-fusion-plasma`. The number sits near ionospheric density, not a TYS core. Status stays unvalidated as a fusion parameter.

## C-FUS-03 (left open)

`0.2×10⁻⁶ C/m³` = `2×10⁻⁷ C/m³`. Dividing by `e` gives a charge-imbalance number density ~`1.2×10¹² m⁻³`, i.e. the same order as C-FUS-04. That is internally consistent with the manuscript's own n_e, and still far from quasineutral fusion plasma practice. No further action until a primary-page citation is pinned.
