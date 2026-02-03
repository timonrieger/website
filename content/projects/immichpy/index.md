---
date: '2026-01-31'
draft: false
title: 'Immichpy'
url: 'projects/immichpy'
cover:
  image: "images/cover.png"
weight: 1
---

Immichpy is the stable, typed Python API layer for [Immich](https://immich.app) automation and integrations. It provides a Python client and CLI so you can interact with your Immich server programmatically or from the terminal, with full type safety and async support. The library is auto-generated from the Immich OpenAPI schema and stays in sync with upstream releases.

You can read the [documentation](https://immichpy.timonrieger.de), install it from [PyPI](https://pypi.org/project/immichpy), and view the [source on GitHub](https://github.com/timonrieger/immichpy).

<!--more-->

## Intention

I’ve been working a lot with OpenAPI-related tooling recently: I added OpenAPI descriptions to Immich in a [massive PR](https://github.com/immich-app/immich/pull/25185), maintain multiple OpenAPI-generated clients in [Python](https://github.com/crypticorn-ai/api-client-python/) and [TypeScript](https://github.com/crypticorn-ai/api-client-typescript), and suggested a [client rewrite for the Lichess API](https://github.com/lichess-org/berserk/issues/153) (berserk).

## Timeline

The project started in January 2026, after [setting up my Immich server](/blog/heaven-not-cloud/) and [contributing to Immich](https://github.com/immich-app/immich/pulls/timonrieger).

It was first named ~~immich-python-client~~ (too long), then ~~immich-py~~ - but the package and CLI name [`immich`](https://pypi.org/project/immich) shadowed module names and was ambiguous with the official CLI, so I renamed it to **immichpy** with consistent naming.

I’m currently working towards ecosystem integration. [^1]

## Tech Stack

See the [Credits](https://immichpy.timonrieger.de/info/credits) page for more details.

[^1]: [Journiv](https://github.com/journiv/journiv-app/pull/370), Home Assistant, [immich-folder-album-creator](https://github.com/Salvoxia/immich-folder-album-creator/pull/259)
