# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('tos')
def speccy(bot, trigger):
	bot.say('Anything that violates other's privacy or breaks terms and agreements are not allowed.')
