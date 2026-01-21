---
date: '2025-12-11T11:52:07+01:00'
draft: false
tags: ['security', 'software']
title: 'Finding Orphan Packages in Homebrew'
url: 'blog/finding-orphan-packages-in-homebrew'
---

Keeping your software up to date is important to stay safe. I recently watched [Hacker - We get you within 5 minutes!](https://www.youtube.com/watch?v=_Zrqpgbb3n0), which talks about security mistakes people and companies make. So keep your software up to date!

<!--more-->

I also only install what I really need to reduce the overall attack surface. That doesn't mean I never install things I'll only use temporarily. But I try to notice when I'm not using something anymore and remove it.

[Homebrew](https://brew.sh) helps me keep track of the programs on my computer. It has a useful command that checks what I have installed. Since I use [fish shell](https://fishshell.com/), the command below is written in fish syntax:

```fish
for pkg in (brew list)
 set deps (brew uses --installed $pkg)
 if test (count $deps) -eq 0
  echo "$pkg is not used by any installed package"
 else
  echo "$pkg is required by: $deps"
 end
end
```

This checks the dependencies between installed programs. It finds "orphan" packages - packages that nothing else needs. You can review it and decide which ones to remove.
Here's what the output might look like:

```txt
ansible is not used by any installed package
brotli is required by: mongosh node
certifi is required by: ansible
cryptography is required by: ansible
docker is not used by any installed package
flac is not used by any installed package
```

> EDIT: Homebrew ships with this out of the box with [`brew autoremove`](https://docs.brew.sh/Manpage#autoremove---dry-run).
