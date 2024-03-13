#C:\Users\A0510171\Desktop\PoweMeter_n\NRX

import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter_n\\NRX')
import action_nrx
import close_nrx
import configure_nrx
import initialize_nrx
class API_nrx:
    def __init__(self,lan_address):
        self.visa_address = lan_address
        self.instrument = None
    def execute(self):
        self.ob1 = initialize_nrx.initialize_nrx(self.visa_address,self.instrument)
        kk = self.ob1.initialize5()
        self.instrument=self.ob1.instrument
        print(kk)
        print(self.instrument)
       
        self.ob5 = action_nrx.action_nrx(self.visa_address,self.instrument)
        jpg = self.ob5.read_power_llr(2)
        print(jpg)
        freq = self.ob5.read_freq_llr()
        print(freq)
        jpgq = self.ob5.abort_all_llr()
        print(jpgq)
        pl=self.ob6=close_nrx.close_nrx(self.instrument)
        print(pl)
       
if __name__ == "__main__":
    api_instance = API_nrx("TCPIP0::10.24.66.241::inst0::INSTR")
    api_instance.execute()
    print("power ")
        
        
