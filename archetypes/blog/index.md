---
date: '{{ .Date }}'
lastmod: '{{ .Date }}'
draft: true
tags: []
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: 'blog/{{ path.Base (path.Dir .Path) | urlize }}'
summary: ''
---