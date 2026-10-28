"""
Run:  python test_molecules.py      (needs:  pip install rdkit)

Checks that every SMILES is valid, no name is duplicated, and that the
melting/boiling-point table and sports notes only refer to real molecules.
"""
from rdkit import Chem
from molecules import MOLECULE_LIBRARY
from molecule_data import EXPERIMENTAL, MOLECULE_NOTES

problems, seen, total = [], set(), 0
for category, items in MOLECULE_LIBRARY.items():
    for name, smiles in items.items():
        total += 1
        if name in seen:
            problems.append(f"DUPLICATE NAME: {name}")
        seen.add(name)
        if Chem.MolFromSmiles(smiles) is None:
            problems.append(f"INVALID SMILES: {name} -> {smiles}")

for name in EXPERIMENTAL:
    if name not in seen:
        problems.append(f"molecule_data.EXPERIMENTAL has an unknown molecule: {name}")
for name in MOLECULE_NOTES:
    if name not in seen:
        problems.append(f"molecule_data.MOLECULE_NOTES has an unknown molecule: {name}")

print(f"Checked {total} molecules in {len(MOLECULE_LIBRARY)} categories")
print(f"Melting/boiling data for {len(EXPERIMENTAL)} molecules, notes for {len(MOLECULE_NOTES)}")
for p in problems:
    print("  ❌", p)
print("✅ All good" if not problems else f"{len(problems)} problem(s) found")
