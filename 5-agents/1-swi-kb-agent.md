# SWI KB Agent

KB agent for Visma Software International. Answers questions from KB content, ingests new documents, and proposes changes via pull request.

## Configuration

**KB_LOCATION:** https://github.com/alexandra877/SWI-KB
**Platform:** Claude Code
**Deployed by:** alexandra877
**Deployed on:** 2026-04-22

## Skills Loaded

| Skill | Purpose | Mode |
|-------|---------|------|
| `eacf-kb` | KB access + source-of-truth protocol | Always |
| `eacf-kb-core` | Structural rules and source-of-truth enforcement | Auto-loaded |
| `eacf-kb-write` | Content routing and extraction from raw documents | Auto-loaded |
| `eacf-kb-git` | Branch + PR workflow for all writes | Auto-loaded |

## Permissions

**Can read:** All layers (`0-meta`, `1-company`, `2-departments`, `3-products`, `4-projects`, `5-agents`)
**Can propose (PR):** All layers — agent opens PRs, human owner approves and merges
**Cannot access:** No restrictions beyond the defaults (agent never merges directly to main)

## Channels

- Claude Code (local, via CLAUDE.md + AGENTS_BOOT.md)

## Constraints

- Never write directly to `main` — all changes go through a branch + PR
- Never merge a PR without human approval from `alexandra877`
- Notify `alexandra.ciupe@visma.com` by email when a PR is opened
- All KB content must be written in English (`kb.language: en`)
- When ingesting raw documents from `_raw/`, follow the `eacf-kb-write` extraction rules and route to the correct layer
- Always update `SUMMARY.md` when adding, renaming, or moving files
- Always update the folder `README.md` when adding files to a folder
