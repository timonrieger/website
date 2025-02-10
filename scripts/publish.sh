#!/usr/bin/env fish

# Check if we're on the hugo branch
set CURRENT_BRANCH (git branch --show-current)
if test "$CURRENT_BRANCH" != "hugo"
    echo "❌ Error: Must be on 'hugo' branch to publish!"
    echo "Current branch: $CURRENT_BRANCH"
    echo "Please switch to the 'hugo' branch first."
    exit 1
end

# Check for .env file
if not test -f ".env"
    echo "❌ Error: .env file not found!"
    echo "Please create a .env file with your READWISE_KEY."
    exit 1
end

# Define variables
set DATE (date +"%Y-%m-%d %H:%M")
set VENV_DIR ".venv"

echo "🚀 Starting Hugo site deployment..."

# Set up virtual environment
echo "🐍 Setting up Python environment..."
if not test -d "$VENV_DIR"
    python3.12 -m venv "$VENV_DIR"
    "$VENV_DIR/bin/pip" install --quiet -r scripts/requirements.txt
end

# Activate virtual environment
source "$VENV_DIR/bin/activate.fish"

# Run Python scripts
echo "⚡ Running preprocessing scripts..."
python3 -m scripts.reads

# Remove virtual environment
rm -rf "$VENV_DIR"

# Build the Hugo site
echo "🏗️ Building site with Hugo..."
hugo --minify --gc --cleanDestinationDir --templateMetrics

# Commit and push changes
echo "📤 Committing and pushing to remotes..."
git commit -a -m "published on $DATE"
git pushcurr

echo "✅ Deployment completed successfully!"