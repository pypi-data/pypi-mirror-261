import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter')
import high_level_resource
import datetime


class initial_nrx(high_level_resource.initial):
    def __init__(self, instrument, visa_address):
        super().__init__( instrument, visa_address)
       

class action_pm_nrx(high_level_resource.action_pm):
    def __init__(self, instrument, visa_address):
        super().__init__( instrument, visa_address)
        
class configure_pm_nrx(high_level_resource.configure_pm):
    def __init__(self, instrument, visa_address,mode,resolution,m):
        super().__init__(instrument, visa_address,mode,resolution,m)
        
        
class utility_pm_nrx(high_level_resource.utility_pm):
     def __init__(self, instrument):
        super().__init__( instrument)
        
class closevi_pm_nrx(high_level_resource.closevi_pm):
    def __init__(self, instrument):
        super().__init__(instrument)
        
class API_nrx():
    def __init__(self,lan_address):
        self.visa_address = lan_address
        self.instrument = None
        self.ob1 = initial_nrx(self.instrument, self.visa_address)
        kk = self.ob1.initiali()
        self.instrument=self.ob1.instrument
    def execute(self):
        self.ob2=action_pm_nrx(self.instrument,self.visa_address)
        p1=self.ob2.read_power_pm(1)
        self.ob3=closevi_pm_nrx(self.instrument)
        p2=self.ob3.close_pm()
        
if __name__ == "__main__":
    logstarttime =datetime.datetime.now()
    print(logstarttime)
    for i in range(100):
     api_instance = API_nrx("TCPIP0::10.24.66.241::inst0::INSTR")
     pp=api_instance.execute()      
    stoptime=datetime.datetime.now()
    print(stoptime)
    print(stoptime-logstarttime)



        
'''self.ob2=configure_pm_nrx(self.instrument,self.visa_address,"NORMal","I",1)
        kk=self.ob2.configure_mode_pm()
        print(kk)
        pp=self.ob2.configure_unit_pm("W")
        print(pp)
        self.ob6 = utility_pm_nrx(self.instrument)
        ppo=self.ob6.rst_pm()
        print(ppo)
        #self.instrument.write(f'UNIT3:POW W')
        self.ob5 = action_pm_nrx(self.instrument,self.visa_address)
        
        kkk=self.ob6.error_query_pm()
        print(kkk)
        jpg = self.ob5.read_power_pm(1)
        print(jpg)
        jpgg = self.ob5.read_power_pm(2)
        print(jpgg)
        jpggg = self.ob5.read_power_pm(3)
        print(jpggg)'''
    
        
        
        



    