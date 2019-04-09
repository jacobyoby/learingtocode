# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('diskpart')
def speccy(bot, trigger):
	bot.say('*WARNING* Will format all data on the selected disk - https://goo.gl/Fvpb3d')
