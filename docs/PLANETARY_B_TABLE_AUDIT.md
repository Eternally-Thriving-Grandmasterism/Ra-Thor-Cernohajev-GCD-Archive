# C-PLN-01 — Work No. 7 planetary B table audit

**Date:** 2026-08-30  
**Source claim:** public summaries of VC-009 / Work No. 7 list intensities in **Oersted**.  
**Comparison convention:** in vacuum / air, 1 Oe ≈ 1 G for this order-of-magnitude audit.  
**Measured reference:** published equatorial (or dipole-equivalent surface) fields from spacecraft-era compilations, not GCD.

Work No. 7 derivation (as summarized by the public archive): a four-force balance

`F_gravitational + F_centripetal = F_centrifugal + F_charge`

plus an assumed excess-electron ratio, then B from motion of that charged mass. That ontology is **not** tested by this table. Only the output numbers are.

## Audit table

| Body | MS (Oe) | Measured equatorial / surface-equivalent (G) | MS / measured | Verdict |
|------|---------|-----------------------------------------------|---------------|---------|
| Mercury | 0.0026 | ~0.003 | ~0.9 | **order match** |
| Venus | 0.47 | ≲ 3×10⁻⁴ (no global dynamo) | ≫ 10³ | **fail** |
| Earth | 0.57 | ~0.31 (dipole equator; surface ~0.25–0.65) | ~1.8 | **order match** |
| Mars | 0.057 | no global dipole; crustal patches ~10⁻² G locally | n/a as global B | **fail as global field** |
| Jupiter | 159 | ~4.2 equator (~10–14 G polar max) | ~38 (vs equator) | **high** |
| Saturn | 47 | ~0.20 | ~235 | **high** |
| Uranus | 7.37 | ~0.23 | ~32 | **high** |
| Neptune | 8.67 | ~0.14 | ~62 | **high** |
| Pluto | 0.045 | no detected global field (New Horizons) | n/a | **fail** |

Measured column sources (independent of GCD): standard spacecraft compilations of equatorial dipole field (Mercury ~0.003 G; Earth ~0.31 G; Jupiter ~4.2 G; Saturn ~0.20 G; Uranus ~0.23 G; Neptune ~0.14 G; Venus/Mars/Pluto — no Earth-class global dynamo).

## Reading

- Inner-rocky **order-of-magnitude luck** on Mercury and Earth does not rescue Venus or Mars.
- Giant-planet MS values are **tens to hundreds of times** the measured equatorial fields. Jupiter's *polar maximum* (~14 G) is still an order below 159 Oe.
- The table therefore does **not** support promoting Work No. 7 numbers into Daedalus, Fusion-Abundance, or HighTc baselines.
- Status for C-PLN-01: `audited-mismatch` for Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto; `order-match-only` for Mercury and Earth.

## What this is not

Not a dynamo paper. Not a GCD proof or disproof of the force-balance story. Just a number-to-number fence.
