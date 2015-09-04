
import os
import setuptools

from pip.req import parse_requirements
from pip.download import PipSession


setuptools.setup(setup_requires=['pbr'],
                 pbr=True,
                 package_data={'': ['*.yaml']})
