# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('backup')
def speccy(bot, trigger):
	bot.say('Please read the following guide for good backup options and instructions to setup: https://goo.gl/KX8o7B')
