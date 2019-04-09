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

@commands('dw')
def speccy(bot, trigger):
        bot.say('"Doesnt work" does not convey any meaningful information, please see here on how to properly ask a question: http://www.catb.org/~esr/faqs/smart-questions.html#beprecise')
