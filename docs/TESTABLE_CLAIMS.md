# Testable Claims Register

**Rule:** every row is a *manuscript claim*, not a measured fact.

Independent check means: comparison to published magnet, MHD, fusion, or planetary-field data, or a new experiment. Passing a dimensional-consistency check is **not** validation of the underlying GCD ontology.

Updated 2026-08-30: C-PLN-01 table audit, C-MAG-02 Ampere-turn note, C-FUS-04/05 SI restatement.

## Fusion / chamber (chiefly Work No. 8 / VC-010, VC-001)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-FUS-01 | d+d channels: t+p, ³He+n, ⁴He+γ | unvalidated-as-GCD | Channels themselves are standard nuclear data |
| C-FUS-02 | Working pressure ≳ 2000 atm in TYS chamber | unvalidated | Extreme vs. MCF practice |
| C-FUS-03 | Excess negative charge density ~ 0.2×10⁻⁶ C/m³ | internally-consistent-with-C-FUS-04 | ~1.2×10¹² m⁻³ imbalance; see SI_UNIT_CHECKS |
| C-FUS-04 | n_e ≳ 0.12×10¹³ m⁻³ | audited-too-low-for-fusion | 1.2×10¹² m⁻³; ionosphere-class, 7–9 orders below MCF |
| C-FUS-05 | Solar-core analog ρ ≈ 2×10³ kg/m³ | audited-mislabelled-mean-as-core | Matches solar *mean* density ~1.4×10³; core is ~10⁵ |
| C-FUS-06 | B = 16.65 T from solar/terrestrial moment ratio | unvalidated-as-method | Field *magnitude* is HTS-class; derivation is not |

## Magnets / solenoids (Work No. 2, 8)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MAG-01 | 32-solenoid spherical array | unvalidated | Geometry only |
| C-MAG-02 | 8000 turns/m, 1.65 kA → 16.65 T | dimensionally-consistent-with-μ0nI | B_∞ = 16.588 T (ratio 0.996). Not a build spec |
| C-MAG-03 | 30 m disc solenoid coverage | archive-only | No fabrication notes |

## MHD / power conversion (Work No. 2.2 / VC-004)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MHD-01 | MZG + MHD ~5% with copper + high-T insulation | unvalidated | Compare only via LITERATURE_FENCE |
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
