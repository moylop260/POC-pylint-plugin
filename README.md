[![Build Status](https://travis-ci.org/moylop260/pylint-oca.svg?branch=master)](https://travis-ci.org/moylop260/pylint-oca)
[![Coverage Status](https://coveralls.io/repos/moylop260/pylint_oca/badge.svg?branch=master&service=github)](https://coveralls.io/github/moylop260/pylint_oca?branch=master)
[![Pypi Package](https://img.shields.io/pypi/v/oca-pylint-plugin.svg)](https://pypi.python.org/pypi/oca-pylint-plugin)



# OCA pylint plugin

Enable custom checks for OCA modules.

[//]: # (checks)
Code | Description | short name
--- | --- | ---
C7902 | Missing ./README.rst file. Template here: %s | missing-readme
C8101 | Missing author required "%s" in manifest file | manifest-required-author
C8102 | Missing required key "%s" in manifest file | manifest-required-key
C8103 | Deprecated key "%s" in manifest file | manifest-deprecated-key
C8104 | Use `CamelCase` "%s" in class name "%s". You can use oca-autopep8 of https://github.com/OCA/maintainer-tools to auto fix it. | class-camelcase
C8105 | License "%s" not allowed in manifest file. | license-allowed
C8201 | No UTF-8 coding comment found: Use `# coding: utf-8` or `# -*- coding: utf-8 -*-` | no-utf8-coding-comment
E7901 | %s:%s %s | rst-syntax-error
E7902 | %s error: %s | xml-syntax-error
R8101 | Import `Warning` should be renamed as UserError `from openerp.exceptions import Warning as UserError` | openerp-exception-warning
W7901 | Dangerous filter without explicit `user_id` in xml_id %s | dangerous-filter-wo-user
W7902 | Duplicate xml record id %s | duplicate-xml-record-id
W7903 | %s | javascript-lint
W8101 | Detected api.one and api.multi decorators together. | api-one-multi-together
W8102 | Missing api.one or api.multi in copy function. | copy-wo-api-one
W8103 | Translation method _("string") in fields is not necessary. | translation-field
W8104 | api.one deprecated | api-one-deprecated
W8105 | attribute "%s" deprecated | attribute-deprecated
W8106 | Missing `super` call in "%s" method. | method-required-super
W8201 | Incoherent interpreter comment and executable permission. Interpreter: [%s] Exec perm: %s | incoherent-interpreter-exec-perm
W8202 | Use of vim comment | use-vim-comment

[//]: # (end checks)


## Install
`# pip install --upgrade git+https://github.com/moylop260/pylint_oca.git`

Or

`# pip install --upgrade --pre oca-pylint-plugin`


## Usage

 `pylint --load-plugins=pylint_oca -e odoolint ...`

 
 Example to test just odoo-lint case:

 `touch {ADDONS-PATH}/__init__.py`
 
 `pylint --load-plugins=pylint_oca -d all -e odoolint {ADDONS-PATH}`
