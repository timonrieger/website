---
date: '{{ .Date }}'
draft: true
tags: []
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
url: '{{ replace .File.ContentBaseName "-" " " | url }}'
---
