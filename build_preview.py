# Builds complete, stand-alone pages in the preview/ folder so you can open them
# by double-clicking, without running server.py.
# Run it from the project folder:  python3 build_preview.py

import os

os.makedirs("preview", exist_ok=True)

pages = [
    ("Our Mission", "mission_1B.html"),
    ("Cost barriers to care", "cost_barriers_2B.html"),
    ("Access and equity", "access_equity_3B.html"),
]

with open("templates/base.html") as f:
    base = f.read()

for title, name in pages:
    with open("templates/" + name) as f:
        content = f.read()
    page = base.replace("{{PAGE_TITLE}}", title).replace("{{PAGE_CONTENT}}", content)
    page = page.replace('href="/static/', 'href="../static/')
    page = page.replace('src="/static/', 'src="../static/')
    page = page.replace('"/cost-barriers"', '"cost_barriers_2B.html"')
    page = page.replace('"/access-equity"', '"access_equity_3B.html"')
    page = page.replace('<a href="/">', '<a href="#">')
    with open("preview/" + name, "w") as f:
        f.write(page)
    print("wrote preview/" + name)
