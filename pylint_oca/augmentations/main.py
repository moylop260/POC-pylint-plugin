
import os

from pylint_plugin_utils import augment_visit, suppress_message
from pylint.checkers.base import BasicChecker
from pylint.checkers.similar import SimilarChecker
from .. import settings


def is_manifest_file(node):
    """Verify if the node file is a manifest file
    :return: Boolean `True` if is manifest file else `False`"""
    filename = os.path.basename(node.root().file)
    is_manifest = filename in settings.MANIFEST_FILES
    return is_manifest


def allow_duplicated_code(chain, node):
    if is_manifest_file(node):
        return
    chain()


def apply_augmentations(linter):
    """Apply suppression rules."""

    # W0104 - pointless-statement
    # manifest file have a valid pointless-statement dict
    suppress_message(linter, BasicChecker.visit_discard,
                     'W0104', is_manifest_file)

    # R0801 - duplicate-code
    # manifest file is duplicated ever.
#    augment_visit(linter, SimilarChecker.process_module,
#                  allow_duplicated_code)
