# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division 
 
from sopel.module import commands, example 
from sopel.web import quote

@commands('cleanboot')
def speccy(bot, trigger):
        bot.say('To clean boot Windows - Open up msconfig.exe and follow this: https://goo.gl/yRBY1Y')
