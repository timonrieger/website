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

```bash
./scripts/hugo.sh
```

## Add theme

```bash
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

needed when you reclone your repo (submodules may not get cloned automatically)
```bash
git submodule update --init --recursive 
```

## Update theme

```bash
git submodule update --remote --merge
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
