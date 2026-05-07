#!/bin/bash

echo "🚀 Starting HeartMuLa One-Click Install..."

# 1. Create Python Virtual Environment
python3 -m venv venv
source venv/bin/activate

# 2. Install Core Dependencies
pip install argparse mido

# 3. Setup External Drive Directories
OUTPUT_DIR="/Volumes/12121231/heartmula/outputs"
if [ -d "/Volumes/12121231" ]; then
    mkdir -p "$OUTPUT_DIR"
    echo "✅ External drive directories created at $OUTPUT_DIR"
else
    echo "⚠️ Warning: Drive '12121231' not found. Please mount it to use the engine."
fi

# 4. Make generate.py executable
chmod +x generate.py

echo "✨ Installation Complete! Run with: ./generate.py --instrumental"
