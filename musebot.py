# -*- coding: utf-8 -*-

from musebot_include import Musebot
from pyo import *

class MyBot(Musebot):

    def __init__(self, config_path='config.txt'):

        # init the base class
        super(MyBot, self).__init__(config_path)

        # init your subclass (e.g. register callbacks)
        # self.register_osc_listener('/mc/time', self.time)

    def time(self, time, *args):
        tempo, t = time
        print(tempo, t%16)

    def do(self):
        '''
        The main processing method.

        You do not need to boot the server from here, this is done in within the
        Musebot base class in order to be able to register OSC listeners
        required by all musebots.

        You are still required to call start(), however, to being audio
        processing. The server is can be accessed via the `server` property
        inherited from Musebot.

        This method should also block when called, which is handled for you by
        calling `server.gui`. Otherwise you would need to devise your own scheme
        for blocking, and possibly override the `shutdown`.
        '''
        s = self.server.start() # server already booted
        a = Sine().out()
        s.gui(locals())



def main():
    mb = MyBot()
    mb.run() # start the musebot

if __name__ == '__main__':
    main()
