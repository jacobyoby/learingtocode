# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('rufus')
def speccy(bot, trigger):
	bot.say('Download and install rufus from https://goo.gl/Z1oNBt Next to create')
