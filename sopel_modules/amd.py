# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('amd')
def speccy(bot, trigger):
	bot.say('Please download your GPU driver from here - https://support.amd.com/en-us/download')
