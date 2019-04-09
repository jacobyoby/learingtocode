# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('eff')
def speccy(bot, trigger):
	bot.say('Like our chat? Got help? Want to pay it forward? Consider donating to the Electronic Frontier Foundation! https://supporters.eff.org/donate')
