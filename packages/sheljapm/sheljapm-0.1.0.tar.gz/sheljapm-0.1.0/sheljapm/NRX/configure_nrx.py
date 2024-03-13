import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter_n\\backened')
import  configure
class configure_nrx(configure.configure):
    def __init__(self, instrument, visa_address,mode,resolution,m):
        super().__init__(instrument, visa_address,mode,resolution,m)
