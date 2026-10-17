The results table lives inside a white `table-card` that scrolls sideways on a narrow screen instead of widening the page. The table is a `data-table`: a bold header row with a 3px `ink` rule, 16px cell padding and thin `line` rules between rows. The last column holds the percentage in bold (`strong`), shown with one decimal. Below the table, inside the same card, two `note` lines: who was left out, then the source. When the card sits under other blocks, add `table-gap` for space above it.

The consumer provides the column names, the rows and the source line. Every row must have one cell for every column: a missing `<td>` shifts the later numbers under the wrong heading. Rows come from the database later; until then they are marked with a `SAMPLE` comment.

- Do keep every figure the table shows in plain numbers, so the reader can check the bars.
- Do not add colors or stripes to rows.
- Do not remove the left-out note: it is how the page says which people were not counted.
