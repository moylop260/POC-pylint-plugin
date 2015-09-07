
import os
from pylint.lint import Run

EXPECTED_ERRORS = 2

files = [os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'pylint_oca_broken.py')]

cmd = [
    '--load-plugins=pylint_oca', '-r', 'n',
    '--msg-template={path}:{line}: [{msg_id}({symbol}), {obj}] {msg}',
    '--output-format=colorized'
]
pylint_res = Run(cmd + files, exit=False)
assert sum([pylint_res.linter.stats['by_msg'][msg]
    for msg in pylint_res.linter.stats['by_msg']]) == EXPECTED_ERRORS, \
    "Errors found different to expected."
