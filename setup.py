from setuptools import setup

setup(name='api',
      version='0.0.6',
      description='Consume an API from ReadMe Build',
      url='https://readme.build',
      author='ReadMe',
      author_email='support@readme.io',
      license='MIT',
      packages=['api'],
      install_requires=['requests', 'nose'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
