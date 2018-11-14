from distutils.core import setup

setup(name='mymath',
      version='0.1',
      description='A silly math package',
      author='Mike Driscoll',
      author_email='mike@mymath.org',
      url='http://www.mymath.org/',
      packages=['mymath', 'mymath.adv'],
      )