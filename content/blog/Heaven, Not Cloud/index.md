---
date: '2025-11-30T23:53:29+01:00'
draft: false
tags: ['programming', 'tech']
title: 'Heaven, Not Cloud'
url: 'blog/heaven-not-cloud'
---

I planned it for a while, finally realized it: a own server. It's more than just a server, it's a cloud. And, it's about freedom, ownership and a philosophy. Explaining the why and how and the stack we are running.

<!--more-->

Yes, I finally built my own server. It feels great. I am quite excited about this because:

1. It solves a long standing family pain point
2. You actually own your data
3. It's fun

## The Pain Point

For most people this is not a pain point, I sense however that it will become one:

PHOTOS.

What's the issue here, you wonder?

1. You might not even know where they are.
2. You won't get them out of the cloud again, ever. [^1]
3. You don't have backups.

One day, everything will be lost, because something in that chain breaks: your phone dies or gets stolen, the cloud provider goes down or your account is locked.

All of these concerns weighed heavily in our family discussions. With tens of thousands of photos and videos, plus a few dozen handcrafted movies, you really start to wonder where on earth to store all that data.

I believe in simplicity, but only as long as it gives freedom. Thus, we decided against the cloud, the quick "Get 2 TB cloud storage" offer and the lock-in.

## The Setup

I am a fan of writing things down. It reclaims brain space, makes the stack reproducible and makes the the system independent of a single entity.

So I [documented everything](https://docs.fam.timonrieger.de/). I made it public, so anyone can take a look and benefit from the thoughts I put into the setup.

In short, I run a popular base system Linux distribution, configure it declaratively, run free open containerized software and access it with a private VPN from anywhere in the world.

## How It's Used

We moved all our media to the server and serve it via dedicated software to the "clients", us.

We run [Immich](https://immich.app) for photo and video management,
[Jellyfin](https://jellyfin.org) for movies and music alongside other software. [^2]

Amazing, open and free software, built for people instead of profits. They respect the [_File over app_](https://stephango.com/file-over-app) principle, are lightweight, feature rich and don't lock you in - and, you can contribute to their success yourself directly.

## Balancing Maintenance

When setting up the server I took some time to think about how to design the architecture in a way that I can maintain it with a few minutes per month. I applied that by only installing the bare minimum, defining all configuration explicitly, running docker with versioned images, automating everything and [documenting](https://docs.fam.timonrieger.de/) it.

We will see how much time I actually spend in the long run, but for now I am happy with it.

[^1]: …unless you bring lots of time and patience.

[^2]: A Git instance, mirroring tools, backup software, etc.
