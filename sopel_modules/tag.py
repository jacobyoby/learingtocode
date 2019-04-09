# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('tag')
def speccy(bot, trigger):
	bot.say('To tag other users - Start by typing the first few letters of their name and press tab to autocomplete the rest.')
