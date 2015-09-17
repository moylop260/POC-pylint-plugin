
import os

from pylint.checkers import utils
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

from difflib import unified_diff

from .. import misc, settings

import isort


OCA_MSGS = {
    # C->convention R->refactor W->warning E->error F->fatal

    'C%d01' % settings.BASE_PYMODULE_ID: (
        'Sort import with `isort` tool.',
        'import-sort',
        settings.DESC_DFLT
    ),
}


class ModuleChecker(BaseChecker):

    __implements__ = IAstroidChecker

    name = settings.CFG_SECTION
    msgs = OCA_MSGS

    def strip_lines(self, content, comment=True, empty=True):
        lines = []
        for line in content.splitlines(1):
            strip_line = line.strip(' \n')
            if (empty and not strip_line) \
               or (comment and strip_line.startswith('#')):
                continue
            lines.append(line)
        return lines

    def get_diff(self, str1, str2):
        diff_lines = []
        for line in unified_diff(
                self.strip_lines(str1),
                self.strip_lines(str2),
            ):
                diff_lines.append(line)
        return diff_lines

    @utils.check_messages(*(OCA_MSGS.keys()))
    def visit_module(self, node):
        if node.wildcard_import_names():
            # There is `import` sentence
            # TODO: Add option for combine_as_imports
            options_list = [{
                'combine_as_imports': True,
            },
            {
                'combine_as_imports': False,
            }
            ]
            # TODO: Use line length from config file
            isort_fail = True
            for options in options_list:
                result = isort.SortImports(file_contents=node.as_string(), line_length=79, **options).output
                diff = self.get_diff(node.as_string(), result)
                if not diff:
                    isort_fail = False
                    break
            if isort_fail:
                print "diff", node.file, ''.join(diff)
