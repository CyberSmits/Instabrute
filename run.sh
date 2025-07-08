#!/bin/bash

# 🔗 Step 1: Open YouTube channel for subscription
echo "📺 Opening ethical mind YouTube channel..."
termux-open-url https://youtube.com/@ethical_mind

# ⏳ Optional wait for user to subscribe
sleep 5

# 🟣 Step 2: Start Tor in background
echo "🟣 Starting Tor in background..."
tor -f $HOME/.torrc &

# Wait for Tor to fully start
sleep 8

# 🟢 Step 3: Run Python Tool
echo "🚀 Launching ETHICALMIND Tool..."
python node.py
