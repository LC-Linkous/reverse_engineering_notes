# Contributing to reverse_engineering_notes

Thanks for your interest in improving these notes. This repository is the public half of the documentation for an undergraduate reverse-engineering elective. It is an educational **tools-and-methods** reference — not a collection of attacks — and contributions are welcome as long as they keep that character. As this is part of a collection educational materials, some contributions may not be accepted immediately or may need adjustments; this does not indicate a quality or legal issue. 


By contributing, you also agree to the [Code of Conduct](CODE_OF_CONDUCT.md).

## What fits here

- Corrections: typos, broken links, tools that no longer exist, inaccurate technical claims.
- New tools or resources for the tables and reading lists, with a short, neutral description.
- Clearer explanations, diagrams, or examples for existing topics.
- Demo code that shows *tool usage* on devices you own or signals you may legally receive.
- Improvements to the companion reference material in `docs/`.

## What does not fit here

To keep this usable in an educational setting, we do **not** accept:

- Working exploits, malware, or payloads (including "proof-of-concept" attack code).
- Material whose main purpose is to attack systems, networks, or devices the reader does not own or have explicit permission to test.
- Instructions or tools for cloning real access credentials or IDs (student cards, badges, keys, etc.).
- Anything that facilitates illegal activity — including attempts to reframe the above to slip past this rule.

When in doubt, open an issue and ask before writing it. See the [Legal & Ethics](docs/SUPPLEMENTARY_NOTES.md#legal--ethics) notes for the framing this project follows. Nothing here is legal advice.

## Licensing of contributions

This repository is dual-licensed (see the README [License](README.md#license) section):

- **Documentation and notes** (Markdown, tables, diagrams) → **CC-BY-SA-4.0**
- **Code** (anything under `src/`) → **GPL-2.0**

By submitting a contribution, you agree it will be licensed under whichever of the two applies to the type of content, and that you have the right to contribute it.

## How to contribute — issues first

**Please open an issue before submitting a pull request.** Even small-looking changes can turn out to need discussion — a "quick tool addition" might raise a scope or safety question — and an issue keeps that discussion transparent and searchable.

1. **Open an issue** describing the change: what, where, and why. For a new tool or resource, include a link to the official source and a one-line neutral description.
2. Wait for a quick round of discussion or a maintainer 👍. This is usually fast.
3. **Open a pull request** that references the issue. Keep PRs focused — one topic per PR is easier to review.

Obvious typo and broken-link fixes still move quickly; a short issue ("typo in X") is enough.

## Style conventions

Keeping the repo consistent makes it easier to read and maintain.

**Tool tables.** Match the existing column formats (e.g., `| Tool | Purpose | Typical Cost | Notes |`):

- Link the tool to its **official** page or repo.
- Costs are **approximate ranges** ("$30-50"); prices drift, and that's expected.
- Keep descriptions neutral. Listing a tool is **not an endorsement**, and **no affiliate links**.

**Citations and reading lists.** Use `- [Title](url) — short note`. For books, use `- *Title* — Author(s) (optional note)`.

**Sections, anchors, and the flowchart.** If you add or rename a section:

- Update the **Table of Contents**.
- If it is one of the topics in the Mermaid flowchart, update the matching `click <node> href "…#anchor"` line so the diagram still jumps correctly. (GitHub only honors the `href` form of `click`.)

**Keep the README self-contained.** The README should read on its own as the main artifact; deeper or optional material goes in `docs/SUPPLEMENTARY_NOTES.md`.

## Adding a demo (code)

Demos live under `src/<demo-name>/`, each with:

- a local `README` (what it shows, the gear needed, how to run it), and
- a `requirements.txt` (or equivalent) if it has dependencies.

Demos must stay within the project's boundaries: **owned devices, sanctioned course hardware, or signals that are legal to receive.** No transmitting on restricted bands, and no touching networks or devices you do not own.

## Reporting a problem with the material

Found an error, a dead link, or a tool that no longer exists? Open an issue — that is the most useful thing you can do. If you believe something in the repo could itself cause harm (for example, it crosses the lines above), please flag it in an issue so it can be addressed quickly.
