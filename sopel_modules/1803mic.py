# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('1803mic')
def speccy(bot, trigger):
	bot.say('Make sure your audio settings match these: https://i.imgur.com/PpASpR2.png')
