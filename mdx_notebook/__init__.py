from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

OUTPUT_RE = r'(\|\[\]>)(.*?)<\[\]\|'


class NotebookPattern(Pattern):
    def __init__(self, pattern, output_class='notebook_output'):
        self.output_class = output_class
        super(NotebookPattern, self).__init__(pattern)

    def handleMatch(self, m):
        el = etree.Element('pre')
        el.set('class', self.output_class)
        el.text = m.group(3)

        return el


class Notebook(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'output_class': ['notebook_output', 'Class to apply to the output pre block']
        }
        super(Notebook, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        notebook_pattern = NotebookPattern(OUTPUT_RE,
                                           output_class=self.getConfig('output_class'))
        md.inlinePatterns['notebook_output'] = notebook_pattern


def makeExtension(*args, **kwargs):
    return Notebook(*args, **kwargs)
