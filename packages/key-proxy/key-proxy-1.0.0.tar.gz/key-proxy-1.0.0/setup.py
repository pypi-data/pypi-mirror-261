from setuptools import setup, find_packages
setup(
   name='key-proxy',
   version='1.0.0',
   packages=find_packages(),
   install_requires=[
      'click',
   ],
   entry_points='''
      [console_scripts]
      key-proxy=script:hello
      ''',
)