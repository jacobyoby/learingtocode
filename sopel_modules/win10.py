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

@commands('win10')
def speccy(bot, trigger):
        bot.say('Use Microsofts Media Creation Tool and select your bootable device (USB or burnable DVD) to install windows 10 from - https://goo.gl/Wn3duz')
