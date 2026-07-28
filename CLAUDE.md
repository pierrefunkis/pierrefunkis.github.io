# Working notes for Claude

## Project

Static marketing site for Semantic, served by GitHub Pages at
`www.workwithsemantic.com` (see `CNAME`). No build step, no dependencies:
plain HTML + `style.css` + `main.js`.

Pages: `index.html`, `about/index.html`, `for-talents/index.html`, `404.html`.

## Always end a change with local preview instructions

The owner previews every change on localhost before merging. After pushing
any change, close the response with a copy-paste block like this, with the
real branch name substituted in:

```bash
cd ~/pierrefunkis.github.io
git fetch origin <branch> && git checkout <branch> && git pull
python3 -m http.server 8000
```

Then: open `http://localhost:8000`, Ctrl+C to stop.

Serve over HTTP rather than opening `index.html` from the filesystem — the
nav links point at `/about/` and `/for-talents/`, which need a server to
resolve to their `index.html`.

Mention `git checkout main` + reload as the way to compare against what is
currently live.
