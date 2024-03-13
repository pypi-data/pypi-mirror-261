import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()
class close:
    def __init__(self, instrument):
        self.instrument = instrument
    def close_llr(self):
        if self.instrument==None:
         return "instrument not connected"
        try:
            self.instrument.close()
            return "instrument close"
        except pyvisa.Error as e:
            return str(e)