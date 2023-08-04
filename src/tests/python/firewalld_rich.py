#!/usr/bin/python
# SPDX-License-Identifier: GPL-2.0-or-later
#
# Copyright (C) 2013 Red Hat, Inc.
#
# Authors:
# Jiri Popelka <jpopelka@redhat.com>

# To use in git tree: PYTHONPATH=.. python firewalld-test.py

import dbus

from firewall.client import FirewallClientConfig, FirewallClientZoneSettings

bus = dbus.SystemBus()
fw_config = FirewallClientConfig(bus)

rule = ['rule service name=ftp audit limit value="1/m" accept ',
        'rule protocol value=ah accept ',
        'rule protocol value=esp accept ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone1", zone.settings)
nz.remove()

rule = ['rule family=ipv4 source address="192.168.0.0/24" service name=tftp log prefix=tftp level=info limit value=1/m accept']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone2", zone.settings)
nz.remove()

rule = ['rule family=ipv4 source not address=192.168.0.0/24 service name=dns log prefix=dns level=info limit value=2/m accept ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone3", zone.settings)
nz.remove()

rule = ['rule family=ipv6 source address=1:2:3:4:6:: service name=radius log prefix=dns level=info limit value=3/m reject limit value=20/m ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone4", zone.settings)
nz.remove()

rule = ['rule family=ipv6 source address=1:2:3:4:5:: port port=4011 protocol=tcp log prefix="port 4011/tcp" level=info limit value=4/m drop ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone5", zone.settings)
nz.remove()

rule = ['rule family=ipv6 source address=1:2:3:4:6:: forward-port port=4011 protocol=tcp to-port=4012 to-addr=1::2:3:4:7 ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone6", zone.settings)
nz.remove()

rule = ['rule family=ipv4 source address=192.168.0.0/24 icmp-block name=source-quench log level=info prefix=source-quench limit value=4/m ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone7", zone.settings)
nz.remove()

rule = ['rule family=ipv6 source address=1:2:3:4:6:: icmp-block name=redirect log prefix=redirect level=info limit value=4/m ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone8", zone.settings)
nz.remove()

rule = ['rule family=ipv4 source address=192.168.1.0/24 masquerade ',
        'rule family=ipv6 masquerade ']
zone = FirewallClientZoneSettings()
zone.setRichRules(rule)
nz = fw_config.addZone("zone9", zone.settings)
nz.remove()
