from distutils.core import setup

from pip.req import parse_requirements

install_reqs = parse_requirements("requirement.txt")
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='twitter_api',
    version='0.1',
    packages=['twitter_api'],
    url='',
    license='',
    author='Raphaël Courivaud',
    author_email='r.courivaud@gmail.com',
    description='',
    install_requires=reqs
)
