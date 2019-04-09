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

@commands('ask')
def speccy(bot, trigger):
        bot.say('Welcome to ##Techsupport! Do not ask for help or specific skills, just state your issue. For verbose descriptions, use a pastebin or a link to your /r/techsupport thread.')
