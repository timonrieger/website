---
date: '2024-11-25T16:28:47+01:00'
draft: false
title: 'Arkivr'
url: 'projects/arkivr'
cover:
  image: "images/cover.png"
weight: 4
---

Arkivr is an archiving software as a self-hostable web server that allows you to store and organize resources such as links, files and more for easy retrieval.

You can [see my instance](https://arkivr.timonrieger.de) and the [source code on GitHub](https://github.com/timonrieger/arkivr).

## Intention

My colleagues and I have been saving interesting websites, documents and general learning resources in a Discord chat for months. It's easy to add the links or files there, but finding a particular resource was cumbersome. So I quickly set up a minimal version with a simple Flask server and have been using it daily ever since. I really like the concept and my first implementation, so I'm thinking about scaling it from a [multi-page to a single-page application](https://medium.com/swlh/spa-mpa-or-a-hybrid-42fdf6b3415c), adding self-hosting capability with Docker, support files and much more functionality.

## Timeline

I started developing it in November 2024 as a weekend project and have been planning to expand it ever since. However, I haven't yet taken the time to actively work on it.

## Tech Stack

- Backend made with [Flask](https://flask.palletsprojects.com/en/stable/)
- Frontend made with [Jinja](https://jinja.palletsprojects.com/en/stable/) and [TailwindCSS](https://tailwindcss.com/)
