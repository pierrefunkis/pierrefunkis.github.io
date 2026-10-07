# Working agreements

## Pull requests
- Open a new pull request for every round of changes. Never push additional commits to an existing PR, even if it is still open.
- Start each new round from a fresh branch off the latest `main`.

## Site
- Pages are generated: edit `tools/` (templates, `plates.py`, `build.py`) and `style.css`, then run `python3 tools/build.py` and commit the regenerated HTML.
