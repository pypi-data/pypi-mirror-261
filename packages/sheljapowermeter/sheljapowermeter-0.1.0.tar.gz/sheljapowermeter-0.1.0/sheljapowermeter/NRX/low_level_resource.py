import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()
import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter')
import low_level_resource
class initialize_nrx(low_level_resource.initialize):
    def __init__(self, visa_address, instrument):
        super().__init__(visa_address, instrument)

class action_llr_nrx(low_level_resource.action_llr):
    def __init__(self, visa_address,instrument):
       super().__init__(visa_address, instrument)
   
class configure_llr_nrx(low_level_resource.configure_llr):
    def __init__(self, instrument, visa_address,mode,resolution,m):
        super().__init__(instrument, visa_address,mode,resolution,m)
class utility_llr_nrx(low_level_resource.utility_llr):
    def __init__(self,instrument):
       super().__init__(instrument)
        

        
        
        
class closevi_llr_nrx(low_level_resource.closevi_llr):
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