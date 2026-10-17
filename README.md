# Patient Experiences Site: Part B pages (HTML and CSS)

Finished version of the three Part B pages, with the shared look (Atkinson Hyperlegible, 20px text, pale blue-grey background, one green accent). Plain HTML and CSS only. No JavaScript.

If you are an AI assistant helping with this project, copy the look from these files, then read `style-guide/README.md` for the rules.

## Files

- `templates/base.html`: page shell with header, navigation and search bar. `{{PAGE_TITLE}}` and `{{PAGE_CONTENT}}` are filled in by `server.py`.
- `static/style.css`: shared styles for every page (Part A and Part B)
- `static/partb.css`: styles used only by the Part B pages
- `templates/1B_mission.html`, `2B_cost_barriers.html`, `3B_access_equity.html`: the page content
- `static/michelle.jpg`, `static/gary.jpg`: persona photos
- `preview/`: the same three pages as complete stand-alone files. Double-click one to see it in a browser, no server needed. Forms and links do not work there.
- `build_preview.py`: rebuilds `preview/` after you change a template (`python3 build_preview.py`)
- `style-guide/`: the colors, sizes, spacing and component rules written out

## Notes

- Numbers in the results are sample data, marked with `SAMPLE` comments. Level 1 and 2 pages must read from the database before M2 is marked.
- Mission statement, team names and student numbers are placeholders.
- Home, Explore and About links are placeholders.
