import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()
class initialize:
    def __init__(self, visa_address, instrument):
        self.visa_address = visa_address
        self.instrument = instrument

    def initialize5(self):
        
        try:
            self.instrument = rm.open_resource(self.visa_address, timeout=10000)
            
            instrument=self.instrument
            
            return "Instrument connected"
        except VisaIOError as e:
             return str(e)
    