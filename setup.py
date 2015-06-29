import os
from setuptools import setup

abspathconfig = '/etc/ee/plugins.d'  # path for config. files for EE-plugins
abspathplugins = '/usr/lib/ee/plugins'  # path for actual plugin(*.py)


# if the directories for plugin config files and the actual plugins doesn't
# exist create them
if not os.path.exists(abspathconfig):
    os.makedirs(abspathconfig)

if not os.path.exists(abspathplugins):
    os.makedirs(abspathplugins)


setup(name='Monit Plugin 4 ee',  # plugin name,used by package-managers as ID
      version='0.1',  # used by package manager incase of a upgrade/downgrade
      description='Monit Plugin',  
      url='http://github.com/rjdp',
      author='rajdeep',
      author_email='rajdeep.sharma@rtcamp.com',
      license='MIT',
      packages=['custom_packages'],
      # move config files and actual plugin at required location
      # if using templates move templates to '/var/lib/ee/templates'
      data_files=[(abspathconfig, ['Config/monit.conf']), 
                  (abspathplugins, ['source/plugin/monit.py'])],
      # packages=['cli'], uncomment if u r importing modules written by u 
      install_requires=[
          'ee',
      ],
      zip_safe=False)
