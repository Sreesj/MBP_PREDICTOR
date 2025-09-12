hydro_scale = {
    "A": 1.8, "C": 2.5, "D": -3.5, "E": -3.5, "F": 2.8, "G": -0.4, "H": -3.2,
    "I": 4.5, "K": -3.9, "L": 3.8, "M": 1.9, "N": -3.5, "P": -1.6, "Q": -3.5,
    "R": -4.5, "S": -0.8, "T": -0.7, "V": 4.2, "W": -0.9, "Y": -1.3
}

def compute_hydrophobicity(sequence: str):
    """Return mean, max, and min hydrophobicity."""
    values = [hydro_scale.get(aa, 0) for aa in sequence]
    return {
        "Hydro_mean": sum(values) / len(values),
        "Hydro_max": max(values),
        "Hydro_min": min(values)
    }
