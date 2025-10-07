## MBP_PREDICTOR

Microtubule-Binding Proteins (MBPs) play a critical role in stabilizing and regulating microtubule dynamics, influencing key cellular processes such as division, transport, and signaling. This project - MBP_PREDICTOR - presents a machine learning-based approach for the classification of MBPs and non-MBPs using protein sequence-derived features. The model integrates physicochemical descriptors such as amino acid composition, charge distribution, hydrophobicity, isoelectric point, and motif presence, along with advanced embedding-based representations from protein language models.

A series of classifiers were trained and optimized through hyperparameter tuning to achieve robust predictive performance. The final system outputs the probability of a given protein being an MBP, enabling efficient large-scale screening of candidate sequences for biological or therapeutic research.

---

### Quick Start (Colab GUI)

The easiest way to test this project is to run the GUI notebook on Google Colab.

1. Open Google Colab and upload the GUI/GUI.ipynb notebook (or open it directly from GitHub).
2. If running from GitHub, you can clone the repo inside Colab:
`ash
!git clone https://github.com/Sreesj/MBP_PREDICTOR.git
%cd MBP_PREDICTOR
`
3. Install dependencies (if required in your Colab session):
`ash
%pip install -r requirements.txt
`
4. Open and run the notebook cells in GUI/GUI.ipynb to launch the interactive interface.
5. Upload or paste your protein sequence(s) as instructed by the GUI and obtain MBP probability predictions.

Notes:
- Trained model artifacts are provided in TRAINED_MODELS/ and will be loaded by the GUI notebook.
- The repository intentionally excludes large raw data and CSV files from version control.

---

### Features and Methodology

- Physicochemical sequence features: amino acid composition, charge distribution, hydrophobicity, isoelectric point, and motif presence.
- Embedding-based representations from protein language models.
- Multiple classifiers trained with hyperparameter tuning; final predictor outputs MBP probability.

---

### Project Structure

`	ext
MBP_PREDICTOR/
â”œâ”€ GUI/
â”‚  â””â”€ GUI.ipynb                # Colab-friendly GUI to run predictions
â”œâ”€ src/                        # Feature extraction and utilities
â”‚  â”œâ”€ extract_all_features.py
â”‚  â”œâ”€ feature_aac.py
â”‚  â”œâ”€ feature_charge.py
â”‚  â”œâ”€ feature_ctd.py
â”‚  â”œâ”€ feature_embeddings.py
â”‚  â”œâ”€ feature_hydrophobicity.py
â”‚  â”œâ”€ feature_motif.py
â”‚  â”œâ”€ feature_physicochemical.py
â”‚  â”œâ”€ feature_pi.py
â”‚  â””â”€ utils.py
â”œâ”€ TRAINED_MODELS/
â”‚  â”œâ”€ LightGBM_91.22.pkl
â”‚  â””â”€ LightGBM_92.pkl
â”œâ”€ notebooks/                  # Data prep, feature exploration, training
â”‚  â”œâ”€ feature_extraction.ipynb
â”‚  â”œâ”€ feature_visualization.ipynb
â”‚  â”œâ”€ cleaning_validation.ipynb
â”‚  â”œâ”€ model_training.ipynb
â”‚  â””â”€ model_training_2.ipynb
â”œâ”€ feature_importance_analysis/
â”‚  â””â”€ feature_importance_analysis.ipynb
â”œâ”€ requirements.txt
â””â”€ README.md
`

---

### Local Development (optional)

Although Colab is the recommended path for quick testing, you can also run locally:

`ash
# Clone the repository
git clone https://github.com/Sreesj/MBP_PREDICTOR.git
cd MBP_PREDICTOR

# Create a virtual environment (optional but recommended)
python -m venv .venv
. .venv/Scripts/activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter and open GUI/GUI.ipynb
jupyter notebook
`

---

### Data Policy

- Large raw datasets and CSV files are excluded from version control to keep the repository lightweight.
- If you need to reproduce training or feature extraction workflows, prepare your datasets locally and update the notebook paths accordingly.

---

### Citation

If you use MBP_PREDICTOR in your research, please cite this repository:

`	ext
Sreejith S. (2025). MBP_PREDICTOR: Machine learning-based microtubule-binding protein prediction.
GitHub repository: https://github.com/Sreesj/MBP_PREDICTOR
`

---

### License

TBD. If you plan to release this under a specific license, add a LICENSE file and update this section.

---

### Contact

For questions or suggestions, please open an issue or reach out via the repository.
