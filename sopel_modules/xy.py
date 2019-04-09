# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('xy')
def speccy(bot, trigger):
	bot.say('Please ask about your problem, not your solution. For more information to accurately describe what (the hell) it is you want, see this whole page. - https://goo.gl/HqPmxd')
