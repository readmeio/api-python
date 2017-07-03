import setuptools
from api.version import Version


setuptools.setup(name='api',
                 version=Version('1.0.0').number,
                 description='Consume an API from ReadMe Build',
                 long_description=open('README.md').read().strip(),
                 author='ReadMe',
                 author_email='support@readme.io',
                 url='http://readme.build',
                 py_modules=['api'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='api readme')
