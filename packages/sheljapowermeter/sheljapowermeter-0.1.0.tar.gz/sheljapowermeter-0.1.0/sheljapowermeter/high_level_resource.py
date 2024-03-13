from low_level_resource import initialize,utility_llr,closevi_llr,action_llr,configure_llr
import configuration

class initial:
    def __init__(self, instrument, visa_address):
        self.instrument = instrument
        self.visa_address = visa_address

    def initiali(self):
        
        ob1 = initialize(self.visa_address, self.instrument)
        result=ob1.initialize5()
        self.instrument = ob1.instrument  # Update the instrument attribute
        return result
class action_pm:
    def __init__(self, instrument, visa_address):
        self.instrument = instrument
        self.visa_address = visa_address
    def read_power_pm(self,m):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.read_power_llr(m)
    def read_freq_pm(self):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.read_freq_llr()
    def set_unit(self,unit,pow):
        self.unit=unit
        self.pow=pow
        ob1 =  action_llr(self.visa_address, self.instrument)
        return ob1.set_unit_llr(self.unit,self.pow)
    def initiate_meas_pm(self):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.initiate_meas_llr()
    def fetch_meas_pm(self):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.fetch_meas_llr()
    def ini_contd_all_pm(self):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.ini_contd_all_llr()
    def disbable_contd_all_pm(self):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.disbable_contd_all_llr()
    def abort_all_pm(self):
        ob1 = action_llr(self.visa_address, self.instrument)
        return ob1.abort_all_llr()
class configure_pm:
    def __init__(self, instrument, visa_address,mode,resolution,m):
        self.instrument = instrument
        self.visa_address = visa_address
        self.mode=mode
        self.resolution=resolution
       
        self.m=m
    def configure_mode_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure_mode_llr()
    def configure_unit_pm(self,unit):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure_unit_llr(unit)
    def configure_resolution_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure_resolution_llr()
    def configure1_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure1_llr()
    def configure2_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure2_llr()
    def configure3_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure3_llr()
    def configure4_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure4_llr()
    def configure5_pm(self):
        ob1 = configure_llr(self.instrument, self.visa_address,self.mode,self.resolution,self.m)
        return ob1.configure5_llr()
   
        
class utility_pm:
     def __init__(self, instrument):
        self.instrument = instrument
        
     def idn_pm(self):
         ob1= utility_llr(self.instrument)
         return ob1.idn_llr()
     def rst_pm(self):
         ob1=utility_llr(self.instrument)
         return ob1.rst_llr()
     def opc_pm(self):
         ob1=utility_llr(self.instrument)
         return ob1.opc_llr()
     def error_query_pm(self):
         ob1=utility_llr(self.instrument)
         return ob1.error_query_llr()
class closevi_pm:
    def __init__(self, instrument):
        self.instrument = instrument
    def close_pm(self):
         ob1= closevi_llr(self.instrument)
         return ob1.close_llr()


class API:
    def __init__(self,lan_address):
        self.visa_address = lan_address
        self.instrument = None
       
        
    def execute(self):
        self.ob1 = initial(self.instrument, self.visa_address)
        
        kk = self.ob1.initiali()
        self.instrument=self.ob1.instrument
        print(kk)
        print(self.instrument)
        self.ob1=configure_pm(self.instrument,self.visa_address,"FAST","OI",2)
        pp= self.ob1.configure_mode_pm()
        print("wowow ",pp)
        self.ob5 = action_pm(self.instrument,self.visa_address)
        jpg = self.ob5.read_power_pm(2)
        print(jpg)
        kk=self.ob5.set_unit("DBM",jpg)
        print("oihoyee ",kk)
        freq = self.ob5.read_freq_pm()
        print(freq)
        
        jpgq = self.ob5.abort_all_pm()
        print(jpgq)
        
        
        

if __name__ == "__main__":
    api_instance = API(configuration.lan_address)
    api_instance.execute()
    print("power ")