import pandas as pd
from src.utils import load_dataset, save_features
from src.feature_aac import compute_aac
from src.feature_charge import compute_charge
from src.feature_hydrophobicity import compute_hydrophobicity
from src.feature_embeddings import ProteinEmbedder
import tqdm  # for progress bar

def extract_all_features(dataset_path, output_path, use_embeddings=True):
    df = load_dataset(dataset_path)

    # Initialize embedder if embeddings are required
    if use_embeddings:
        embedder = ProteinEmbedder()

    all_features = []
    for _, row in tqdm.tqdm(df.iterrows(), total=len(df)):
        seq = row["Sequence"]

        features = {}
        # Hand-crafted features
        features.update(compute_aac(seq))
        features.update(compute_charge(seq))
        features.update(compute_hydrophobicity(seq))

        # Embeddings
        if use_embeddings:
            embedding_vector = embedder.get_embedding(seq)
            embedding_features = {f"E_{i}": val for i, val in enumerate(embedding_vector)}
            features.update(embedding_features)

        # Add metadata
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
