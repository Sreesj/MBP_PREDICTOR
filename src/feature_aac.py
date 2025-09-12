AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

def compute_aac(sequence: str):
    """Return amino acid composition (fraction of each residue)."""
    length = len(sequence)
    return {f"AAC_{aa}": sequence.count(aa) / length for aa in AMINO_ACIDS}
