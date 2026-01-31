#!/bin/bash

# Cloudflare Worker Deployment Script
# This script automates the deployment of the Bhagavad Gita OpenAI API proxy worker

set -e  # Exit on error

echo "=========================================="
echo "Cloudflare Worker Deployment"
echo "=========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if wrangler is installed
echo "Checking prerequisites..."
if ! command -v wrangler &> /dev/null; then
    echo -e "${RED}Error: Wrangler CLI is not installed${NC}"
    echo ""
    echo "Install it with:"
    echo "  npm install -g wrangler"
    echo ""
    exit 1
fi

echo -e "${GREEN}✓ Wrangler is installed${NC}"
WRANGLER_VERSION=$(wrangler --version)
echo "  Version: $WRANGLER_VERSION"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${RED}Error: .env file not found${NC}"
    echo "Please create a .env file with your OPENAI_API_KEY"
    exit 1
fi

# Load environment variables
source .env

if [ -z "$OPENAI_API_KEY" ]; then
    echo -e "${RED}Error: OPENAI_API_KEY not found in .env file${NC}"
    exit 1
fi

echo -e "${GREEN}✓ OpenAI API key loaded from .env${NC}"
echo ""

# Step 1: Login to Cloudflare
echo -e "${BLUE}Step 1: Checking Cloudflare authentication${NC}"
echo ""

if wrangler whoami &> /dev/null; then
    echo -e "${GREEN}✓ Already logged in to Cloudflare${NC}"
    wrangler whoami
else
    echo -e "${YELLOW}Not logged in. Opening browser for authentication...${NC}"
    wrangler login
fi
echo ""

# Step 2: Set OpenAI API Key as secret
echo -e "${BLUE}Step 2: Setting OpenAI API key as Cloudflare secret${NC}"
echo ""

# Check if secret already exists
echo "Checking if OPENAI_API_KEY secret exists..."
if wrangler secret list 2>/dev/null | grep -q "OPENAI_API_KEY"; then
    echo -e "${YELLOW}OPENAI_API_KEY secret already exists${NC}"
    read -p "Do you want to update it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "$OPENAI_API_KEY" | wrangler secret put OPENAI_API_KEY
        echo -e "${GREEN}✓ Secret updated${NC}"
    else
        echo "Skipping secret update"
    fi
else
    echo "Setting OPENAI_API_KEY secret..."
    echo "$OPENAI_API_KEY" | wrangler secret put OPENAI_API_KEY
    echo -e "${GREEN}✓ Secret set${NC}"
fi
echo ""

# Step 3: Deploy the worker
echo -e "${BLUE}Step 3: Deploying worker to Cloudflare${NC}"
echo ""

echo "Deploying bhagavad-gita-api worker..."
DEPLOY_OUTPUT=$(wrangler deploy 2>&1)
echo "$DEPLOY_OUTPUT"
echo ""

# Extract worker URL from deployment output
WORKER_URL=$(echo "$DEPLOY_OUTPUT" | grep -o 'https://[^[:space:]]*\.workers\.dev' | head -1)

if [ -z "$WORKER_URL" ]; then
    echo -e "${RED}Warning: Could not extract worker URL from deployment output${NC}"
    echo "Please check the output above for the worker URL"
    echo ""
    echo "It should look like: https://bhagavad-gita-api.your-subdomain.workers.dev"
    echo ""
    read -p "Please enter your worker URL: " WORKER_URL
fi

echo ""
echo "=========================================="
echo -e "${GREEN}✓ Deployment successful!${NC}"
echo "=========================================="
echo ""
echo "Worker URL: ${GREEN}$WORKER_URL${NC}"
echo ""

# Step 4: Update guidance.js with worker URL
echo -e "${BLUE}Step 4: Updating guidance.js with worker URL${NC}"
echo ""

GUIDANCE_JS="assets/js/guidance.js"

if [ -f "$GUIDANCE_JS" ]; then
    # Check current WORKER_URL value
    CURRENT_URL=$(grep "const WORKER_URL = " "$GUIDANCE_JS" | sed -E "s/.*'([^']*)'.*/\1/")

    if [ "$CURRENT_URL" = "$WORKER_URL" ]; then
        echo -e "${GREEN}✓ guidance.js already has the correct worker URL${NC}"
    else
        echo "Current URL in guidance.js: $CURRENT_URL"
        echo "New URL: $WORKER_URL"
        echo ""
        read -p "Update guidance.js with new worker URL? (Y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            # Backup original file
            cp "$GUIDANCE_JS" "$GUIDANCE_JS.backup"

            # Update WORKER_URL
            sed -i.tmp "s|const WORKER_URL = '.*';|const WORKER_URL = '$WORKER_URL';|g" "$GUIDANCE_JS"
            rm "$GUIDANCE_JS.tmp"

            echo -e "${GREEN}✓ Updated guidance.js${NC}"
            echo ""

            # Commit changes
            read -p "Commit and push changes to GitHub? (Y/n): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Nn]$ ]]; then
                git add "$GUIDANCE_JS"
                git commit -m "Configure Cloudflare Worker URL for spiritual guidance"
                git push
                echo -e "${GREEN}✓ Changes pushed to GitHub${NC}"
            fi
        fi
    fi
else
    echo -e "${RED}Error: $GUIDANCE_JS not found${NC}"
fi

echo ""
echo "=========================================="
echo -e "${GREEN}Setup Complete!${NC}"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Wait for GitHub Actions to deploy (1-2 minutes)"
echo "2. Visit: https://sanatan-learnings.github.io/bhagavad-gita/guidance.html"
echo "3. Test the spiritual guidance feature (no API key needed!)"
echo ""
echo "Monitoring:"
echo "- Cloudflare Dashboard: https://dash.cloudflare.com/"
echo "- OpenAI Usage: https://platform.openai.com/usage"
echo ""
echo "Your worker URL: ${GREEN}$WORKER_URL${NC}"
echo ""
