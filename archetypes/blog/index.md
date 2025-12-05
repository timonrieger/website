---
date: '{{ .Date }}'
draft: true
tags: []
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: 'blog/{{ path.Base (path.Dir .Path) | urlize }}'
---
your summary goes here

<!--more-->

your content goes here