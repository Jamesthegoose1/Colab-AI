#!/bin/bash

# ===== CONFIG =====
NGROK_AUTH_TOKEN="YOUR_NGROK_TOKEN_HERE"
FASTAPI_MODULE="api.fastapi_app:app"
PORT=8000

# ===== INSTALL DEPENDENCIES =====
echo "Installing Python packages..."
python3 -m pip install --upgrade pip
sleep 5
python3 -m pip install fastapi uvicorn nest-asyncio requests beautifulsoup4 ngrok

# ===== CONFIGURE NGROK =====
echo "Configuring ngrok..."
ngrok config add-authtoken add_your_auth_token_here

# ===== CREATE FOLDERS =====
echo "Creating data directories..."
mkdir -p /content/data/datasets
mkdir -p /content/data/outputs

# ===== START FASTAPI =====
echo "Starting FastAPI server..."
nohup uvicorn $FASTAPI_MODULE --host 0.0.0.0 --port $PORT &

# ===== START NGROK TUNNEL =====
echo "Starting ngrok tunnel..."
ngrok http $PORT
