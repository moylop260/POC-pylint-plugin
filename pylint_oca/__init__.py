
from . import checkers
from . augmentations.main import apply_augmentations


def register(linter):
    """Required method to auto register this checker"""
    linter.register_checker(checkers.modules_odoo.ModuleChecker(linter))
    linter.register_checker(checkers.no_modules.NoModuleChecker(linter))
    linter.register_checker(checkers.format.FormatChecker(linter))
    linter.register_checker(checkers.modules.ModuleChecker(linter))

    # register any checking fiddlers
    apply_augmentations(linter)
