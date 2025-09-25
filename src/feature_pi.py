# src/feature_pi.py
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import warnings

def compute_pi(sequence: str) -> float:
    """
    Compute the theoretical isoelectric point (pI) of a protein sequence.
    
    Returns:
        float: pI value if successful, None otherwise.
    """
    try:
        # Validate input
        if not isinstance(sequence, str) or len(sequence) == 0:
            return None

        # Create analysis object
        analysed_seq = ProteinAnalysis(sequence)

        # Get pI - this should return a float
        pi_value = analysed_seq.isoelectric_point()

        # Ensure it's a valid float
        if pi_value is None:
            return None
        if isinstance(pi_value, (int, float)):
            return float(pi_value)
        else:
            # Fallback: log unexpected type
            warnings.warn(f"Unexpected pI type: {type(pi_value)} for sequence: {sequence[:20]}...")
            return None

    except Exception as e:
        # Catch any underlying errors (e.g., invalid amino acids)
        warnings.warn(f"Error computing pI for sequence {sequence[:20]}...: {e}")
        return None
