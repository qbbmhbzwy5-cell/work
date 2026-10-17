A step card asks one question of the reader: a green numbered circle (`step-number`), the question (`step-title`) and one or more dropdowns. The whole card is a `step`, with the circle and a `step-body` side by side. Stack the cards in order, 1, 2, 3. A card with a single dropdown uses the question itself as that dropdown's `<label>` (`<label class="step-title" for="...">`). A card with several dropdowns puts them in `fields`, each in a `field` with its own label.

The consumer provides the step number, the question and the dropdowns. Every dropdown needs a visible `<label for="...">` whose `for` matches the select's `id`, so clicking the words focuses the field. Give every select a `name`, because the form sends choices by name.

- Do put the most important choice in step 1.
- Do not add a fourth step; split the form into two pages first.
- Do not hide a label or use placeholder text instead of one.
