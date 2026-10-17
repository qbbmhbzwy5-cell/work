Results open with one dark summary card (`summary-card`) holding a single plain-English sentence, followed by one stat card per group inside a `stat-row`. A stat card (`stat-card`) shows the group name (`stat-name`), one big percentage (`stat-figure`), how many people it is based on, and a bar. The first group uses `figure-orange` and `fill-orange`; the second uses `figure-green` and `fill-green`.

The consumer provides the sentence, the group names, the percentages, the people counts and each bar's width. A bar is a `bar` (the grey track) holding a `bar-fill` whose width is set with `style="width: 76%"`. The `%` sign is required: without it the browser ignores the width and the bar fills the whole track. The example numbers here are samples. Use one scale for every bar on a page, so the bars never suggest a bigger gap than the numbers show.

- Do keep the sentence to one line of meaning and name both groups.
- Do not drop the number next to the bar.
- Do not use more than two stat cards in a row.
