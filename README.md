# 🏅 ChemSport Lab - Chemistry of Sport

A sports-themed cheminformatics virtual laboratory built with Python, Streamlit and RDKit.

## Features
- 90+ sport-related molecules in 10 categories (fuels, supplements, hydration, anti-doping watchlist,
  equipment polymers, motorsport fuels, breath & air ...)
- 2D and interactive 3D structures from SMILES
- Molecule Datasheet: melting point, boiling point, density, state, solubility,
  H-bond donors/acceptors, TPSA, LogP, Lipinski/Veber checklist, QED, functional groups
- Compare molecules side by side with melting/boiling-point charts
- Coach ChemBot: an AI assistant for questions (needs an API key, see below)
- PDF reports, assessment and structure-property analysis

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Check the molecule library
```bash
python test_molecules.py
```

## Turning on the AI coach
Add an API key under **Settings → Secrets** in Streamlit Cloud.
See `.streamlit/secrets.toml.example`. Never commit a real key.

## Data note
Melting and boiling points are approximate literature values stored in `molecule_data.py`
(RDKit cannot calculate them). Verify important values on PubChem or the CRC Handbook.

## Customize
Edit your name and college at the top of `app.py` (section "YOUR DETAILS").
Add molecules in `molecules.py`.
