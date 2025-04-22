#!/usr/bin/env fish

# this script is used locally to publish the site

# Check if we're on the hugo branch
set CURRENT_BRANCH (git branch --show-current)
if test "$CURRENT_BRANCH" != "v2"
    echo "❌ Error: Must be on 'v2' branch to publish!"
    echo "Current branch: $CURRENT_BRANCH"
    echo "Please switch to the 'v2' branch first."
    exit 1
end

git add . && git stash

git pull

git stash pop stash@{0}

# Define variables
set DATE (date +"%Y-%m-%d %H:%M")

# Build the Hugo site
echo "🏗️ Building site with Hugo..."
hugo --minify --gc --cleanDestinationDir --templateMetrics

# Commit and push changes
echo "📤 Committing and pushing to remotes..."
git add .
git commit -m "published on $DATE"
git push

echo "✅ Deployment completed successfully!"