# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('pw')
def speccy(bot, trigger):
	bot.say('We cannot assist with password issues due to high potential for abuse.')
