#!/usr/bin/env python3

from aws_cdk import core

from atmoz.atmoz_stack import AtmozStack

app = core.App()

env = app.node.try_get_context("environment")

AtmozStack(app, "atmoz-net", env=env)

app.synth()
