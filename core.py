import csv
import json

def load_polymers(csv_file='data/polymer_data.csv'):
    polymers = []
    try:
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert numeric fields
                polymers.append({
                    "Name": row["Name"],
                    "MolecularWeight": float(row["MolecularWeight"]),
                    "GlassTransitionTemp": float(row["GlassTransitionTemp"]),
                    "Density": float(row["Density"]),
                })
    except FileNotFoundError:
        print(f"Warning: {csv_file} not found, starting with empty dataset.")
    return polymers

def save_polymers_to_csv(polymers, csv_file='data/polymer_data.csv'):
    with open(csv_file, 'w', newline='') as f:
        fieldnames = ["Name", "MolecularWeight", "GlassTransitionTemp", "Density"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in polymers:
            writer.writerow(p)

def save_polymers_to_json(polymers, json_file='data/polymer_data.json'):
    with open(json_file, 'w') as f:
        json.dump(polymers, f, indent=2)

def filter_polymers(polymers, min_mw=None, max_mw=None,
                    min_tg=None, max_tg=None,
                    min_density=None, max_density=None):
    filtered = []
    for p in polymers:
        if min_mw is not None and p["MolecularWeight"] < min_mw:
            continue
        if max_mw is not None and p["MolecularWeight"] > max_mw:
            continue
        if min_tg is not None and p["GlassTransitionTemp"] < min_tg:
            continue
        if max_tg is not None and p["GlassTransitionTemp"] > max_tg:
            continue
        if min_density is not None and p["Density"] < min_density:
            continue
        if max_density is not None and p["Density"] > max_density:
            continue
        filtered.append(p)
    return filtered
