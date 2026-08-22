---
title: Obsidian
created: 2026-08-20
updated: 2026-08-20
type: entity
tags: [tooling, knowledge-base]
sources: [raw/articles/karpathy-llm-wiki.md]
confidence: medium
---

# Obsidian

## What it is

A local-first markdown editor that reads a plain directory of `.md` files as a vault. In the
LLM Wiki pattern it is the **human's read surface** — the agent writes the files, the human
browses them, follows links, and watches the graph. No database or import step; the wiki
directory *is* the vault.

## Why it fits the pattern

- `[[wikilinks]]` render as clickable navigation
- **Graph view** shows the shape of the wiki — hubs, clusters, and orphan pages that
  [[wiki-operations]] lint would otherwise have to find programmatically
- **Dataview** plugin queries YAML frontmatter, turning tags/dates/source counts into dynamic
  tables — the reason frontmatter is worth the overhead
- **Marp** plugin renders markdown as slide decks, so wiki content can become a presentation
  without leaving the format

## Ingest tooling

- **Obsidian Web Clipper** — browser extension converting web articles to markdown, the fastest
  path from a page to `raw/articles/`
- **Local image download** — set Settings → Files and links → "Attachment folder path" to
  `raw/assets/`, then bind "Download attachments for current file" to a hotkey. Keeps images on
  disk instead of behind URLs that rot. Caveat: agents can't read markdown with inline images in
  one pass; read the text first, then view referenced images separately.

## Notes

Everything here is optional. The vault is a git repo of markdown files, so version history,
branching, and collaboration come free regardless of editor. For larger wikis where the index
stops being enough, the source suggests [qmd](https://github.com/tobi/qmd) — local hybrid
BM25/vector search over markdown, available as both CLI and MCP server.

## Related

[[wiki-operations]] · [[compiled-knowledge-base]] · [[andrej-karpathy]]
