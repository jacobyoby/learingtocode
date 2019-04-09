# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('biz')
def speccy(bot, trigger):
	bot.say('We do not assist with business related queries or support. If you need assistance, please speak to your companys IT department. SA queries can be made in ##reddit-sysadmin')
