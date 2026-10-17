Buttons are pills with a bold label and a 2px outline, built with the class `button`. Add `button-big button-main` (green) for the one action that sends the form: Apply or Discover. Add `button-big` (white, ink outline) for Reset. Use plain `button` for the Search button. Put a form's buttons in a row with `actions`.

Reset is a link styled as a button, not a button: `<a class="button button-big" href="/page-address">Reset</a>` takes the reader back to the page with no choices. Its `href` must be the address of the page it sits on. There is no Print button; add a line of text telling the reader to press Ctrl+P (Windows) or Cmd+P (Mac).

The consumer provides the label and, inside a form, the `type`: give a button that must not send the form `type="button"`, because a button inside a form sends it by default. The button that does send it has `type="submit"`.

- Do keep one green button per form.
- Do not change a button's height or radius: they come from `control-h` and `control-h-lg`.
- Do not use orange on a button.
