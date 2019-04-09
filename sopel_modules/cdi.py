# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('cdi')
def speccy(bot, trigger):
	bot.say('Download Crystal Disk Info - At the top of the programs window go to Edit > Copy then pastebin the contents - https://goo.gl/Rxm3dF')
