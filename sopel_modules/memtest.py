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

@commands('memtest')
def speccy(bot, trigger):
        bot.say('To test RAM - https://goo.gl/6zQezq - Download either the Pre-Compiled Bootable ISO to create a bootable optical media, or the Auto-Installer for USB Key, if you wish to create a bootable USB flash drive.')
