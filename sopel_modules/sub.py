# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('sub')
def speccy(bot, trigger):
	bot.say('If you don't get the answer you're looking for here, post in our subreddit - https://goo.gl/Jwr6xm')
