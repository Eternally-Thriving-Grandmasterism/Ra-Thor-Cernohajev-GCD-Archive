# Testable Claims Register (first pass)

**Rule:** every row is a *manuscript claim*, not a measured fact. Status starts at `unvalidated`.

Independent check means: comparison to published magnet, MHD, fusion, or planetary-field data, or a new experiment. Passing a dimensional-consistency check is **not** validation of the underlying GCD ontology.

## Fusion / chamber (chiefly Work No. 8 / VC-010, VC-001)

| ID | Claim (as stated in public summaries of the MS) | Status | Notes |
|----|--------------------------------------------------|--------|-------|
| C-FUS-01 | d+d channels considered: t+p, ³He+n, ⁴He+γ | unvalidated-as-GCD | Channels themselves are standard nuclear data; GCD framing is not |
| C-FUS-02 | Working pressure ≳ 2000 atm in TYS chamber | unvalidated | Extreme vs. magnetic-confinement practice; inertial/pulsed devices use different language |
| C-FUS-03 | Excess negative charge density ~ 0.2×10⁻⁶ C/m³ at ignition framing | unvalidated | Needs SI restatement and comparison to plasma quasineutrality |
| C-FUS-04 | Electron concentration ≳ 0.12×10¹³ m⁻³ at discharge initiation | unvalidated | Check units; 10¹³ m⁻³ is low vs. fusion-relevant n_e |
| C-FUS-05 | Solar-core density used as analog ρ ≈ 2×10³ kg/m³ | check-against-literature | Standard solar-mean-density estimate is order 1.4×10³ kg/m³; core is much higher |
| C-FUS-06 | Target regulation field B = 16.65 T from solar/terrestrial magnetic-moment ratio | unvalidated-as-method | 16.65 T is within modern HTS/REBCO magnet capability; the *derivation* is not standard |

## Magnets / solenoids (Work No. 2, 8)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MAG-01 | 32-solenoid spherical array as regulation geometry | unvalidated | Geometry only; do not treat as a build spec |
| C-MAG-02 | Example winding sketch: 2 mm wire, 2 mm gaps, 2 cm solenoid diameter, ~8000 turns/m, I ≈ 1.65×10³ A → 16.65 T | dimensional-check-open | Compare to Ampere-turn / B formulas and quench/cooling reality |
| C-MAG-03 | Work No. 2 craft-scale solenoid coverage language (~30 m disc, dense Al-alloy windings in Si-alloy matrix) | archive-only | Out of scope for fabrication notes; keep as historical claim |

## MHD / power conversion (Work No. 2.2 / VC-004)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MHD-01 | Combined MZG + MHD path proposed at ~5% efficiency with copper + high-T insulation | unvalidated | Conventional MHD literature exists; do not import GCD current ontology |
| C-MHD-02 | Candidate high-Z / odd-valence elements listed as superconductor-interest set | literature-compare | Route any materials interest through HighTc lattice, not this archive |

## Materials / monocrystal (Work No. 4 / VC-006)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-MAT-01 | Polycrystal domains have locally parallel “neutrino-magnetic” flows that cancel across grain boundaries | unvalidated | No mainstream mechanism |
| C-MAT-02 | A single-crystal hull would synchronize electron-sphere / nuclear rotation and produce net thrust | unvalidated | Archive-only; no fabrication path in this repo |

## Planetary / solar B tables (Work No. 7 / VC-009)

| ID | Claim | Status | Notes |
|----|-------|--------|-------|
| C-PLN-01 | Tabulated planetary magnetic intensities derived from GCD force-balance | compare-to-measured | Earth/Jupiter/Saturn measured fields exist; use as a *table audit*, not a theory proof |

## Explicitly not testable here

- Recovered-craft provenance statements.
- Instantaneous cosmic neutrino-magnetic flux as a force carrier.
- Civilizational-cycle predictions (Works 6, 10).
- Any construction of a vehicle or reactor from these pages.
