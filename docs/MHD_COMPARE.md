# C-MHD-01 — MHD efficiency fence

**Date:** 2026-08-30  
**Manuscript claim (public Work No. 2.2 / VC-004 summaries):** combined magneto-charge generator (MZG) + MHD path at **~5%** with copper conductors and high-temperature insulation (mica, porcelain), aimed at high-ampere solenoid feed.

This note compares *that number* to published MHD practice. It does **not** import MZG geometry, GCD current ontology, or a plant design.

## What “5%” sits next to

| Class | Published figure | Source class |
|-------|------------------|--------------|
| C-MHD-01 headline | ~5% | manuscript summary |
| Early one-component LM-MHD fog-flow cycle predictions | ~3–4% | 1970 survey of liquid-metal MHD cycles |
| Modified separator / injector-condenser LM-MHD cycle predictions | ~10–20% | same survey |
| Highest predicted two-component slug-flow LM-MHD in that survey | ~30% (optimistic cycle study) | same survey |
| Standalone open-cycle coal Hall/duct MHD (typical demonstrated) | ~17% | standard MHD generator reviews |
| Closed-cycle disc MHD enthalpy-extraction record (1994, Tokyo Tech) | 22% efficiency / 30.2% peak enthalpy extraction | closed-cycle disc experiments |
| Reciprocating liquid-metal MHD prototypes | ~45–57% *generator* efficiency at small power (W–kW class; one sea-state test ~57%) | 2025 LMMHD review |
| Fossil MHD *combined* with steam/Brayton bottoming (projected, not a commercial fleet fact) | ~50–60% plant | DOE-era and textbook projections |

Power density in a conventional MHD channel scales as σ u² B². Plasma MHD wants high T (thermal ionization, often seeded alkali, ≳ ~1800 K) or non-equilibrium ionization; liquid-metal MHD trades velocity for conductivity and can run much colder.

## Reading for C-MHD-01

- **5% is not insane.** It sits with conservative 1960s–70s liquid-metal *cycle* estimates, not with 50–60% combined-plant projections and not with small LMMHD prototype generator efficiencies.
- Copper + mica/porcelain is ordinary high-temperature electrical practice. It is **not** an HTS MHD magnet program. Magnet-capability questions stay in HighTc.
- Demonstrated standalone plasma-MHD converters are typically tens of percent *generator* efficiency, still unattractive alone versus a 40% Rankine plant — which is why the literature talks topping cycles. That debate is independent of GCD.
- The MZG (“magneto-charge generator”) half of the manuscript pair has **no** counterpart in the Faraday / Hall / disc / LMMHD literature above. Do not treat 5% as a measured MZG+MHD stack.

## Verdict

`literature-compared-conservative`. The 5% headline is a low-side engineering guess relative to later MHD data. It does **not** validate GCD, a fusion-pumped current source, or a vehicle power plant.

## Forbidden follow-ups

No channel CAD, no electrode spacing, no seed-chemical recipes, no “build the MZG.” If Fusion-Abundance ever wants MHD as a conversion *question*, start from the Faraday/Hall/σu²B² literature, not from VC-004 schematics.
