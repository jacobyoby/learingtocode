# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('llcd')
def speccy(bot, trigger):
	bot.say('Please read the following guide to help troubleshoot using a Live Linux Session -- https://www.reddit.com/r/techsupport/wiki/livelinuxsession')
