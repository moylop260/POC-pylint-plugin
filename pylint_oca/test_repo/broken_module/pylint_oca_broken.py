

import openerp

from openerp import api
from openerp.api import one, multi

from openerp.exceptions import Warning as UserError  # pylint: disable=W0622
from openerp.exceptions import Warning as OtherName  # pylint: disable=W0404
from openerp.exceptions import Warning  # pylint: disable=W0404,W0622
from openerp.exceptions import (AccessError as AE,  # pylint: disable=W0404
                                ValidationError,
                                Warning as UserError2)


class snake_case(object):
    pass


class UseUnusedImport(object):
    def method1(self):
        return UserError, OtherName, Warning, AE, ValidationError, UserError2


class ApiOne(object):
    @api.one
    def copy(self):
        # ToDo: Add check of super
        pass


class One(object):
    @one
    def copy(self):
        pass


class OpenerpApiOne(object):
    @openerp.api.one
    def copy(self):
        pass


class WOApiOne(object):
    # copy without api.one decorator
    def copy(self):
        pass


class ApiOneMultiTogether(object):

    @api.multi
    @api.one
    def copy(self):
        pass

    @multi
    @one
    def copy2(self):
        pass

    @openerp.api.multi
    @openerp.api.one
    def copy3(self):
        pass

# vim:comment vim
