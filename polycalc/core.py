import csv

def load_polymers(filepath):
    polymers = []
    try:
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                polymers.append({
                    "Name": row["Name"],
                    "MolecularWeight": float(row["MolecularWeight"]),
                    "GlassTransitionTemp": float(row["GlassTransitionTemp"]),
                    "Density": float(row["Density"]),
                })
    except Exception as e:
        print(f"Error loading data: {e}")
    return polymers

def filter_polymers(polymers, mw_range=None, tg_range=None, density_range=None):
    result = []
    for p in polymers:
        if mw_range and not (mw_range[0] <= p["MolecularWeight"] <= mw_range[1]):
            continue
        if tg_range and not (tg_range[0] <= p["GlassTransitionTemp"] <= tg_range[1]):
            continue
        if density_range and not (density_range[0] <= p["Density"] <= density_range[1]):
            continue
        result.append(p)
    return result
