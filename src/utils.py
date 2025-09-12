import pandas as pd

def load_dataset(path):
    """Load dataset with Protein_ID, Sequence, Label."""
    return pd.read_csv(path)

def save_features(df, path):
    """Save extracted features as CSV."""
    df.to_csv(path, index=False)
