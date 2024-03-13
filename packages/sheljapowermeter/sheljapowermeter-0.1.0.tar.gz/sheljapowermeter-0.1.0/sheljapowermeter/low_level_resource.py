import pyvisa
from pyvisa.errors import VisaIOError

rm = pyvisa.ResourceManager()

class initialize:
    def __init__(self, visa_address, instrument):
        self.visa_address = visa_address
        self.instrument = instrument

    def initialize5(self):
        
        try:
            self.instrument = rm.open_resource(self.visa_address, timeout=10000)
            
            instrument=self.instrument
            
            return "Instrument connected"
        except VisaIOError as e:
             return str(e)
class action_llr:
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
class configure_llr:
    def __init__(self, instrument, visa_address,mode,resolution,m):
        self.instrument = instrument
        self.visa_address = visa_address
        self.mode=mode
        self.resolution=resolution
        self.m=m
    
    def configure_mode_llr(self):
        try:
            if self.mode == "NORMal":
                self.instrument.write(f'SYSTem:SPEed NORMal')
            elif self.mode== "FAST":
                self.instrument.write(f'SYSTem:SPEed FAST')
            elif self.mode == "SLOW":
                self.instrument.write(f'SYSTem:SPEed SLOW')
            else:
                self.instrument.write(f'SYSTem:SPEed FREeze')
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
        
class utility_llr:
    def __init__(self,instrument):
        self.instrument = instrument
    def idn_llr(self):
        try:
         return str(self.instrument.query('*IDN?'))
        except pyvisa.Error as e:
            return str(e)
    def rst_llr(self):
        try:
            self.instrument.write("*RST")
            return "Reset successful"
        except pyvisa.Error as e:
            return str(e)
    def opc_llr(self):
        try:
           return str(self.instrument.query('*OPC?'))
        except pyvisa.Error as e:
            return str(e)
    def error_query_llr(self):
        try:
           return str(self.instrument.query(':SYST:ERR?'))
        except pyvisa.Error as e:
            return str(e)
        
class read1:
    def __init__(self, visa_address, instrument):
        self.visa_address = visa_address
        self.instrument = instrument

    def read_power1(self):
        try:
            scpi_command = f"MEAS1?"
            kk = self.instrument.query(scpi_command)
            return kk
        except pyvisa.Error as e:
            return str(e)
        
        
        
class closevi_llr:
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


'''
 if unit == "W":
                self.instrument.write(f'UNIT{self.m}:POW W')
            elif unit == "W":
                self.instrument.write(f'UNIT{self.m}:POW DBM')
            elif unit == "DBUV":
                self.instrument.write(f'UNIT{self.m}:POW DBµV)
            return "Done"
'''
        
    
    
    