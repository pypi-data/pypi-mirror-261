import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter_n\\backened')
import  initialize
class initialize_nrx(initialize.initialize):
    def __init__(self, visa_address, instrument):
        super().__init__(visa_address, instrument)
