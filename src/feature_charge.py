def compute_charge(sequence: str):
    """Very simple net charge: (K+R+H) - (D+E)."""
    pos = sum(sequence.count(aa) for aa in "KRH")
    neg = sum(sequence.count(aa) for aa in "DE")
    return {"Charge": pos - neg}
