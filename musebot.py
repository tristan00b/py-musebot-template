from musebot_include import MusebotBase
from pyo import *

class Musebot(MusebotBase):

  def __init__(self, config_path='config.txt'):
    # init the base class
    super(Musebot, self).__init__(config_path)

    # init your subclass (e.g. register callbacks)
    # self.register_osc_listener('/mc/time', self.time)

  def time(self, time, *args):
    tempo, t = time
    print(tempo, t%16)

  def run(self):
    '''
    The main processing method.

    You do not need to boot the server from here, this is done in within the
    Musebot base class in order to be able to register OSC listeners
    required by all musebots.

    You are still required to call start(), however, to begin audio
    processing (see `main` definition). The audio server can be accessed via
    the `server` property inherited from `Musebot`.

    This method should also block when called. The way to do so is by
    calling `s.gui(locals())`.
    '''
    s = self.server.start() # server already booted
    a = Sine(mul=0.01).mix(2).out()
    s.gui(locals())



def main():
  Musebot().start() # Instantiate bot and start heartbeat

if __name__ == '__main__':
  main()
