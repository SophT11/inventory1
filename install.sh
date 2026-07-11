#!/bin/bash

set -e

echo "Checking Docker..."

if ! command -v docker >/dev/null 2>&1; then
    echo "Installing Docker..."
    sudo apt update
    sudo apt install -y docker.io docker-compose-v2
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -aG docker $USER

    echo ""
    echo "Docker installed."
    echo "Please log out and log back in, then run ./install.sh again."
    exit 0
fi

docker compose up --build -d
docker compose ps01~#!/bin/bash

set -e

echo "Checking Docker..."

if ! command -v docker >/dev/null 2>&1; then
    echo "Installing Docker..."
    sudo apt update
    sudo apt install -y docker.io docker-compose-v2
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo usermod -aG docker $USER

    echo ""
    echo "Docker installed."
    echo "Please log out and log back in, then run ./install.sh again."
    exit 0
fi

docker compose up --build -d
docker compose ps
