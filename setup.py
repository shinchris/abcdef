from setuptools import setup, find_packages
setup(name='abcdef',
      version='1.0',
      packages = find_packages(),
      entry_points ={
            'console_scripts': [
                'abcdef = abcdef.abcdef:main'
            ]
        },
      )
