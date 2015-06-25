#!/usr/bin/env python3
"""
Skeleton Code for EasyEngine Stack Plugin(means of plugging additional
                                           arguments and respective behavior
                                           to an EE installation)

Assumptions/Standards for plugins
==================================
a) We dont append additonal subcommands to whats already available under
   "ee stack" command i.e (install,remove,purge,status,start,stop
                            ,reload,restart and upgrade)
b) For each argument that we add , we also define a method to mimic
   each subcommand in "ee stack" w.r.t the argument eg)for --monit
   we defined _monit_install(),_monit_remove() and so on .
c) For each subcommand under "ee stack" we define a hook-function which
   which is registered with their respective predefined hooks

   ...more

"""


from cement.core import foundation, controller, handler, hook
from cement.core.controller import CementBaseController, expose


# define Plugin's all of theCore methods

def _monit_install():
    """All code for Monit Installation goes here"""
    print("installing Monit")


def _monit_remove():
    """All code for Monit Removal goes here"""
    print("removing Monit")


def _monit_purge():
    """All code for Purging Monit goes here"""
    print("Purging Monit")


def _monit_status():
    """All code for showing Monit status goes here"""
    print("shows Monit status")


def _monit_start():
    """All code for starting Monit goes here"""
    print("starts Monit")


def _monit_stop():
    """All code for stopping Monit goes here"""
    print("stops Monit")


def _monit_reload():
    """All code for reloading Monit goes here"""
    print("reloads Monit")


def _monit_restart():
    """All code for restarting Monit goes here"""
    print("restarts Monit")


def _monit_upgrade():
    """All code for Monit upgradation goes here"""
    print("upgrades Monit")


# define all hook-funtions required for this plugin


def monit_install_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack install --monit` is issued"""
        _monit_install()

    # Additional if-blocks like the above if-block should be added in case you are 
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_install()
            """


def monit_remove_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack remove --monit` is issued"""
        _monit_remove()

    # Additional if-blocks like the above if-block should be added in case you are 
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_remove()
            """


def monit_purge_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack purge --monit` is issued"""
        _monit_purge()

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_purge()
            """


def monit_status_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack status --monit` is issued"""
        _monit_status()

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_status()
            """


def monit_start_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack start --monit` is issued"""
        _monit_start()

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_start()
            """


def monit_stop_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack stop --monit` is issued"""
        _monit_stop()

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_stop()
            """


def monit_reload_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack reload --monit` is issued"""
        _monit_reload()

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_reload()
            """


def monit_restart_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack restart --monit` is issued"""
        _monit_restart()
    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_restart()
            """


def monit_upgrade_hookfunc(ee):

    if ee.pargs.monit:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing ,this code-block is executed when
        `ee stack upgrade --monit` is issued"""
        _monit_upgrade()

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_upgrade()
            """


# define application controllers

class MonitPlugin4eeController(CementBaseController):

    class Meta:
        label = 'MonitPlugin4ee'
        description = "Monit Plugin for ee"
        stacked_on = 'stack'
        stacked_type = 'embedded'
        # add arguments that you intend 'ee stack' command to accept
        arguments = [
            (['--monit'],
             dict(help="install/remove monit", action='store_true')),

        ]


def load(ee):
    # register the controller with ee
    handler.register(MonitPlugin4eeController)
    # register hook-functions with stack-hooks that are predefined in ee
    hook.register('stack_install_hook', monit_install_hookfunc)
    hook.register('stack_remove_hook', monit_remove_hookfunc)
    hook.register('stack_purge_hook', monit_purge_hookfunc)
    hook.register('stack_status_hook', monit_status_hookfunc)
    hook.register('stack_start_hook', monit_start_hookfunc)
    hook.register('stack_stop_hook', monit_stop_hookfunc)
    hook.register('stack_restart_hook', monit_reload_hookfunc)
    hook.register('stack_restart_hook', monit_restart_hookfunc)
    hook.register('stack_upgrade_hook', monit_upgrade_hookfunc)
