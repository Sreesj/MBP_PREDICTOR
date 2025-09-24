# src/feature_physicochemical.py

from typing import Dict

# Zimmerman Polarity Scale
POLARITY_SCALE = {
    'A': 0.0, 'R': 52.0, 'N': 3.38, 'D': 49.7, 'C': 1.48,
    'Q': 3.53, 'E': 49.9, 'G': 0.0, 'H': 51.6, 'I': 0.13,
    'L': 0.13, 'K': 49.5, 'M': 1.43, 'F': 0.35, 'P': 1.58,
    'S': 1.67, 'T': 1.66, 'W': 2.1, 'Y': 1.61, 'V': 0.13
}

# Chou–Fasman Flexibility Scale
FLEXIBILITY_SCALE = {
    'A': 0.36, 'R': 0.52, 'N': 0.46, 'D': 0.51, 'C': 0.35,
    'Q': 0.49, 'E': 0.50, 'G': 0.54, 'H': 0.32, 'I': 0.46,
    'L': 0.37, 'K': 0.47, 'M': 0.30, 'F': 0.31, 'P': 0.52,
    'S': 0.51, 'T': 0.44, 'W': 0.31, 'Y': 0.42, 'V': 0.39
}

# Chou–Fasman Secondary Structure Propensities
HELIX_SCALE = {
    'A': 1.45, 'R': 1.00, 'N': 0.67, 'D': 1.01, 'C': 0.77,
    'Q': 1.11, 'E': 1.51, 'G': 0.57, 'H': 1.00, 'I': 1.08,
    'L': 1.34, 'K': 1.07, 'M': 1.20, 'F': 1.12, 'P': 0.57,
    'S': 0.77, 'T': 0.83, 'W': 1.14, 'Y': 0.61, 'V': 1.06
}

SHEET_SCALE = {
    'A': 0.97, 'R': 0.90, 'N': 0.89, 'D': 0.54, 'C': 1.30,
    'Q': 1.10, 'E': 0.37, 'G': 0.75, 'H': 0.87, 'I': 1.60,
    'L': 1.22, 'K': 0.74, 'M': 1.67, 'F': 1.28, 'P': 0.55,
    'S': 0.75, 'T': 1.19, 'W': 1.19, 'Y': 1.29, 'V': 1.70
}

COIL_SCALE = {
    'A': 0.97, 'R': 0.95, 'N': 1.34, 'D': 1.46, 'C': 1.30,
    'Q': 0.98, 'E': 0.74, 'G': 1.56, 'H': 0.95, 'I': 0.47,
    'L': 0.92, 'K': 1.01, 'M': 0.60, 'F': 0.59, 'P': 1.52,
    'S': 1.43, 'T': 0.96, 'W': 0.88, 'Y': 1.05, 'V': 0.50
}


def compute_physicochemical(sequence: str) -> Dict[str, float]:
    """
    Compute average physicochemical properties:
    - Polarity
    - Flexibility
    - Secondary structure propensities (helix, sheet, coil)
    """
    if not sequence:
        return {}

    seq = sequence.upper()
    n = len(seq)

    # Compute averages
    polarity = sum(POLARITY_SCALE.get(aa, 0) for aa in seq) / n
    flexibility = sum(FLEXIBILITY_SCALE.get(aa, 0) for aa in seq) / n
    helix = sum(HELIX_SCALE.get(aa, 0) for aa in seq) / n
    sheet = sum(SHEET_SCALE.get(aa, 0) for aa in seq) / n
    coil = sum(COIL_SCALE.get(aa, 0) for aa in seq) / n

    return {
        "Polarity": polarity,
        "Flexibility": flexibility,
        "Helix_Propensity": helix,
        "Sheet_Propensity": sheet,
        "Coil_Propensity": coil
    }
