---
date: '2025-01-25T16:35:02+01:00'
draft: false
title: 'Blog Boiler Templates'
url: 'projects/blog-boiler-templates'
cover:
  image: "images/cover.png" 
weight: 2
---
Blog Boiler is a set of two templates to get started with a free, easy and predesigned blog template that will help you get started blogging in minutes.

Before I switched my blog to Hugo I had been using the Pro template myself. You can find more detailed information about usage on Github, [Pro](https://github.com/timonrieger/blog-boiler-pro) and [Lite](https://github.com/timonrieger/blog-boiler-lite) version

## Intention

I started this project during the 100 Days of Code challenge. It was a long-term project spanning several days, implementing various features over time. While the design itself is not my own, I was drawn to the idea of having a self-hosted space where I could write about my ideas and thoughts. I continued developing it over time, adapting it to my needs.
Initially, it used JSON storage via [npoint](https://npoint.io/) for blog posts, which is still being used in the Lite version. Later, I enhanced the Pro version by adding a PostgreSQL database for blog posts to enable basic CRUD operations, along with features like tags, user management, and comments. I maintained my own instance of the Pro version running alongside the Lite and Pro templates for a while. Recently, I migrated the blog to Hugo and have since discontinued development and usage of this project.

## Timeline

While I started the project during the 100 Days of Code challenge, I continued working on it over a longer period of time in private. In January 2025 I decided to make both templates public and open source. Since then it is not actively maintained anymore.

## Tech Stack
- Backend made with [Flask](https://flask.palletsprojects.com/en/stable/)
- Frontend made with [Jinja](https://jinja.palletsprojects.com/en/stable/) and [Start Bootstrap](https://startbootstrap.com/theme/clean-blog)