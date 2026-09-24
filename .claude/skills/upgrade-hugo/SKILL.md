---
name: upgrade-hugo
description: Upgrades Hugo for this site — bumps both version pins, clears deprecations, re-checks hugo.yaml against upstream config changes, and proves the built output changed only where intended. Use when updating Hugo or the PaperMod submodule, when a build prints deprecation warnings, or when checking whether hugo.yaml still matches current upstream keys.
---
# Upgrade Hugo

Bumping the pin is one line. The work is proving the site renders what it rendered before, and folding in what upstream renamed, deprecated, or now does better than the local workaround.

The bar: **output-neutral**, except for changes you decided on and report. Every surviving diff between the old build and the new one is accounted for or undone.

## Steps

1. **Baseline first.** On the *current* pin, before editing anything: `mise exec -- hugo --gc --minify -d "$TMP/before"`. Every later claim about what changed is a diff against this tree, so it has to exist before the bump. Done when the tree is there and its warnings are written down.

2. **Branch, then bump both pins.** `mise.toml` `[tools] hugo` *and* `vercel.json` `build.env.HUGO_VERSION` — `renovate.json` keeps the pair in one group, and moving one alone ships a local/Vercel skew. `mise install hugo`. Done when `mise exec -- hugo version` prints the target.

3. **Read the release notes for every version spanned**, not only the newest: `curl -s "https://api.github.com/repos/gohugoio/hugo/releases?per_page=5"`. Check each breaking change against this project specifically — glob semantics in module mounts and cascade targets, security defaults, template lookup, image encoding. Done when every noted change is acted on or ruled irrelevant with a reason.

4. **Clear the deprecations that come from project files.** Config-key warnings print before `Start building sites`, template warnings after. Grep the warned-about method or key to find its source: `hugo.yaml` and `layouts/` are yours to fix; a hit under `themes/PaperMod/` is upstream's, so confirm the submodule is already current (step 5) and report it rather than forking a theme file for a warning. Done when every remaining warning traces to the theme.

5. **Confirm the theme submodule is current.** `git -C themes/PaperMod fetch --depth=1 origin master`, then compare `FETCH_HEAD` with `HEAD`; `mise run theme:update` moves it. A theme bump usually lands with the Hugo bump, and PaperMod tracks Hugo's template-layout renames (`layouts/partials/` → `layouts/_partials/`, `_default/single.html` → `single.html`), so re-diff each forked file in `layouts/` against its upstream twin and shrink the fork to the deltas you still want.

6. **Audit hugo.yaml key by key against upstream docs.** Root keys and deprecations live in `raw.githubusercontent.com/gohugoio/hugoDocs/master/content/en/configuration/{all,imaging,markup,minify,privacy,services,module}.md`. Two classes of **dead key** hide from the build because neither Hugo nor the theme reads them: a key Hugo dropped, and a theme param the theme stopped using — `grep -rl "<param>" themes/PaperMod/layouts layouts` returning nothing settles the second. A param sitting in the wrong scope is the third: Hugo's own settings belong at root, and `params:` swallows them silently. Done when every key is either current-and-read or gone.

7. **Diff the two builds.** Build again into `"$TMP/after"`, then `./.claude/skills/upgrade-hugo/compare-builds.py "$TMP/before" "$TMP/after"`. It compares image bytes as content hashes (an imaging-config change renames every `_hu_<hash>` file without touching a pixel) and groups text diffs by shape, so a site-wide edit reads as one entry. Done when every group has a cause you can name.

8. **Build twice and compare fingerprints:** `(cd DIR && find . -type f | sort | xargs shasum | shasum)` on two fresh builds. A mismatch means build-order-dependent output — most likely a taxonomy term authored with mixed casing across posts, where the rendered name is whichever page Hugo reached first. Fix the frontmatter. Done when two consecutive builds fingerprint identically.

9. **Harvest the new release for workarounds it retires.** Read the release's new template methods and config options against the forked files in `layouts/` — this is where a hand-rolled loop collapses into one call (`Pages.IndexOf` replaced a manual permalink-matching loop over a series). Verify each swap by diffing the rendered fragment, and when live content doesn't exercise the path, author a throwaway fixture that does (the series nav needs two entries in one series) and delete it after. Done when the rendered fragment is identical and the fixture is gone.

10. **Commit in focused commits, one concern each**, matching the repo's lowercase imperative subjects (`update hugo to 0.166.0`, `modernize imaging config`). Then report (below).

## Project facts

- `hugo` on `PATH` may still be the previous mise install; `mise exec -- hugo` runs the pinned one.
- `hugo.yaml` sets `minify.minifyOutput: true`, so even a bare `hugo` writes minified HTML — attributes come out unquoted (`<nav class=paginav>`), which is what greps and regexes have to match.
- `mise run dev` leaves a `hugo server` writing into `public/`, which is why comparison builds go to `-d` scratch dirs; a `rm -rf public` can also fail mid-serve.
- An env override renders a what-if build with no edit to config: `HUGO_CAPITALIZELISTTITLES=true mise exec -- hugo -d "$TMP/x"`. Good for isolating one setting's effect on output.
- The user edits this repo while you work. Stage nothing wholesale: `git commit -- <paths>` names your files and leaves theirs, and `uvx prek run --files <paths>` lints yours where `--all-files` would rewrite theirs.

## Report

Close with what a maintainer cannot see from the diff:

- Versions moved, and the pins that carry them.
- Config keys renamed, and dead keys dropped — with what made each one dead.
- Workarounds retired, and the new feature that retired each.
- Visible output changes, with the count of affected pages and the one-line revert.
- Warnings still printing, whose they are, and what would silence them.
- Anything you found but deliberately left alone, so the call stays theirs.
