# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('nocoop')
def speccy(bot, trigger):
	bot.say('You've been helped on the matter and will receive no further help or advice. Thank you for your cooperation.')
