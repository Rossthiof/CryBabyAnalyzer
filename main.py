import os
import re
import csv
from datetime import datetime
from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser
from parser import parse_signal, parse_result
from utils import save_to_csv, analyze_signals

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHAT_ID = int(os.getenv("CHAT_ID"))

SIGNAL_FILE = "signals.csv"

def fetch_telegram_messages():
    all_signals = {}
    with TelegramClient("signal_session", API_ID, API_HASH) as client:
        print("[+] Verbunden mit Telegram...")

        messages = client.iter_messages(PeerUser(CHAT_ID), reverse=True)
        for message in messages:
            if not message.message:
                continue

            text = message.message.strip()
            timestamp = message.date.strftime("%Y-%m-%d %H:%M:%S")

            if "Setup" in text and "SL" in text and "TP" in text:
                signal_data = parse_signal(text)
                if signal_data:
                    setup_id = signal_data["setup_id"]
                    all_signals[setup_id] = {
                        **signal_data,
                        "timestamp": timestamp,
                        "result": "OPEN"
                    }

            elif "Ergebnis für Setup" in text:
                result_data = parse_result(text)
                if result_data and result_data["setup_id"] in all_signals:
                    all_signals[result_data["setup_id"]]["result"] = result_data["result"]

    return list(all_signals.values())

def main():
    print("[+] Starte Nachrichtenauswertung...")
    parsed_signals = fetch_telegram_messages()

    if not parsed_signals:
        print("[-] Keine Signale gefunden.")
        return

    save_to_csv(parsed_signals, SIGNAL_FILE)
    print(f"[✓] Signale gespeichert in {SIGNAL_FILE}")

    analyze_signals(SIGNAL_FILE)

if __name__ == "__main__":
    main()
