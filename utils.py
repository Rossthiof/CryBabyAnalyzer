import csv
import pandas as pd

def save_to_csv(data, filename):
    if not data:
        print("[-] Keine Daten zum Speichern.")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def analyze_signals(signal_file):
    try:
        df = pd.read_csv(signal_file)

        grouped = df.groupby("setup_id").agg({
            "setup_name": "first",
            "direction": "first",
            "result": lambda x: (x == "TP").sum() / len(x),
            "entry": "count"
        }).rename(columns={"result": "win_rate", "entry": "trades"})

        grouped["win_rate"] = (grouped["win_rate"] * 100).round(2)
        grouped = grouped.sort_values(by="win_rate", ascending=False)

        grouped.to_csv("setup_stats.csv")
        print("[✓] Analyse abgeschlossen: setup_stats.csv wurde erstellt.")
    except Exception as e:
        print(f"[!] Fehler bei Analyse: {e}")
