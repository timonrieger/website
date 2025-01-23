# Instruction for using Hugo

## Develop

includes drafts in build
```bash
hugo server -D
```
to exclude drafts run
```bash
hugo server
```

## Build

Ideally remove the `public/` and `resource/` folder before building with:

```bash
rm -rf public/
rm -rf resources/
```

```bash
hugo
```

## Add new content
A new blog post
```bash
hugo new blog/TITLE
```

A new project
```bash
hugo new project/NAME
```

A new single page
```bash
hugo new NAME.md
```
