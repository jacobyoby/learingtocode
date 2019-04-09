# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('oc')
def speccy(bot, trigger):
	bot.say('Overclocking is not advisable due to the risk of system instability, permanent hardware damage, and voiding any warranties. Our support focuses on addressing the underlying performance issues without causing irreparable harm to your devices and components.')
