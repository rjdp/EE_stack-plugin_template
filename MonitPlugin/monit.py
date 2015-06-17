#!/usr/bin/env python3

# Monit Plugin
from cement.core import foundation, controller, handler, hook
from cement.core.controller import CementBaseController, expose


# define Plugin's all of theCore methods

def _monit_install():
    """All code for Monit Installation goes here"""
    print("installing Monit")


def _monit_remove():
    """All code for Monit Removal goes here"""
    print("removing Monit")

# define all hook-funtions required for this plugin


def monit_install_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing"""
        _monit_install()


def monit_remove_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t out use-case unless
        u know what ur doing"""
        _monit_remove()


# define application controllers

class MonitPlugin4eeController(CementBaseController):

    class Meta:
        label = 'MonitPlugin4ee'
        description = "Monit Plugin for ee"
        stacked_on = 'stack'
        stacked_type = 'embedded'
        arguments = [
            (['--monit'], dict(help="install/remove monit", action='store_true')),

        ]


def load(ee):
    handler.register(MonitPlugin4eeController)
    hook.register('stack_install_hook', monit_install_hookfunc)
    hook.register('stack_remove_hook', monit_remove_hookfunc)
