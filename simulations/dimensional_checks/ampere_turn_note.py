#!/usr/bin/env python3
"""C-MAG-02 dimensional note.

Compares the manuscript headline (n ≈ 8000 turns/m, I ≈ 1650 A, B_target = 16.65 T)
to the infinite-solenoid estimate B = mu0 * n * I.

This is not a magnet design, quench study, or winding schedule.
"""

MU0 = 1.256637062e-6  # N A^-2
N_TURNS_PER_M = 8000.0
I_A = 1650.0
B_TARGET_T = 16.65


def main() -> None:
    b_infinite = MU0 * N_TURNS_PER_M * I_A
    ratio = b_infinite / B_TARGET_T if B_TARGET_T else float("nan")
    print("C-MAG-02 dimensional note")
    print(f"  n = {N_TURNS_PER_M:.0f} turns/m (manuscript headline)")
    print(f"  I = {I_A:.0f} A (manuscript headline)")
    print(f"  B_target = {B_TARGET_T} T (manuscript headline)")
    print(f"  B_infinite_solenoid = mu0*n*I = {b_infinite:.3f} T")
    print(f"  ratio B_infinite / B_target = {ratio:.3f}")
    print()
    print("Interpretation:")
    print("  Infinite-solenoid estimate is an upper-bound idealization.")
    print("  Finite length, gaps, spherical packing of 32 coils, conductor")
    print("  cross-section, cooling, and quench are all omitted.")
    print("  Result does not validate GCD or a vehicle architecture.")


if __name__ == "__main__":
    main()
