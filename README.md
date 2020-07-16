# hosts

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/hosts/status.svg)](https://cloud.drone.io/rolehippie/hosts)

Ansible role to configure hosts

## Table of content

* [Default Variables](#default-variables)
  * [fqdn](#fqdn)
  * [hostname](#hostname)
  * [hosts_additions](#hosts_additions)
  * [hosts_ipv4_address](#hosts_ipv4_address)
  * [hosts_ipv6_address](#hosts_ipv6_address)
  * [hosts_reload_services](#hosts_reload_services)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### fqdn

Fully qualified domain name for this host

#### Default value

```YAML
fqdn: '{{ ansible_fqdn }}'
```

### hostname

Hostname for this host

#### Default value

```YAML
hostname: '{{ inventory_hostname }}'
```

### hosts_additions

Additional entries for hosts config

#### Default value

```YAML
hosts_additions: []
```

#### Example usage

```YAML
hosts_additions:
  - 192.168.1.10 host1
  - 192.168.1.20 host2
  - 192.168.1.30 host3
```

### hosts_ipv4_address

IPv4 address of this host

#### Default value

```YAML
hosts_ipv4_address: '{{ ansible_eth0.ipv4.address }}'
```

### hosts_ipv6_address

IPv6 address of this host

#### Default value

```YAML
hosts_ipv6_address: "{{ ansible_eth0.ipv6 | map(attribute='address') | first }}"
```

### hosts_reload_services

List of services to reload on hosts change

#### Default value

```YAML
hosts_reload_services: []
```

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
