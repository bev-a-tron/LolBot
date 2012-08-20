#lolbot.py

'''
This bot will make lols to random people on the #hackerschool channel.
'''

import sys
sys.path.append('/Users/administrator/Programming/pyrc')
import pyrc
import pyrc.utils.hooks as hooks
from time import time

class HiBot(pyrc.SpamBot):
    @hooks.command()
    def sayhi(self,channel):
        self.message(channel, "hi!")
class JoeTheClown(pyrc.SpamBot):
    @hooks.command()
    def lol(self,channel):
        self.message(channel, "lol!")
    @hooks.command()
    def sayhi(self,channel):
        self.message(channel, "hi!")

if __name__ == '__main__':
    #bot = HiBot('irc.freenode.net',channels = ['#bevlol'])
    bot = JoeTheClown('irc.freenode.net',channels = ['#bevlol'])
    bot.connect()
