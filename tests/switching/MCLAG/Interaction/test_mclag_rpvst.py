import pytest
import lib_mclag_stp as lib_stp
from spytest import st

vars = dict()
stp_protocol = "rpvst"
topology_2_tier = False

@pytest.fixture(scope="module", autouse=True)
def mclag_stp_interaction_module_hooks(request):
    global vars
    vars = st.ensure_min_topology("D1D2:4", "D1D3:3", "D1D4:1", "D1D5:1", "D2D4:3", "D2D3:1", "D3D4:3", "D3D5:1", "D4D5:1", "D1T1:1", "D2T1:1", "D3T1:1", "D4T1:1", "D5T1:1")
    lib_stp.module_config(vars, stp_protocol, topology_2_tier)
    yield
    lib_stp.module_unconfig(stp_protocol)

@pytest.fixture(scope="function", autouse=True)
def mclag_stp_interaction_function_hooks(request):
    lib_stp.update_log_error_flag(True)

    yield

    lib_stp.update_log_error_flag(False)
    lib_stp.check_setup_status()

def test_ft_mclag_with_rpvst_basic_tests():
    if lib_stp.lib_stp_mclag_basic_tests():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_orphan_port_shutdown():
    if lib_stp.lib_stp_mclag_orphan_port_shutdown():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_path_cost():
    if lib_stp.lib_stp_mclag_path_cost():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_rootbridge_multi_instances():
    if lib_stp.lib_stp_mclag_rootbridge_multi_instances():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_mclag_interface_shutdown():
    if lib_stp.lib_stp_mclag_interface_shutdown():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_stp_disable_enable():
    if lib_stp.lib_stp_mclag_disable_enable_stp():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_mclag_unconfig_config():
    if lib_stp.lib_stp_mclag_unconfig_config_mclag():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_failover_tests():
    if lib_stp.lib_stp_mclag_failover_tests():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_both_peers_reload():
    if lib_stp.lib_stp_mclag_both_peers_reload():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_config_reload():
    if lib_stp.lib_stp_mclag_config_reload():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_bpdu_guard():
    if lib_stp.lib_stp_mclag_bpdu_guard():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_interaction_test():
    if lib_stp.lib_stp_mclag_pvst_and_rpvst_interaction():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')

def test_ft_mclag_with_rpvst_peer_link_tests():
    if lib_stp.lib_stp_mclag_peer_link_tests():
       st.report_pass('test_case_passed')
    else:
       st.report_fail('test_case_failed')