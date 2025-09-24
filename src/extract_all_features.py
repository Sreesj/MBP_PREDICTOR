# extract_all_features.py

import pandas as pd
import tqdm  # for progress bar

from src.utils import load_dataset, save_features
from src.feature_aac import compute_aac
from src.feature_charge import compute_charge
from src.feature_hydrophobicity import compute_hydrophobicity
from src.feature_embeddings import ProteinEmbedder
from src.feature_pi import compute_pi
from src.feature_motif import compute_motif


def extract_all_features(dataset_path, output_path, use_embeddings=True):
    """
    Extract all protein features (AAC, charge, hydrophobicity, pI, motifs, embeddings).

    Parameters
    ----------
    dataset_path : str
        Path to input dataset CSV (must contain 'Sequence', 'Label', 'Protein_ID').
    output_path : str
        Path to save the extracted features CSV.
    use_embeddings : bool, optional
        If True, compute embeddings with ProteinEmbedder (default=True).
    """
    df = load_dataset(dataset_path)

    # Initialize embedder only once
    embedder = ProteinEmbedder() if use_embeddings else None

    all_features = []
    for _, row in tqdm.tqdm(df.iterrows(), total=len(df)):
        seq = row["Sequence"]

        features = {}

        # --- Hand-crafted features ---
        features.update(compute_aac(seq))              # Amino Acid Composition
        features.update(compute_charge(seq))           # Net charge
        features.update(compute_hydrophobicity(seq))   # Hydrophobicity
        features.update(compute_pi(seq))               # Isoelectric point
        features.update(compute_motif(seq))            # Motif presence

        # --- Embeddings ---
        if use_embeddings:
            embedding_vector = embedder.get_embedding(seq)
            embedding_features = {f"E_{i}": val for i, val in enumerate(embedding_vector)}
            features.update(embedding_features)

        # --- Metadata ---
        features["Label"] = row["Label"]
        features["Protein_ID"] = row["Protein_ID"]

        all_features.append(features)

    feature_df = pd.DataFrame(all_features)
    save_features(feature_df, output_path)
    print(f"✅ Features saved to {output_path}")


if __name__ == "__main__":
    extract_all_features(
        dataset_path="data/mbp_dataset.csv",
        output_path="data/features_with_embeddings.csv",
        use_embeddings=True
    )
