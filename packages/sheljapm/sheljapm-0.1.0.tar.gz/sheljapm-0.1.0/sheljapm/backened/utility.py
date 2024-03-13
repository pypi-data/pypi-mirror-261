import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()
class utility:
    def __init__(self,instrument):
        self.instrument = instrument
    def idn_llr(self):
        try:
         return str(self.instrument.query('*IDN?'))
        except pyvisa.Error as e:
            return str(e)
    def rst_llr(self):
        try:
            self.instrument.write("*RST")
            return "Reset successful"
        except pyvisa.Error as e:
            return str(e)
    def opc_llr(self):
        try:
           return str(self.instrument.query('*OPC?'))
        except pyvisa.Error as e:
            return str(e)
    def error_query_llr(self):
        try:
           return str(self.instrument.query(':SYST:ERR?'))
        except pyvisa.Error as e:
            return str(e)