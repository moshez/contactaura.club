#!/bin/bash
# Build script for Sphinx documentation
# Uses python -m sphinx for compatibility with Netlify and other build environments

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Building ContactAura RPG Materials documentation...${NC}"

# Clean previous build
if [ -d "_build" ]; then
    echo "Cleaning previous build..."
    rm -rf _build
fi

# Build HTML documentation using python -m sphinx
echo -e "${BLUE}Running Sphinx build...${NC}"
python -m sphinx -b html . _build/html

echo -e "${GREEN}Build complete! Documentation is in _build/html/${NC}"
echo -e "${GREEN}Open _build/html/index.html in your browser to view.${NC}"
