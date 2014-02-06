from utils import enclose_tags
from plainprinter import PlainPrinter

class DayonePrinter(PlainPrinter):
    def __init__(self):
        self.prev_tag = '**'
        self.post_tag = '**'

    def pformat(self, tlist):
        result = []
        for item in tlist:
            if item.type == 'project':
                result.append(self.project(item))
            elif item.type == 'task':
                result.append(self.task(item))
            elif item.type == 'note':
                result.append(self.note(item))
            else:
                result.append('')
        return '\n'.join(result).encode('utf-8').strip() + '\n'

    def pprint(self, tlist):
        print self.pformat(tlist)

    def project(self, item):
        return '#' * (item.indent_level + 1) + ' ' + enclose_tags(item.text, self.prev_tag, self.post_tag) + ':'

    def task(self, item):
        return '\t' * (item.indent_level - 2) + '- ' + enclose_tags(item.text, self.prev_tag, self.post_tag)

    def note(self, item):
        return '*' + enclose_tags(item.text, self.prev_tag, self.post_tag) + '*'
