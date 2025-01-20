---
date: '2025-01-20T12:48:11+01:00'
draft: true
title: 'Learn Hugo'
tags: []
summary: ''
params:
  color: 'red'
  size:
    top: 'large' 
    bottom: 'medium'
cover:
  image: ""
  # can also paste direct link from external site
  # ex. https://i.ibb.co/K0HVPBd/paper-mod-profilemode.png
  alt: "<alt text>"
  caption: "<text>"
  relative: false # To use relative path for cover image, used in hugo Page-bundles
---

## Intro
For applied syntax view [PaperMod demo page](https://adityatelange.github.io/hugo-PaperMod/posts/)

<!-- more -->

To leverage this website even more, you could add [taxonomies](https://discourse.gohugo.io/t/handling-taxonomies-like-a-boss-update/7719)

The following is a example page, which is useful for testing the [Hugo Shortcodes](https://gohugo.io/shortcodes/)

Defining parameters

We found a {{< param "color" >}} shirt. It is {{< param size.top >}} size.

##  Links
see [here](https://gohugo.io/content-management/cross-references/)


## Shortcodes

see [here](https://gohugo.io/shortcodes/)

Code block
{{< highlight python >}} A bunch of code here {{< /highlight >}}

Hidden comment
{{% comment %}} rewrite the paragraph below {{% /comment %}}

Dropdown Details
{{< details summary="See the details" >}}
 - This is a **bold** word.
{{< /details >}}

Image
![Image 1](/images/2.png)

Image with options
{{< figure
  src="/images/1.png"
  alt="A photograph of Zion National Park"
  width=50%
  link="https://www.nps.gov/zion/index.htm"
  caption="Zion National Park"
  class="ma0 w-75"
>}}

X Post
{{< x user="SanDiegoZoo" id="1453110110599868418" >}}

Instagram Post
{{< instagram CxOWiQNP2MO >}}

Gist User
{{< gist user 23932424365401ffa5e9d9810102a477 >}}

Gist File
{{< gist user 23932424365401ffa5e9d9810102a477 list.html >}}

QR Code Web
{{< qr text="https://gohugo.io" />}}

QR Code Tel
{{< qr text="tel:+12065550101" />}}
