from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

OUTPUT_RE = r'(\|\[\]>)(.*?)\|\[\]>'


class NotebookPattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element('pre')
        el.set('class', 'notebook_output')
        el.text = m.group(3)

        return el


class Notebook(Extension):
    def extendMarkdown(self, md, md_globals):
        notebook_pattern = NotebookPattern(OUTPUT_RE)
        md.inlinePatterns['notebook_output'] = notebook_pattern

