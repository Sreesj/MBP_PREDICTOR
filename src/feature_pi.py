# src/feature_pi.py
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def compute_pi(sequence: str) -> float:
    """
    Compute the theoretical isoelectric point (pI) of a protein sequence.
    """
    try:
        analysed_seq = ProteinAnalysis(sequence)
        return analysed_seq.isoelectric_point()
    except Exception:
        return None
