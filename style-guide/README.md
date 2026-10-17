This is the look of a public health data website that has to work for an older reader with reading glasses and for a busy parent on a phone: large text, plain words, one green accent. Every page of the site, Part A and Part B, uses it. Build new pages from the tokens and components here and do not add colors, fonts or radii.

## What the site is built with

Only HTML, basic CSS and Python. There is no JavaScript, no SQL in the pages, and no CSS variables, grid or media queries. Rows and columns of cards use `display: flex` with `flex-wrap: wrap`, which also makes them stack on a narrow screen. The one newer HTML tag is `<details>`, used for "Read more" boxes. If you are not allowed it, show that text all the time instead.

The tokens below are names for the values. In your CSS type the value itself, for example `#1b6b4f`, not the token name.

## Setup

Put these three lines in `templates/base.html` inside `<head>`. The font link is the same on every page.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/static/style.css">
```

The shared `static/style.css` starts with these rules. Whoever creates it pushes it first, and the other person pulls before writing any CSS.

```css
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: 'Atkinson Hyperlegible', Arial, sans-serif;
  font-size: 20px;
  line-height: 1.5;
  background-color: #eef3f7;
  color: #14262e;
}

a {
  color: #1b6b4f;
}

select, input, button {
  font-family: inherit;
}

select:focus, input:focus, button:focus, a:focus {
  outline: 3px solid #f2a900;
  outline-offset: 2px;
}

th, td {
  text-align: left;
}
```

Keep page-specific CSS in its own file, for example `static/partb.css` for Part B and a separate file for Part A, and link it on the first line of the page's template with `<link rel="stylesheet" href="/static/partb.css">`. Two people editing one stylesheet causes Git conflicts.

## Content fundamentals

- Write for someone with no statistics background. Use short sentences and everyday words.
- Name things the way a person would: "What kind of care?", "Where people live", "Long-term condition".
- Start every results block with `Showing results for:` and the person's choices, with the number of people in brackets.
- State who is left out: "People who did not need the service, or did not answer, are left out."
- End a results block with the source line: "Source: Patient Experiences Survey data, 2020-21 to 2024-25 (synthetic data based on ABS statistics)."
- Show whole percentages in big figures (23%) and one decimal in tables (22.8%).
- Use sentence case for headings and buttons. No emoji.

## Visual foundations

- **Color.** `ground` behind everything, white `card` surfaces, `ink` for all text. `green` is the one accent: step numbers, the main button, links, the Help box rule. In a two-group comparison the first group is `orange` and the second is `green`. Use `orange-text` for orange figures, never `orange` itself.
- **Type.** One family, Atkinson Hyperlegible, in regular and bold. Body is 20px. Nothing is smaller than `note` (18px). Take sizes from the type styles, not by eye.
- **Spacing.** Content sits in one column, at most `page-max` wide, with `space-24` side gutters. Blocks are `space-28` apart, cards are padded `space-24`, rows of fields use `space-16`.
- **Shape.** Cards use `radius-card`. Dropdowns use `radius-select`. Buttons, the search box and nav links are pills (`radius-pill`, or `radius-pill-lg` for 64px buttons).
- **Controls.** Dropdowns and the search box are `control-h` (56px) tall with a 2px `field-border`. Every dropdown has a visible bold label. Large buttons are `control-h-lg` (64px).
- **Bars.** 24px tall on a `track`, filled with `orange` or `green`. Always put the number next to the bar so color is never the only signal.
- **Focus.** Every link, button and field shows a 3px `focus` outline with a 2px offset. See the note on the `focus` token about its contrast.
- **Hover.** Nav links and buttons underline on hover. Nothing else changes.
- **Depth and motion.** No shadows, no gradients, no animation. Separation comes from white cards on `ground`.

## Layout

A page is a white header (logo box, then the links Home, Explore, About), a search bar, then the content. Form pages use the Help box, then numbered step cards, then Apply (or Discover) and Reset, then a results block. Results go in this order: the "Showing results for" line, the plain-English summary card, the stat cards, the table, the left-out note and the source line. Cards in a row wrap to one column on a phone.

## Components

- `Button`: Search, Apply, Discover and Reset.
- `StepCard`: a numbered card with one question and its dropdowns.
- `HelpBox`: always-visible help above a form.
- `StatCard`: the dark summary sentence and the two big-figure cards with bars.
- `DataTable`: the results table with its notes.

Use their class names so Part A and Part B look the same.

## Do and do not

- Do keep the 20px base size and the visible labels. Do not shrink text to fit more on screen.
- Do use the colors and sizes from the tokens. Do not type a new hex value into a page.
- Do keep Part A and Part B pages in the same header, color and component set. Do not restyle a component for one page.
- Do not rely on color alone to tell two groups apart: use the number, the label or the bar length too.
- Do not add JavaScript. Where a design shows a pop-up, a hide-and-show help button or a print button, use a link, an always-visible box or a line of text.
