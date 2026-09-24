---
date: '{{ .Date }}'
draft: true
series: ['Letters']
tags: ['letters']
verse: true
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: 'blog/letters/{{ index (last 1 (split (path.Base (path.Dir .Path)) "-")) 0 }}'
---

your content goes here
