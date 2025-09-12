# src/feature_embeddings.py
import torch
from transformers import BertModel, BertTokenizer

class ProteinEmbedder:
    def __init__(self, model_name="Rostlab/prot_bert", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Loading model {model_name} on {self.device}...")
        self.tokenizer = BertTokenizer.from_pretrained(model_name, do_lower_case=False)
        self.model = BertModel.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def get_embedding(self, sequence: str) -> torch.Tensor:
        """Return a 1024-dim embedding for a single protein sequence."""
        # Add spaces between amino acids as expected by ProtBERT
        sequence = " ".join(list(sequence))
        # Replace unusual amino acids with X
        sequence = sequence.replace("U", "X").replace("Z", "X").replace("O", "X")

        tokens = self.tokenizer(sequence, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model(**tokens)
            # CLS token as embedding for the whole sequence
            embedding = outputs.last_hidden_state[:, 0, :]

        return embedding.squeeze().cpu().numpy()
