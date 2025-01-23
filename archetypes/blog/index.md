---
date: '{{ .Date }}'
lastmod: '{{ .Date }}'
draft: true
tags: []
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: '{{ path.Base (path.Dir .Path) | urlize }}'
summary: ''
---