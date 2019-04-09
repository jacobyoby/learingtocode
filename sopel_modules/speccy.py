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


@commands('speccy')
def speccy(bot, trigger):
	bot.say('Please download Speccy from: https://goo.gl/1cf6VV — at the top of the Speccy window, go to File > Publish snapshot. Then, paste the link here.')

