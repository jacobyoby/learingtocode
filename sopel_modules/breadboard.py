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

@commands('breadboard')
def speccy(bot, trigger):
        bot.say('Breadboarding is rebuilding the entire computer outside the case on a table or a wooden breadboard, this should leave you with ONLY the PSU, RAM, CPU w/ heatsink, GPU (Only if you dont have integrated graphics) and motherboard.')
