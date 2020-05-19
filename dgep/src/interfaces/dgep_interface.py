from interface import Interface

class DGEPInterface(Interface):
    """ Base class for DGEP interfaces; provides only
        the promise of a run method
    """
    def run(self, dgep):
        raise NotImplementedError
