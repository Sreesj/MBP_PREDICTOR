# src/feature_ctd.py
"""
Compute CTD (Composition, Transition, Distribution) descriptors
based on amino acid property groupings.
"""

import numpy as np

# Example grouping: Charge
# Groups: Positive (K, R, H), Negative (D, E), Neutral (others)
charge_groups = {
    "positive": set("KRH"),
    "negative": set("DE"),
    "neutral": set("ACFGILMNPQSTVWY")
}


def _group_sequence(sequence, groups):
    """Map amino acids to their group labels."""
    return [g for aa in sequence for g, s in groups.items() if aa in s]


def compute_ctd(sequence: str) -> dict:
    """
    Compute CTD (Composition, Transition, Distribution) descriptors for charge.
    Returns a dictionary of features.
    """
    if not sequence:
        return {}

    features = {}

    # ---- 1. Composition ----
    grouped = _group_sequence(sequence, charge_groups)
    total_len = len(grouped)
    for g in charge_groups:
        features[f"CTDC_{g}"] = grouped.count(g) / total_len

    # ---- 2. Transition ----
    transitions = {f"{g1}_to_{g2}": 0 for g1 in charge_groups for g2 in charge_groups if g1 != g2}
    for i in range(len(grouped) - 1):
        if grouped[i] != grouped[i + 1]:
            key = f"{grouped[i]}_to_{grouped[i+1]}"
            if key in transitions:
                transitions[key] += 1
            else:
                # symmetric: A->B == B->A
                transitions[f"{grouped[i+1]}_to_{grouped[i]}"] += 1
    total_transitions = sum(transitions.values()) or 1
    for k, v in transitions.items():
        features[f"CTDT_{k}"] = v / total_transitions

    # ---- 3. Distribution ----
    for g in charge_groups:
        positions = [i for i, x in enumerate(grouped, 1) if x == g]
        if positions:
            percentiles = [0, 25, 50, 75, 100]
            for p in percentiles:
                idx = int(len(positions) * p / 100) - 1
                idx = max(idx, 0)
                features[f"CTDD_{g}_{p}"] = positions[idx] / total_len
        else:
            for p in [0, 25, 50, 75, 100]:
                features[f"CTDD_{g}_{p}"] = 0.0

    return features
