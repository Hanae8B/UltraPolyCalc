from core import load_polymers, save_polymers_to_csv, save_polymers_to_json, filter_polymers

def input_float(prompt):
    while True:
        val = input(prompt).strip()
        if val == '':
            return None
        try:
            return float(val)
        except ValueError:
            print("Invalid number, try again.")

def main():
    polymers = load_polymers()

    while True:
        print("\nUltraPolyCalc CLI")
        print("=================")
        print("1. List all polymers")
        print("2. View polymer details")
        print("3. Filter polymers by property range")
        print("4. Add new polymer data")
        print("5. Export polymer data")
        print("6. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            print("\nAll Polymers:")
            for p in polymers:
                print(f"- {p['Name']}")
        elif choice == '2':
            name = input("Enter polymer name: ").strip()
            found = next((p for p in polymers if p['Name'].lower() == name.lower()), None)
            if found:
                print(f"Details for {found['Name']}:")
                print(f"  Molecular Weight: {found['MolecularWeight']} g/mol")
                print(f"  Glass Transition Temp: {found['GlassTransitionTemp']} °C")
                print(f"  Density: {found['Density']} g/cm³")
            else:
                print("Polymer not found.")
        elif choice == '3':
            print("Enter property ranges to filter (leave blank to skip):")
            min_mw = input_float("Min Molecular Weight (g/mol): ")
            max_mw = input_float("Max Molecular Weight (g/mol): ")
            min_tg = input_float("Min Glass Transition Temp (°C): ")
            max_tg = input_float("Max Glass Transition Temp (°C): ")
            min_density = input_float("Min Density (g/cm³): ")
            max_density = input_float("Max Density (g/cm³): ")

            filtered = filter_polymers(polymers,
                                       min_mw=min_mw, max_mw=max_mw,
                                       min_tg=min_tg, max_tg=max_tg,
                                       min_density=min_density, max_density=max_density)

            if filtered:
                print("\nFiltered Polymers:")
                for p in filtered:
                    print(f"- {p['Name']}: MW={p['MolecularWeight']} g/mol, Tg={p['GlassTransitionTemp']} °C, Density={p['Density']} g/cm³")
            else:
                print("No polymers matched the filter criteria.")
        elif choice == '4':
            print("Add New Polymer Data")
            name = input("Name: ").strip()
            mw = input_float("Molecular Weight (g/mol): ")
            tg = input_float("Glass Transition Temp (°C): ")
            density = input_float("Density (g/cm³): ")

            if None in (mw, tg, density) or name == '':
                print("All fields are required. Polymer not added.")
            else:
                new_polymer = {
                    "Name": name,
                    "MolecularWeight": mw,
                    "GlassTransitionTemp": tg,
                    "Density": density,
                }
                polymers.append(new_polymer)
                save_polymers_to_csv(polymers)
                print(f"Polymer '{name}' added successfully.")
        elif choice == '5':
            save_polymers_to_json(polymers)
            print("Polymer data exported to JSON file.")
        elif choice == '6':
            print("Exiting UltraPolyCalc.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()