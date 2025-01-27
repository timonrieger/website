---
date: '{{ .Date }}'
lastmod: '{{ .Date }}'
draft: true
tags: []
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
url: '{{ replace .File.ContentBaseName "-" " " | urlize }}'
---
your summary goes here

<!--more-->

your content goes here