# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('safemode')
def speccy(bot, trigger):
	bot.say('To get into safe mode - Click Start > Settings cog > Update & Security > Recovery > Advanced start-up > Restart now')
