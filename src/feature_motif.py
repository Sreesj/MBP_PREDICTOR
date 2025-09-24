# src/feature_motif.py
import re
from typing import List, Dict


def compute_motif(seq: str, motifs: List[str] = None) -> Dict[str, int]:
    """
    Detect biologically relevant motifs in a protein sequence.

    Parameters
    ----------
    seq : str
        Amino acid sequence (single-letter code).
    motifs : list of str, optional
        List of motif patterns to search for.
        Supported format:
          - Exact strings, e.g., "KR", "RR"
          - Wildcard 'X' meaning any amino acid, e.g., "KXK" → regex "K.K"
          - Standard regex patterns, e.g., "K[RK]" → K followed by R or K

        If None, defaults to common MBP-related motifs.

    Returns
    -------
    dict
        Keys are motif names (Motif_<pattern>), values are 0/1 flags
        indicating presence in the sequence.
    """

    # Default motifs relevant for MBPs (positively charged clusters)
    if motifs is None:
        motifs = [
            "KR",    # Lys-Arg
            "RR",    # Arg-Arg
            "KK",    # Lys-Lys
            "KXK",   # Lys-any-Lys
            "K[RK]K",  # Lys-(Lys/Arg)-Lys
            "R..R",  # Arg with 2 aa gap
        ]

    features = {}
    for motif in motifs:
        # Convert wildcard X → regex .
        motif_pattern = motif.replace("X", ".")
        try:
            found = re.search(motif_pattern, seq) is not None
        except re.error as e:
            raise ValueError(f"Invalid motif pattern: {motif} ({e})")

        key = f"Motif_{motif}"
        features[key] = 1 if found else 0

    return features


if __name__ == "__main__":
    # ✅ Quick test
    test_seq = "MKRAGKKLMRRQK"
    result = compute_motif(test_seq)
    print("Sequence:", test_seq)
    print("Motif features:", result)
