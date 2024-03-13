#C:\Users\A0510171\Desktop\powermeter\nrx
import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter')
import high_level_resource
#from high_level import API_nrx,initial_nrx,action_pm_nrx,configure_pm_nrx,utility_pm_nrx,closevi_pm_nrx
import configuration
powermeter = high_level_resource.API("TCPIP0::10.24.66.241::inst0::INSTR")
instrument = powermeter.instrument
visa_address = powermeter.visa_address


def test_connection1():
    powermeter.ob1 = high_level_resource.initial(instrument, "")
    error = powermeter.ob1.initiali()
    powermeter.ob2 = high_level_resource.initial(instrument, visa_address)    
    assert powermeter.ob2.initiali() != error
def test_idn():
    powermeter.ob1 = high_level_resource.initial(instrument, visa_address)
    k=powermeter.ob1.initiali()
    it=powermeter.ob1.instrument
    powermeter.ob2=high_level_resource.utility_pm(it)
    assert powermeter.ob2.idn_pm()==configuration.check_id
def test_rst():
    powermeter.ob1 = high_level_resource.initial(instrument, visa_address)
    k=powermeter.ob1.initiali()
    it=powermeter.ob1.instrument
    powermeter.ob2=high_level_resource.utility_pm(it)
    assert powermeter.ob2.rst_pm()!=configuration.reset_error
def test_mode():
    powermeter.ob1 = high_level_resource.initial(instrument, visa_address)
    k=powermeter.ob1.initiali()
    it=powermeter.ob1.instrument
    powermeter.ob2=high_level_resource.configure_pm(it,visa_address,"NORMal",'I',1)
    assert  powermeter.ob2.configure_mode_pm() == configuration.completion_command
def test_resol():
    powermeter.ob1 = high_level_resource.initial(instrument, visa_address)
    k=powermeter.ob1.initiali()
    it=powermeter.ob1.instrument
    powermeter.ob2=high_level_resource.configure_pm(it,visa_address,"NORMal",'I',1)
    assert  powermeter.ob2.configure_resolution_pm() == configuration.completion_command
def test_read():
    powermeter.ob1 = high_level_resource.initial(instrument, visa_address)
    k=powermeter.ob1.initiali()
    it=powermeter.ob1.instrument
    powermeter.ob2=high_level_resource.action_pm(it,visa_address)
    assert powermeter.ob2.read_power_pm(2)!= configuration.power_error
def test_close():
    powermeter.ob1 = high_level_resource.initial(instrument, visa_address)
    k=powermeter.ob1.initiali()
    it=powermeter.ob1.instrument
    powermeter.ob2=high_level_resource.closevi_pm(it)
    powermeter.ob3=high_level_resource.closevi_pm(instrument)
    error=powermeter.ob3.close_pm()
    assert powermeter.ob2.close_pm != error
