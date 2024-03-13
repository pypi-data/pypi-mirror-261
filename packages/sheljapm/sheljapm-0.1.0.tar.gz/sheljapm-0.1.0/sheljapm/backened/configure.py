import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()
class configure:
    def __init__(self, instrument, visa_address,mode,resolution,m):
        self.instrument = instrument
        self.visa_address = visa_address
        self.mode=mode
        self.resolution=resolution
        self.m=m
    
    def configure_mode_llr(self):
        try:
            if self.mode == "NORMal":
                self.instrument.write('SYSTem:SPEed NORMal')
            elif self.mode== "FAST":
                self.instrument.write('SYSTem:SPEed FAST')
            elif self.mode == "SLOW":
                self.instrument.write('SYSTem:SPEed SLOW')
            else:
                self.instrument.write('SYSTem:SPEed FREeze')
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure_unit_llr(self,unit):
        try:
            if unit == "DBM":
                self.instrument.write(f'UNIT{self.m}:POW DBM')
            elif self.mode== "W":
                self.instrument.write(f'UNIT{self.m}:POW W')
            elif self.mode == "DBUV":
                self.instrument.write(f'UNIT{self.m}:POW DBµV')
            else:
                self.instrument.write(f'UNIT{self.m}:POW DBM')
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure_resolution_llr(self):
        try:
            if self.resolution == "I":
                self.instrument.write(f'CALCulate{self.m}:RESolution I')
            elif self.resolution == "OI":
                self.instrument.write(f'CALCulate{self.m}:RESolution OI')
            elif self.resolution == "OOI":
                self.instrument.write(f'CALCulate{self.m}:RESolution OOI')
            else:
                self.instrument.write(f'CALCulate{self.m}:RESolution OOOI')
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure1_llr(self):
        try:
            self.instrument.write(f"CALCulate{self.m}:TSLot:TIMing:EXCLude:STOP")
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure2_llr(self):
        try:
            self.instrument.write(f"CALCulate{self.m}:STATistics[:SCALe]:X:RLEVel[:ABSolute]")
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure3_llr(self):
        try:
            self.instrument.write(f"CALCulate{self.m}:STATistics:APERture")
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure4_llr(self):
        try:
            self.instrument.write(f"CALCulate<Measurement>:TSLot:TIMing:EXCLude:STARt")
            return "Done"
        except pyvisa.Error as e:
            return str(e)
    def configure5_llr(self):
        try:
            self.instrument.write(f"CALCulate<Measurement>:TSLot:TIMing:EXCLude:STOP")
            return "Done"
        except pyvisa.Error as e:
            return str(e)
        