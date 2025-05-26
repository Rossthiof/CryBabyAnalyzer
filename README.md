# 🧠 CryptoBabylonAnalyzer

Ein Tool zur Analyse von Telegram-Signalen, die durch einen Trading-Bot wie CryptoBabylon gesendet wurden.  
Liest Telegram-Nachrichten, speichert Signale und erstellt eine Auswertung pro Setup (z. B. Winrate, Trefferquote, Performance).

---

## 🚀 Funktionen

- Verbindet sich mit deinem Telegram-Konto über `Telethon`
- Erkennt automatisch gesendete Signale & Ergebnisse (TP/SL)
- Speichert alle Daten in `signals.csv`
- Erstellt `setup_stats.csv` mit Erfolgsanalyse
- Railway-ready mit `.env` Support

---

## 🔧 Installation

```bash
git clone https://github.com/dein-benutzername/CryptoBabylonAnalyzer.git
cd CryptoBabylonAnalyzer
pip install -r requirements.txt
