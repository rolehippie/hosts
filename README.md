# hosts

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/hosts)
[![General Workflow](https://github.com/rolehippie/hosts/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/hosts/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/hosts/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/hosts/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/hosts/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/hosts/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/hosts)](https://github.com/rolehippie/hosts/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.hosts-blue)](https://galaxy.ansible.com/rolehippie/hosts)

Ansible role to manipulate the local hosts configuration.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [fqdn](#fqdn)
  - [hostname](#hostname)
  - [hosts_additions](#hosts_additions)
  - [hosts_ipv4_address](#hosts_ipv4_address)
  - [hosts_ipv6_address](#hosts_ipv6_address)
  - [hosts_reload_services](#hosts_reload_services)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`


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
hosts_ipv4_address: '{{ (ansible_eth0.ipv4.address) if ansible_eth0 is defined else
  (ansible_all_ipv4_addresses | first) }}'
```

### hosts_ipv6_address

IPv6 address of this host

#### Default value

```YAML
hosts_ipv6_address: "{{ (ansible_eth0.ipv6 | map(attribute='address') | first) if\
  \ ansible_eth0 is defined else (ansible_all_ipv6_addresses | first) }}"
```

### hosts_reload_services

List of services to reload on hosts change

#### Default value

```YAML
hosts_reload_services: []
```

## Discovered Tags

**_hosts_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
