import csv
import json

def save_polymers_to_csv(polymers, path):
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ["Name", "MolecularWeight", "GlassTransitionTemp", "Density"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for p in polymers:
            writer.writerow(p)

def save_polymers_to_json(polymers, path):
    with open(path, 'w') as jsonfile:
        json.dump(polymers, jsonfile, indent=2)