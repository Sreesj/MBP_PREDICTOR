def compute_charge(sequence: str, pH: float = 7.0):
    """
    Compute net charge of a protein sequence at given pH 
    using Henderson–Hasselbalch equation and amino acid pKa values.
    """
    # Standard pKa values
    pKa = {
        "Cterm": 3.1,
        "Nterm": 8.0,
        "D": 3.9,
        "E": 4.3,
        "C": 8.3,
        "Y": 10.1,
        "H": 6.0,
        "K": 10.5,
        "R": 12.5
    }

    # Count amino acids
    counts = {aa: sequence.count(aa) for aa in "DECYHKR"}

    # N-terminal group (basic)
    charge = 1 / (1 + 10 ** (pH - pKa["Nterm"]))

    # C-terminal group (acidic)
    charge += -1 / (1 + 10 ** (pKa["Cterm"] - pH))

    # Acidic side chains (D, E, C, Y)
    for aa in ["D", "E", "C", "Y"]:
        charge += counts[aa] * (-1 / (1 + 10 ** (pKa[aa] - pH)))

    # Basic side chains (H, K, R)
    for aa in ["H", "K", "R"]:
        charge += counts[aa] * (1 / (1 + 10 ** (pH - pKa[aa])))

    return {"Charge": charge}
