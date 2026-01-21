---
title: 'Privacy Policy'
url: 'privacy-policy'
---

## Zero Tracking

- No cookies
- No analytics
- No ads
- No third-party trackers or embeds
- No user related logs
- No IP tracking

## Embeds

I avoid third‑party embeds. If I ever add one (e.g., a video or social post), I use [Hugo's privacy settings](https://gohugo.io/configuration/privacy/) to reduce or disable tracking.

My current configuration:

```yaml
privacy:

  x:
    disabled: false
    enableDNT: true
    simple: false

  instagram:
    disabled: false

  youtube:
    disabled: false
    privacyEnhanced: true

services:
  instagram:
    disableInlineCSS: true
  x:
    disableInlineCSS: true
```

_[Verify source](https://github.com/timonrieger/website/blob/v2/hugo.yaml)_

## Contact

If you email me, I'll use your message only to reply.
