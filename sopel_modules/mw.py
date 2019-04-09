# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('mw')
def speccy(bot, trigger):
	bot.say('Official Malware Removal Guide - https://www.reddit.com/r/techsupport/comments/33evdi/suggested_reading_official_malware_removal_guide/')
