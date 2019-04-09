# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('buildapc')
def speccy(bot, trigger):
	bot.say('We don't do hardware recommendations, do check out /r/buildapc and their live chat for builders advice: https://goo.gl/bDwuHm')
