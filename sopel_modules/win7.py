# coding=utf-8
"""
PipeItToDevNull

@commands('')
def speccy(bot, trigger):
	bot.say('')
"""
from __future__ import unicode_literals, absolute_import, print_function, division 
 
from sopel.module import commands, example 
from sopel.web import quote

@commands('win7')
def speccy(bot, trigger):
        bot.say('Windows 7 EOLs in January 2020, consider moving to Windows 10 or a Linux OS on weaker hardware.')
