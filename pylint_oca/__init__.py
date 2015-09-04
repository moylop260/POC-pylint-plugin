
from . import checkers


def register(linter):
    """Required method to auto register this checker"""
    linter.register_checker(checkers.modules_odoo.ModuleChecker(linter))
    linter.register_checker(checkers.no_modules.NoModuleChecker(linter))
    linter.register_checker(checkers.format.FormatChecker(linter))
    linter.register_checker(checkers.base.CustomBasicChecker(linter))

all_msgs = {}
all_msgs.update(checkers.modules_odoo.OCA_MSGS)
all_msgs.update(checkers.no_modules.OCA_MSGS)
all_msgs.update(checkers.format.OCA_MSGS)
all_msgs.update(checkers.base.OCA_MSGS)
print ',\n    '.join(sorted([name_key for msg_code, (title, name_key, description) in all_msgs.iteritems()]))
for msg_code, (title, name_key, description) in \
                sorted(all_msgs.iteritems()):
    print "\t- {0} - {1} - {2}".format(msg_code, title, name_key)
print ','.join(sorted(all_msgs.keys()))
