import re
from markdown.util import etree, AtomicString
from markdown.extensions import Extension
from markdown.blockprocessors import BlockProcessor


class NotebookOutputBlockProcessor(BlockProcessor):
    RE_OUTPUT = re.compile(r'(\|\[(?P<number>\d*)\]>)(?P<text>.*?)<\[\]\|')

    def __init__(self, parser, config):
        self.config = config
        super(NotebookOutputBlockProcessor, self).__init__(parser)

    def test(self, parent, block):
        return bool(self.RE_OUTPUT.search(block))

    def run(self, parent, blocks):
        block = blocks.pop(0)

        match = self.RE_OUTPUT.match(block)
        text = match.group('text')

        container = etree.SubElement(parent, 'div')
        container.set('class', self.config['OUTPUT_CLASS'])

        if self.config['OUTPUT_SHOW_LABEL']:
            label = etree.SubElement(container, 'div')
            label.set('class', 'notebook_output_text')

            span = etree.SubElement(label, 'span')
            span.text = self.config['OUTPUT_LABEL_TEXT'].format(match.group('number'))

        output = etree.SubElement(container, 'div')
        output.set('class', 'notebook_output_code')

        preElement = etree.SubElement(output, 'pre')
        preElement.text = AtomicString('%s\n' % text)

    @staticmethod
    def _is_output_block(sibling):
        return sibling is not None and sibling.tag == "pre"


class NotebookExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {'OUTPUT_CLASS': ['notebook_output', 'CSS class name for output styling'],
                       'OUTPUT_SHOW': [True, 'Show output blocks'],
                       'OUTPUT_SHOW_LABEL': [True, 'Show output label itself'],
                       'OUTPUT_LABEL_TEXT': ['Out[{}]:', 'Label for output']}

        super(NotebookExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        if self.getConfig('OUTPUT_SHOW'):
            output = NotebookOutputBlockProcessor(md.parser, self.getConfigs())
            md.parser.blockprocessors.add('notebook_output', output, '>code')


def makeExtension(*args, **kwargs):
    return NotebookExtension(*args, **kwargs)
