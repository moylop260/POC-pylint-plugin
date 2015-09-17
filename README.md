[![Build Status](https://travis-ci.org/moylop260/pylint-oca.svg?branch=master)](https://travis-ci.org/moylop260/pylint-oca)
[![Coverage Status](https://coveralls.io/repos/moylop260/pylint_oca/badge.svg?branch=master&service=github)](https://coveralls.io/github/moylop260/pylint_oca?branch=master)
[![Pypi Package](https://img.shields.io/pypi/v/oca-pylint-plugin.svg)](https://pypi.python.org/pypi/oca-pylint-plugin)



# OCA pylint plugin

Enable custom checks for OCA modules.

## Install
`# pip install --upgrade git+https://github.com/moylop260/pylint_oca.git`

Or

`# pip install --upgrade --pre oca-pylint-plugin`


## Usage

 `pylint --load-plugins=pylint_oca -e odoolint ...`

 
 Example to test just odoo-lint case:

 `touch {ADDONS-PATH}/__init__.py`
 `pylint --load-plugins=pylint_oca -d all -e odoolint {ADDONS-PATH}`
