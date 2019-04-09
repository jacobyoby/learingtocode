# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('psu')
def speccy(bot, trigger):
	bot.say('https://linustechtips.com/main/topic/631048-psu-tier-list-updated/')
