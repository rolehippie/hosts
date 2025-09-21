import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_dummy(host):
    assert True

# def test_hosts_file(host):
#     file = host.file("/etc/hosts")
#     assert file.contains("192.168.1.1 example.com")
