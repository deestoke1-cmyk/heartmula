#!/bin/bash

# Colors for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🚀 Starting HeartMuLa One-Click Setup...${NC}"

# 1. Setup Virtual Environment
if [ ! -d "venv" ]; then
    echo "📦 Creating Virtual Environment..."
    python3 -m venv venv
fi

source venv/bin/activate
echo -e "${GREEN}✅ Virtual Environment Active${NC}"

# 2. Install Dependencies
echo "🛠 Installing Python dependencies..."
pip install --upgrade pip
pip install argparse mido

# 3. Configure External Drive
DRIVE_PATH="/Volumes/12121231/heartmula/outputs"
if [ -d "/Volumes/12121231" ]; then
    mkdir -p "$DRIVE_PATH"
    echo -e "${GREEN}✅ Output directory verified on Drive 12121231${NC}"
else
    echo -e "\033[0;31m⚠️  WARNING: Drive '12121231' not found. Ensure it is plugged into your iMac.\033[0m"
fi

# 4. Permissions
chmod +x generate.py setup.sh
echo -e "${GREEN}✨ Setup Complete! ✨${NC}"
echo -e "Run the engine with: ${BLUE}./generate.py --instrumental${NC}"
