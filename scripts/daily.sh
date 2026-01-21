#!/usr/bin/env fish

# this script is used by the github action to publish parts of the site automatically (see .github/workflows/daily.yml)

# Check if we're on the hugo branch
set CURRENT_BRANCH (git branch --show-current)
if test "$CURRENT_BRANCH" != "main"
    echo "❌ Error: Must be on 'main' branch to publish!"
    echo "Current branch: $CURRENT_BRANCH"
    echo "Please switch to the 'main' branch first."
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

echo "🚀 Starting Hugo site deployment..."

# Run Python scripts
echo "⚡ Running preprocessing scripts..."
python3 -m scripts.reads

git add content/reads.md
git commit -m "published on $DATE"
git push

echo "✅ Deployment completed successfully!"