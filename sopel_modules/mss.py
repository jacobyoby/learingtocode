# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('mss')
def speccy(bot, trigger):
	bot.say('Find cheap keys here: https://goo.gl/CxGdNs')
