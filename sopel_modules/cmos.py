# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('cmos')
def speccy(bot, trigger):
	bot.say('Resetting cmos means removing the small battery from your motherboard. This resets all your bios settings and fixes a lot of common issues.')
