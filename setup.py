import os
from setuptools import setup

abspathconfig = '/etc/ee/plugins.d'
abspathplugins = '/usr/lib/ee/plugins'

if not os.path.exists(abspathconfig):
    os.makedirs(abspathconfig)

if not os.path.exists(abspathplugins):
    os.makedirs(abspathplugins)


setup(name='Monit Plugin 4 ee',
      version='0.1',
      description='Monit Plugin',
      url='http://github.com/rjdp',
      author='rajdeep',
      author_email='rajdeep.sharma@rtcamp.com',
      license='MIT',
      data_files=[(abspathconfig, ['MonitPlugin/monit.conf']),
                  (abspathplugins, ['MonitPlugin/monit.py'])],
      # packages=['cli'],
      install_requires=[
          'ee',
      ],

      zip_safe=False)