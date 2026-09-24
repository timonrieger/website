---
date: '{{ .Date }}'
draft: true
series: ['letters']
tags: ['letters']
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: 'blog/letters/{{ index (last 1 (split (path.Base (path.Dir .Path)) "-")) 0 }}'
---
your summary goes here

<!--more-->

your content goes here
