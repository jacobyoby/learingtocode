#!/bin/bash

echo "# coding=utf-8

from __future__ import unicode_literals, absolute_import, print_function, division

from sopel.module import commands, example
from sopel.web import quote
" > $1.py

echo "@commands('$1')
def speccy(bot, trigger):
	bot.say('$2')" >> $1.py
