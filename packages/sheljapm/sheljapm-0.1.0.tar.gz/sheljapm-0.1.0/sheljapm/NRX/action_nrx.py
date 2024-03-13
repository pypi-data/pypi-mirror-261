#C:\Users\A0510171\Desktop\PoweMeter_n\backened
import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter_n\\backened')
import action
class action_nrx(action.action):
    def __init__( self,visa_address,instrument):
        super().__init__(visa_address,instrument)


