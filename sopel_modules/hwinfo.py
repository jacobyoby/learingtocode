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

@commands('hwinfo')
def speccy(bot, trigger):
        bot.say('Please follow the instructions on this page for logging and hardware stress testing -- https://www.reddit.com/r/techsupport/wiki/hwinfo_logging')
