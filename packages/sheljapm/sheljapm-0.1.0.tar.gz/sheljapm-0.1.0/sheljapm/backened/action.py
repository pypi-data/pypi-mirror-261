import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()
class action:
    def __init__(self, visa_address,instrument):
        self.instrument = instrument
        self.visa_address = visa_address
    def read_power_llr(self,m):
        try:
            scpi_command = f"MEAS{m}?"
            kk = self.instrument.query(scpi_command)
            return kk
        except pyvisa.Error as e:
            return str(e)
    def read_freq_llr(self):
        try:
            scpi_command = f"FREQ?"
            kk = self.instrument.query(scpi_command)
            return kk
        except pyvisa.Error as e:
            return str(e)
    def set_unit_llr(self,unit,kk):
        try:
            
            if unit == "DBUV":
                kk = float(kk) + 107.0
            elif unit == "W":
                kk = float(kk) / 10.0
            return kk
        except pyvisa.Error as e:
            return str(e)
    def initiate_meas_llr(self):
        try:
            scpi_command = f"INITiate:IMMediate"
            self.instrument.write(scpi_command)
            return "initiated measurement"
        except pyvisa.Error as e:
            return str(e)
    def fetch_meas_llr(self):
        try:
            scpi_command = f'FETCh?'
            pp=self.instrument.query(scpi_command)
            return str(pp)
        except pyvisa.Error as e:
            return str(e)
    def ini_contd_all_llr(self):
        try:
            scpi_command = f"INITiate:CONTinuous:ALL ON"
            self.instrument.write(scpi_command)
            return "initiated continuous on"
        except pyvisa.Error as e:
            return str(e)
    def disbable_contd_all_llr(self):
        try:
            scpi_command = f"INITiate:IMMediate:ALL OFF"
            self.instrument.write(scpi_command)
            return "disable continuous measurement"
        except pyvisa.Error as e:
            return str(e)
    def abort_all_llr(self):
        try:
            scpi_command = f"ABORt"
            self.instrument.write(scpi_command)
            return "ALL Measurement aborted"
        except pyvisa.Error as e:
            return str(e)