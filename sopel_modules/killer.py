# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote

@commands('killer')
def speccy(bot, trigger):
	bot.say('Killer NIC drivers are known to cause high memory usage. In the following order: (1) Download the latest drivers from: https://goo.gl/FkJk8t (2) Remove any Killer software using the uninstaller and (3) install your newly downloaded drivers.')
