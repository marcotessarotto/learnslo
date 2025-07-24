from enota2 import enota


def check_duplicates():
    """Verifica l'esistenza di doppioni nella prima colonna (parole slovene)"""
    first_columns = []
    duplicates = []

    # Estrai tutte le tuple dal dizionario
    for unit_name, tuple_list in enota.items():
        for item in tuple_list:
            if isinstance(item, tuple) and len(item) >= 2:
                first_col = item[0]  # Prima colonna (parola slovena)

                if first_col in first_columns:
                    if first_col not in duplicates:
                        duplicates.append(first_col)
                else:
                    first_columns.append(first_col)

    # Mostra i risultati
    if duplicates:
        print(f"🔍 TROVATI {len(duplicates)} DOPPIONI nella prima colonna:")
        print("=" * 50)

        for duplicate in sorted(duplicates):
            print(f"❌ '{duplicate}' appare più volte")

            # Trova tutte le occorrenze
            occurrences = []
            for unit_name, tuple_list in enota.items():
                for i, item in enumerate(tuple_list):
                    if isinstance(item, tuple) and len(item) >= 2 and item[0] == duplicate:
                        occurrences.append((unit_name, i, item))

            print(f"   Occorrenze ({len(occurrences)}):")
            for unit_name, index, full_item in occurrences:
                print(f"     - {unit_name}, posizione {index}: {full_item}")
            print()

    else:
        print("✅ NESSUN DOPPIONE trovato nella prima colonna!")
        print(f"   Totale elementi unici: {len(first_columns)}")


if __name__ == "__main__":
    check_duplicates()