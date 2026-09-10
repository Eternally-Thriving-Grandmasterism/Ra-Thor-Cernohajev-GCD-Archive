# Testable Claims Register

**Rule:** every row is a *manuscript claim*, not a measured fact.

Independent check means: comparison to published magnet, MHD, fusion, or planetary-field data, or a new experiment. Passing a dimensional-consistency check is **not** validation of the underlying GCD ontology.

Updated 2026-08-30: C-PLN-01 audit, C-MAG-02 Ampere-turn, C-FUS-04/05 SI, C-MHD-01 literature fence.  
Updated 2026-09-10: C-MAG-02 dimensional check re-run with the array-aggregation flag — see [Appendix A](#appendix-a--c-mag-02-ampere-turn--solenoid-dimensional-check).

## Fusion / chamber (chiefly Work No. 8 / VC-010, VC-001)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-FUS-01 | d+d channels: t+p, ³He+n, ⁴He+γ | unvalidated-as-GCD | Channels themselves are standard nuclear data |
| C-FUS-02 | Working pressure ≳ 2000 atm in TYS chamber | unvalidated | Extreme vs. MCF practice |
| C-FUS-03 | Excess negative charge density ~ 0.2×10⁻⁶ C/m³ | internally-consistent-with-C-FUS-04 | ~1.2×10¹² m⁻³ imbalance; primary-page pin still optional |
| C-FUS-04 | n_e ≳ 0.12×10¹³ m⁻³ | audited-too-low-for-fusion | 1.2×10¹² m⁻³; ionosphere-class, 7–9 orders below MCF |
| C-FUS-05 | Solar-core analog ρ ≈ 2×10³ kg/m³ | audited-mislabelled-mean-as-core | Matches solar *mean* density ~1.4×10³; core is ~10⁵ |
| C-FUS-06 | B = 16.65 T from solar/terrestrial moment ratio | unvalidated-as-method | Field *magnitude* is HTS-class; derivation is not |

## Magnets / solenoids (Work No. 2, 8)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MAG-01 | 32-solenoid spherical array | unvalidated | Geometry only |
| C-MAG-02 | 8000 turns/m, 1.65 kA → 16.65 T | consistent-as-one-long-solenoid; array-aggregation-inconsistent | B_∞ = μ0nI = 16.588 T (ratio 0.996). The same n and I read as the 32-coil array give 0.518 T or 1.62×10⁻² T; array field needs geometry the row does not carry. See [Appendix A](#appendix-a--c-mag-02-ampere-turn--solenoid-dimensional-check). Not a build spec |
| C-MAG-03 | 30 m disc solenoid coverage | archive-only | No fabrication notes |

## MHD / power conversion (Work No. 2.2 / VC-004)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MHD-01 | MZG + MHD ~5% with copper + high-T insulation | literature-compared-conservative | 5% sits with early LM-MHD cycle guesses; standalone plasma MHD ~17–22%; combined-plant projections 50–60%. MZG has no Faraday/Hall counterpart. See MHD_COMPARE |
| C-MHD-02 | Odd-valence superconductor-interest list | literature-compare | Route through HighTc lattice |

## Materials / monocrystal (Work No. 4 / VC-006)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MAT-01 | Polycrystal domain-flow cancellation | unvalidated | No mainstream mechanism |
| C-MAT-02 | Monocrystal hull net thrust | unvalidated | Archive-only |

## Planetary / solar B tables (Work No. 7 / VC-009)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-PLN-01 | GCD force-balance planetary B table | audited-mismatch | Mercury+Earth order-match only; Venus/Mars/Pluto fail; giants 30–230× high. See PLANETARY_B_TABLE_AUDIT |

## Explicitly not testable here

- Recovered-craft provenance statements.
- Instantaneous cosmic neutrino-magnetic flux as a force carrier.
- Civilizational-cycle predictions (Works 6, 10).
- Any construction of a vehicle or reactor from these pages.

## Appendix A — C-MAG-02 Ampere-turn / solenoid dimensional check

**Date:** 2026-09-10. Extends the 2026-08-30 seed note in [SI_UNIT_CHECKS.md](SI_UNIT_CHECKS.md), which computed `B_∞` only.  
**Scope:** arithmetic and units on the numbers already in the C-MAG-02 row. Dimensional consistency is **not** validation of GCD, and this appendix is not a magnet design.

### Inputs (as stated in the row)

| Symbol | Value | Unit |
|--------|-------|------|
| `n` | 8.000×10³ | turns/m (m⁻¹) |
| `I` | 1.65×10³ | A |
| `B_target` | 16.65 | T |

### Formula and units

Interior axial field of a long (idealised infinite) solenoid:

```
B = μ0 · n · I
[T] = [T·m·A⁻¹] · [m⁻¹] · [A]          → units close

μ0  = 4π × 10⁻⁷ T·m·A⁻¹ = 1.2566370614×10⁻⁶
n·I = 8.000×10³ m⁻¹ × 1.65×10³ A = 1.3200×10⁷ A·turn/m   (= H, in A/m)
B   = 1.2566370614×10⁻⁶ × 1.3200×10⁷ = 16.5876 T

B / B_target        = 0.99625        (0.375 % below the headline)
n·I needed for 16.65 T = 16.65 / μ0 = 1.32496×10⁷ A/m   (+0.376 %)
```

Finite length changes this by a factor no greater than one. At the centre of a solenoid of length `L` and radius `R`:

```
B_centre = μ0 · n · I · L / √(L² + 4R²)     ,   L/√(L² + 4R²) ≤ 1
```

`L` and `R` do not appear in the row, so `μ0 n I` can only be read as an upper bound.

### Ampere-turn aggregation flag

The public item summary for VC-010 that carries `n` and `I` describes 8000 m⁻¹ as the **array-summed** winding density of the 32-solenoid set (32 coils × 250 m⁻¹ each; 8000 / 250 = 32 exactly), and 1650 A as the current for the **group**, not the current in each turn. Recomputing per solenoid at 250 m⁻¹:

```
group current shared across 32 coils:  I = 1650/32 = 51.5625 A
  B = μ0 · 250 · 51.5625 = 1.62×10⁻² T        →  headline / this = 1024 = 32²

full 1650 A in each coil:
  B = μ0 · 250 · 1650    = 0.518 T            →  headline / this = 32
```

So the 16.65 T headline is recovered only by applying the 32-fold coil multiplicity to the turn density **and** giving every turn the whole group current — the multiplicity is spent twice. Separately, `μ0 n I` is the interior field of one long solenoid; it is not the superposition at the centre of a sphere of 32 discrete coils, which would require per-coil current, coil radius, coil length, and axis positions.

### Verdict

| Reading of the row | Verdict | Field |
|--------------------|---------|-------|
| One long solenoid, 8000 turns/m, 1650 A in every turn | **consistent** | 16.588 T vs 16.65 T, ratio 0.996 |
| The 32-coil array the same source describes | **inconsistent** | same numbers give 0.518 T or 1.62×10⁻² T |
| Field at the centre of the 32-coil spherical array | **missing geometry** | per-coil current, coil radius, coil length, axis positions absent |

Headline: `consistent` as the textbook `μ0 n I` identity, `inconsistent` as the array it is attached to, `missing geometry` for any array field.

### What this check does not do

- No coil design, winding schedule, conductor, bore, cooling, or quench parameters are derived or reproduced here.
- Passing the `μ0 n I` identity is arithmetic. It says nothing about GCD, and the 16.65 T target itself comes from the solar/terrestrial moment-ratio derivation in C-FUS-06, which stays `unvalidated-as-method`.
- Magnet-capability questions route to the HighTc lattice per [LITERATURE_FENCE.md](LITERATURE_FENCE.md).
