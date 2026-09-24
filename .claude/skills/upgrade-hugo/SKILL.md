---
name: upgrade-hugo
description: Upgrades Hugo for this site — bumps both version pins, clears deprecations, re-checks hugo.yaml against upstream config changes, and proves the built output changed only where intended. Use when updating Hugo or the PaperMod submodule, when a build prints deprecation warnings, or when checking whether hugo.yaml still matches current upstream keys.
---
# Upgrade Hugo

The bar: output-neutral, except for changes you decide on and report.

## Steps

1. Baseline build on the current pin, before any edit: `mise exec -- hugo --gc --minify -d "$TMP/before"`. Keep its warnings.
2. Branch, then bump both pins — `mise.toml` `[tools] hugo` and `vercel.json` `build.env.HUGO_VERSION` — and `mise install hugo`.
3. Release notes for every version spanned: `curl -s "https://api.github.com/repos/gohugoio/hugo/releases?per_page=5"`. Rule each breaking change in or out for this project.
4. Fix the deprecations coming from `hugo.yaml` and `layouts/`; grep the warned key or method for its source. Hits under `themes/PaperMod/` are upstream's — report them instead of forking a theme file.
5. Theme submodule: `git -C themes/PaperMod fetch --depth=1 origin master`, compare `FETCH_HEAD` with `HEAD`, `mise run theme:update` to move it. Then re-diff each forked file in `layouts/` against its upstream twin and keep only the deltas you still want.
6. Audit `hugo.yaml` key by key against `raw.githubusercontent.com/gohugoio/hugoDocs/master/content/en/configuration/{all,imaging,markup,minify,privacy,services,module}.md`. Three kinds of dead key: dropped by Hugo, no longer read by the theme (`grep -rl "<param>" themes/PaperMod/layouts layouts`), or one of Hugo's own settings misfiled under `params:`.
7. Diff the builds: `.claude/skills/upgrade-hugo/compare-builds.py "$TMP/before" "$TMP/after"`. Name a cause for every group it prints.
8. Fingerprint two fresh builds: `(cd DIR && find . -type f | sort | xargs shasum | shasum)`. A mismatch means build-order-dependent output — usually a taxonomy term authored with mixed casing across posts.
9. Harvest the release for features that retire forked code (`Pages.IndexOf` replaced a hand-rolled loop over a series). Verify each swap by diffing the rendered fragment, with a throwaway fixture when live content doesn't exercise the path.
10. Focused commits, one concern each, lowercase imperative subjects.

## Project facts

- `hugo` on `PATH` may be the previous install; `mise exec -- hugo` runs the pinned one.
- `minify.minifyOutput: true` means even a bare `hugo` writes minified HTML with unquoted attributes (`<nav class=paginav>`) — match that in greps.
- `mise run dev` leaves a `hugo server` writing into `public/`, so comparison builds go to `-d` scratch dirs.
- `HUGO_CAPITALIZELISTTITLES=true mise exec -- hugo -d "$TMP/x"` renders a what-if build without editing config.
- The user edits this repo while you work: `git commit -- <paths>` and `uvx prek run --files <paths>` touch only your files.

## Report

- Versions moved, and the pins carrying them.
- Keys renamed; dead keys dropped, with what made each dead.
- Workarounds retired, and the feature that retired each.
- Visible output changes, affected page count, and the one-line revert.
- Warnings still printing, whose they are, what would silence them.
- What you found and deliberately left alone.
