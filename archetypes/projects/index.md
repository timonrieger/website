---
date: '{{ .Date }}'
lastmod: '{{ .Date }}'
draft: true
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: 'projects/{{ path.Base (path.Dir .Path) | urlize }}'
summary: ''
cover:
  image: ""
  alt: "<alt text>"
  relative: true
---