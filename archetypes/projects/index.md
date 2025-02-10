---
date: '{{ .Date }}'
draft: true
title: '{{ replace (path.Base (path.Dir .Path)) "-" " " | title }}'
url: 'projects/{{ path.Base (path.Dir .Path) | urlize }}'
cover:
  image: "images/cover.png" 
---


## Intention

## Timeline

## Tech Stack