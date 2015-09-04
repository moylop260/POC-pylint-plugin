
import os
import setuptools

from pip.req import parse_requirements
from pip.download import PipSession

file_requirements = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "requirements.txt")

install_reqs = parse_requirements(file_requirements, session=PipSession)
reqs = [str(ir.req) for ir in install_reqs]

setuptools.setup(setup_requires=['pbr'],
                 pbr=True,
                 install_requires=reqs,
                 package_data={'': ['*.yaml']})
