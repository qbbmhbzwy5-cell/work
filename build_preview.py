# Builds complete, stand-alone pages in the preview/ folder so you can open them
# by double-clicking, without running server.py.
# Run it from the project folder:  python3 build_preview.py

pages = [
    ("Our Mission", "1B_mission.html"),
    ("Cost barriers to care", "2B_cost_barriers.html"),
    ("Access and equity", "3B_access_equity.html"),
]

with open("templates/base.html") as f:
    base = f.read()

for title, name in pages:
    with open("templates/" + name) as f:
        content = f.read()
    page = base.replace("{{PAGE_TITLE}}", title).replace("{{PAGE_CONTENT}}", content)
    page = page.replace('href="/static/', 'href="../static/')
    page = page.replace('src="/static/', 'src="../static/')
    page = page.replace('"/cost-barriers"', '"2B_cost_barriers.html"')
    page = page.replace('"/access-equity"', '"3B_access_equity.html"')
    page = page.replace('<a href="/">', '<a href="#">')
    with open("preview/" + name, "w") as f:
        f.write(page)
    print("wrote preview/" + name)
