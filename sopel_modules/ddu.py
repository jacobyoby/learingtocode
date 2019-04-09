# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('ddu')
def speccy(bot, trigger):
	bot.say('To cleanly uninstall your display drivers, launch DDU (Display Driver Uninstaller) in safe mode and select the Clean and Restart option in the DDU window - https://goo.gl/KSoEbJ')
