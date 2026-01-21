---
date: '2025-10-06T13:37:23+02:00'
draft: false
tags: ['programming']
title: 'Installing Mac Apps With Homebrew'
url: 'blog/installing-mac-apps-with-homebrew'
---
This quick guide shows how to install Mac apps with Homebrew Casks and automate App Store installs using the `mas` CLI.

Homebrew makes it easy to search, inspect, and install third‑party apps, while `mas` brings similar convenience for Mac App Store apps so you can script and standardize your setup.

<!--more-->

<hr>

## Prerequisites

[Install Homebrew](https://brew.sh) if not already installed.

## Using Homebrew Casks

Casks are Homebrew packages for installing macOS applications. To browse the full directory and read explanations, use the [Homebrew Casks directory](https://formulae.brew.sh/cask/) or run:

```bash
brew search chatgpt
```

To get information about an app:

```bash
brew info minecraft
```

To install a cask, use the `--cask` flag, otherwise it will try to install the CLI tool:

```bash
brew install --cask whatsapp
```

## Installing App Store Apps

Some apps aren't available as Casks in Homebrew. For example:

```bash
brew search goodnotes
```

...returns no Goodnotes results.

Goodnotes' website indicates the Mac app is only available via the Mac App Store. To install App Store apps from the command line, use the `mas` CLI.

### mas - Mac App Store CLI

You can install `mas` using brew:

```bash
brew install mas
```

Then to download Goodnotes, use its ID:

```bash
mas install 1444383602
```

### Finding the ID

Open the app in the Mac App Store and click the Share button on the app's page. Copy the link and extract the numeric ID from the URL path.
