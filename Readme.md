# Notebook style markdown extension

If you work with Jupyter notebooks, you will remember they have the concept of _inputs_ and _outputs_ in the notation, an input is something you enter and and output what the compiler or interpreter returns (it is very useful with expression based languages like OCaml or Haskell).

When working in a Jupyter to Notebook extension for Pelican I found problems trying to convert the inputs and outputs to a markdown syntax, so I think this could be useful to represent them in markdown.

This extension adds support for the elements `|[]>` and `|<[]` to indicate _outputs_ and _inputs_ respectibly. They will be rendered inside `code` elements with defined class styles, for example:

```md
|[]> val a: int = 4 |[]>
```

Would be rendered as:

```html
<code class="notebook_output">val a: int = 4</code>
```

You can define a number between the brackets for the style:

```md
|[12]> val a: int = 5 |[]>
```

Would be rendered as:

```html
<span class="notebook_output_index">12</span><code class="notebook_output">val a: int = 4</code>
```

## Configuration options

 * `output_class` what class to use with the output code, by default is `notebook_output`
 * `show_output` display output, by default is `True`, set this if you want to hide the output at all
 * `show_label` display a label for the output
 * `label_text` used with `show_label` set the text for the label for each output

## Using the extension

First install with pip: `pip install markdown-notebook` and then set the extension name in your Python Markdown library, the name of the extension is `mdx_notebook`.

