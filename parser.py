import re

def parse_signal(text):
    try:
        setup_match = re.search(r'Setup (\d+):\s*(.+)\nRichtung:\s*`(\w+)`\nKaufpreis:\s*`([\d.]+)`\nSL:\s*`([\d.]+)`\nTP:\s*`([\d.]+)`', text)
        if not setup_match:
            return None

        return {
            "setup_id": f"{setup_match.group(1)}",
            "setup_name": setup_match.group(2).strip(),
            "direction": setup_match.group(3),
            "entry": float(setup_match.group(4)),
            "sl": float(setup_match.group(5)),
            "tp": float(setup_match.group(6))
        }

    except Exception as e:
        print(f"[!] Fehler beim Parsen von Signal: {e}")
        return None

def parse_result(text):
    try:
        result_match = re.search(r'Ergebnis für Setup (\d+)\n.*?\*\((\w+)\).*?→\s*(TP|SL)', text)
        if not result_match:
            return None

        return {
            "setup_id": result_match.group(1),
            "direction": result_match.group(2),
            "result": result_match.group(3)
        }

    except Exception as e:
        print(f"[!] Fehler beim Parsen von Ergebnis: {e}")
        return None
