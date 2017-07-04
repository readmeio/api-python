import setuptools

setuptools.setup(name='api',
                 version='1.0.2',
                 description='Consume an API from ReadMe Build',
                 long_description=open('README.md').read().strip(),
                 author='ReadMe',
                 author_email='support@readme.io',
                 download_url='https://github.com/readmeio/api-python/archive/1.0.2.tar.gz',
                 url='http://readme.build',
                 py_modules=['api'],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='api readme')
