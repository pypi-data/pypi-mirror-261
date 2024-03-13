#C:\Users\A0510171\Desktop\powermeter\nrx
import sys 
sys.path.insert(0,'C:\\Users\\A0510171\\Desktop\\PoweMeter_n\\NRX')
import action_nrx
import close_nrx
import configure_nrx
import initialize_nrx
import utility_nrx
import configuration
#from high_level import API_nrx,initial_nrx,action_pm_nrx,configure_pm_nrx,utility_pm_nrx,closevi_pm_nrx
instrument=None
visa_address=configuration.lan_address


def test_connection1():
    ob1 = initialize_nrx.initialize_nrx("",instrument)
    error = ob1.initialize5()
    ob2 = initialize_nrx.initialize_nrx(visa_address,instrument) 
    assert ob2.initialize5() != error
def test_idn():
    ob1 = initialize_nrx.initialize_nrx(visa_address,instrument) 
    k=ob1.initialize5()
    it=ob1.instrument
    ob2=utility_nrx.utility_nrx(it)
    assert ob2.idn_llr()==configuration.check_id
def test_rst():
    ob1 = initialize_nrx.initialize_nrx(visa_address,instrument)
    k=ob1.initialize5()
    it=ob1.instrument
    ob2=utility_nrx.utility_nrx(it)
    assert ob2.rst_llr()!=configuration.reset_error
def test_mode():
    ob1 = initialize_nrx.initialize_nrx(visa_address,instrument)
    k=ob1.initialize5()
    it=ob1.instrument
    ob2=configure_nrx.configure_nrx(it,visa_address,'NORMal','I',1)
    assert  ob2.configure_mode_llr() == configuration.completion_command
def test_resol():
    ob1 = initialize_nrx.initialize_nrx(visa_address,instrument)
    k=ob1.initialize5()
    it=ob1.instrument
    ob2=configure_nrx.configure_nrx(it,visa_address,'NORMal','I',1)
    assert  ob2.configure_resolution_llr() == configuration.completion_command
def test_read():
    ob1 = initialize_nrx.initialize_nrx(visa_address,instrument)
    k=ob1.initialize5()
    it=ob1.instrument
    ob2=action_nrx.action_nrx(visa_address,it)
    assert ob2.read_power_llr(2)!= configuration.power_error
def test_close():
    ob1 = initialize_nrx.initialize_nrx(visa_address,instrument)
    k=ob1.initialize5()
    it=ob1.instrument
    ob2=close_nrx.close_nrx(it)
    ob3=close_nrx.close_nrx(instrument)
    error=ob3.close_llr()
    assert ob2.close_llr() != error
