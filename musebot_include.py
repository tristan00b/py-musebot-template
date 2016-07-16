# -*- coding: utf-8 -*-

from copy import deepcopy
from pyo import Server, OscDataSend, OscDataReceive
from threading import Thread, Timer
from time import sleep

class Musebot(object):

    class Heartbeat:

        def __init__(self, config={}):
            self._del = 5
            self._msg = [config['id']]
            self._osc = OscDataSend(
                's',
                config['mc_listen_port'],
                '/agent/alive',
                host=config['mc_hostname'])

        def beat(self):
            while self._keep_alive:
                self._osc.send(self._msg)
                sleep(self._del)

        def start(self):
            self._keep_alive = True
            self._thread = Thread(target=self.beat)
            self._thread.start()

        def stop(self):
            self._keep_alive = False
            self._thread.join()

    def __init__(self, config_path='config.txt'):
        self.parse_config_file(config_path)
        # init members & properties
        self._server = Server().boot() # do first
        self._gain = None
        self._heartbeat = Musebot.Heartbeat(self._config)
        self._osc_listeners = {}
        self._osc_recv = OscDataReceive(7476, '/', self.osc_listener_callback)
        # register osc listeners
        self.register_osc_listener('/agent/gain', self.gain)
        self.register_osc_listener('/agent/kill', self.shutdown)
        self.register_osc_listener('/agent/quit', self.shutdown)
        self.register_osc_listener('/agent/off',  self.shutdown)

    def parse_config_file(self, config):
        with open(config) as f:
            self._config = {}
            for line in f:
                k,v = line.split()
                if k in {'mc_listen_port', 'my_listen_port', 'output_channels'}:
                    self._config[k] = int(v)
                else:
                    self._config[k] = v

    def do(self):
        '''Implemented in user code'''
        pass

    def run(self):
        self._heartbeat.start()
        self.do()

    def register_osc_listener(self, address, func):
        self._osc_listeners[address] = func
        self._osc_recv.addAddress(address)

    def osc_listener_callback(self, address, *args):
        if address in self._osc_listeners:
            self._osc_listeners[address](args)

    ############################################################################
    # osc callbacks
    #

    def shutdown(self, *args):
        print(self.id+' shutting down!')
        self._heartbeat.stop()
        self._server.stop()
        self._server.closeGui()

    def gain(self, gain, *args):
        self._server.amp = float(gain[0])

    ############################################################################
    # properties
    #

    @property
    def server(self):
        return self._server

    @property
    def config(self):
        return deepcopy(self._config)

    @property
    def id(self):
        return self.config['id']

    @property
    def port(self):
        return self.config['my_listen_port']

    @property
    def hostname(self):
        return self.config['mc_hostname']

    @property
    def hostport(self):
        return self.config['mc_listen_port']

    @property
    def heartbeat(self):
        return self._heartbeat

def main():
    pass

if __name__ == '__main__':
    main()
