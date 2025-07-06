#!/bin/bash

echo "🔄 Updating packages..."
pkg update -y

echo "📦 Installing Tor..."
pkg install tor -y

echo "🐍 Installing Python modules..."
pip install -r requirements.txt

echo "✅ All requirements installed."
