class Interface:
    '''Basic generic parent class for an interface
        Possibly a bit too "death by abstraction" but meh...it's little effort'''

    def __init__(self):
        self.endpoints = {}

    def add_endpoint(source, sink):
        self.endpoints[source] = sink

    def run(self):
        pass
