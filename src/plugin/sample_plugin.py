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
   each subcommand in "ee stack" w.r.t the argument eg)for --sample
   we defined _sample_install(ee),_sample_remove(ee) and so on .
c) For each subcommand under "ee stack" we define a hook-function which
   which is registered with their respective predefined hooks

   ...more

"""


from cement.core import foundation, controller, handler, hook
from cement.core.controller import CementBaseController, expose


# define Plugin's all of theCore methods

def _sample_install(ee):
    """All code for sample Installation goes here"""
    print("installing sample")


def _sample_remove(ee):
    """All code for sample Removal goes here"""
    print("removing sample")


def _sample_purge(ee):
    """All code for Purging sample goes here"""
    print("Purging sample")


def _sample_status(ee):
    """All code for showing sample status goes here"""
    print("shows sample status")


def _sample_start(ee):
    """All code for starting sample goes here"""
    print("starts sample")


def _sample_stop(ee):
    """All code for stopping sample goes here"""
    print("stops sample")


def _sample_reload(ee):
    """All code for reloading sample goes here"""
    print("reloads sample")


def _sample_restart(ee):
    """All code for restarting sample goes here"""
    print("restarts sample")


def _sample_upgrade(ee):
    """All code for sample upgradation goes here"""
    print("upgrades sample")


# define all hook-funtions required for this plugin


def sample_install_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack install --sample` is issued"""
        _sample_install(ee)

    # Additional if-blocks like the above if-block should be added in case you are 
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_install(ee)
            """


def sample_remove_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack remove --sample` is issued"""
        _sample_remove(ee)

    # Additional if-blocks like the above if-block should be added in case you are 
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_remove(ee)
            """


def sample_purge_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack purge --sample` is issued"""
        _sample_purge(ee)

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_purge(ee)
            """


def sample_status_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack status --sample` is issued"""
        _sample_status(ee)

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_status(ee)
            """


def sample_start_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack start --sample` is issued"""
        _sample_start(ee)

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_start(ee)
            """


def sample_stop_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack stop --sample` is issued"""
        _sample_stop(ee)

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_stop(ee)
            """


def sample_reload_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack reload --sample` is issued"""
        _sample_reload(ee)

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_reload(ee)
            """


def sample_restart_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing, this code-block is executed when
        `ee stack restart --sample` is issued"""
        _sample_restart(ee)
    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_restart(ee)
            """


def sample_upgrade_hookfunc(ee):

    if ee.pargs.sample:
        """All code for this method lives in this block w.r.t our use-case unless
        u know what ur doing ,this code-block is executed when
        `ee stack upgrade --sample` is issued"""
        _sample_upgrade(ee)

    # Additional if-blocks like the above if-block should be added in case you are
    # - adding more than one argument using a single plugin
    # eg) we add --goaccess argument
            """
            if ee.pargs.goaccess:
                _goaccess_upgrade(ee)
            """


# define application controllers

class samplePlugin4eeController(CementBaseController):

    class Meta:
        label = 'samplePlugin4ee'
        description = "sample Plugin for ee"
        stacked_on = 'stack'
        stacked_type = 'embedded'
        # add arguments that you intend 'ee stack' command to accept
        arguments = [
            (['--sample'],
             dict(help="install/remove sample", action='store_true')),

        ]


def load(ee):
    # register the controller with ee
    handler.register(samplePlugin4eeController)
    # register hook-functions with stack-hooks that are predefined in ee
    hook.register('stack_install_hook', sample_install_hookfunc)
    hook.register('stack_remove_hook', sample_remove_hookfunc)
    hook.register('stack_purge_hook', sample_purge_hookfunc)
    hook.register('stack_status_hook', sample_status_hookfunc)
    hook.register('stack_start_hook', sample_start_hookfunc)
    hook.register('stack_stop_hook', sample_stop_hookfunc)
    hook.register('stack_restart_hook', sample_reload_hookfunc)
    hook.register('stack_restart_hook', sample_restart_hookfunc)
    hook.register('stack_upgrade_hook', sample_upgrade_hookfunc)
