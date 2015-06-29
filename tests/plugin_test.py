#from __future__ import absolute_import
import unittest
<<<<<<< HEAD
from ..plugin import sample
=======
from ..src.plugin import sample_plugin
>>>>>>> 0f93a87f9cd10b6ae3f0a178342a5608ef10e0ab

class SamplePluginTestCase(unittest.TestCase):

    def test_sample_install(self):
        """test _sample_install() functionality"""
        pass

    def test_sample_remove(self):
        """test _sample_remove() functionality"""
        pass

    def test_sample_purge(self):
        """test _sample_purge() functionality"""
        pass

    def test_sample_status(self):
        """test _sample_status() functionality"""
        pass

    def test_sample_start(self):
        """test _sample_start() functionality"""
        pass

    def test_sample_stop(self):
        """test _sample_stop() functionality"""
        pass

    def test_sample_reload(self):
        """test _sample_reload() functionality"""
        pass

    def test_sample_restart(self):
        """test _sample_restart() functionality"""
        pass

    def test_sample_upgrade(self):
        """test _sample_upgrade() functionality"""
        pass
