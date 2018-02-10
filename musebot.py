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

    You do not need to boot the server, this is done in within the base class in
    order to be able to register OSC listeners required by all musebots.

    To begin audio processing, call `start()` on the audio server, accessesed
    via the `server` property inherited from `MusebotBase`.

    This thread should also block in order to prevent the bot from shutting down
    prematurely. The easiest method is to call `gui(locals())` on the audio
    server, as demonstrated below.
    '''
    s = self.server.start() # server already booted
    a = Sine(mul=0.01).mix(2).out()
    s.gui(locals())



def main():
  Musebot().start() # Instantiate bot and start heartbeat

if __name__ == '__main__':
  main()
