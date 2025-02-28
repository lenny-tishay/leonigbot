#!/data/data/com.termux/files/usr/bin/bash
echo "[LeonigBot] Installing dependencies..."
pip install -r requirements.txt
echo "[LeonigBot] Starting bot..."
python bot.py
