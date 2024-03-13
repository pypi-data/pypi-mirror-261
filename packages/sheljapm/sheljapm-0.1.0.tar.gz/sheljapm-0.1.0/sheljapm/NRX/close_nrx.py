import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter_n\\backened')
import close
class close_nrx(close.close):
    def __init__(self,instrument):
        super().__init__(instrument)
