

vm oob-mgmt-server netq-1.3.0 2 10 40

vm juniper01 cumulus-vx-3.7.2 1 2 2

vm spine05 cumulus-vx-3.7.2 1 2 2
vm spine06 cumulus-vx-3.7.2 1 2 2
vm spine07 cumulus-vx-3.7.2 1 2 2
vm spine08 cumulus-vx-3.7.2 1 2 2

vm leaf50 cumulus-vx-3.7.2 1 2 2
vm leaf51 cumulus-vx-3.7.2 1 2 2
#vm leaf52 cumulus-vx-3.7.2 1 2 2
#vm leaf53 cumulus-vx-3.7.2 1 2 2
#vm leaf54 cumulus-vx-3.7.2 1 2 2
#vm leaf55 cumulus-vx-3.7.2 1 2 2
#vm leaf56 cumulus-vx-3.7.2 1 2 2

vm leaf60 cumulus-vx-3.7.2 1 2 2
vm leaf61 cumulus-vx-3.7.2 1 2 2
#vm leaf62 cumulus-vx-3.7.2 1 2 2
#vm leaf63 cumulus-vx-3.7.2 1 2 2
#vm leaf64 cumulus-vx-3.7.2 1 2 2
#vm leaf65 cumulus-vx-3.7.2 1 2 2
#vm leaf66 cumulus-vx-3.7.2 1 2 2


vm server01 ubuntu-16.04 2 4 4
vm server02 ubuntu-16.04 2 4 4
#vm server03 ubuntu-16.04 2 4 4
#vm server04 ubuntu-16.04 2 4 4
#vm server05 ubuntu-16.04 2 4 4
#vm server06 ubuntu-16.04 2 4 4
#vm server07 ubuntu-16.04 2 4 4

vm outside01 ubuntu-16.04 2 4 4

network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server http eth0 80 TCP public
service oob-mgmt-server https eth0 443 TCP public
service oob-mgmt-server http2 eth0 1337 TCP public
service oob-mgmt-server grafana eth0 3000 TCP public
service oob-mgmt-server novnc eth0 6080 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server mesos eth0 5050 TCP public
service oob-mgmt-server marathon eth0 8080 TCP public
service oob-mgmt-server mesosapp eth0 8088 TCP public

network oob-mgmt-server eth1 172.16.83.254 255.255.252.0

network juniper01 eth0 172.16.82.1 255.255.252.0

network spine05 eth0 172.16.82.105 255.255.252.0
network spine06 eth0 172.16.82.106 255.255.252.0
network spine07 eth0 172.16.82.107 255.255.252.0
network spine08 eth0 172.16.82.108 255.255.252.0

network leaf50 eth0 172.16.82.150 255.255.252.0
network leaf51 eth0 172.16.82.151 255.255.252.0
#network leaf52 eth0 172.16.82.152 255.255.252.0
#network leaf53 eth0 172.16.82.153 255.255.252.0
#network leaf54 eth0 172.16.82.154 255.255.252.0
#network leaf55 eth0 172.16.82.155 255.255.252.0
#network leaf56 eth0 172.16.82.156 255.255.252.0

network leaf60 eth0 172.16.82.160 255.255.252.0
network leaf61 eth0 172.16.82.161 255.255.252.0
#network leaf62 eth0 172.16.82.162 255.255.252.0
#network leaf63 eth0 172.16.82.163 255.255.252.0
#network leaf64 eth0 172.16.82.164 255.255.252.0
#network leaf65 eth0 172.16.82.165 255.255.252.0
#network leaf66 eth0 172.16.82.166 255.255.252.0

network server01 eth0 172.16.83.1 255.255.252.0
network server02 eth0 172.16.83.2 255.255.252.0
#network server03 eth0 172.16.83.3 255.255.252.0
#network server04 eth0 172.16.83.4 255.255.252.0
#network server05 eth0 172.16.83.5 255.255.252.0
#network server06 eth0 172.16.83.6 255.255.252.0
#network server07 eth0 172.16.83.7 255.255.252.0

network outside01 eth0 172.16.83.8 255.255.252.0

autoconfig oob-mgmt-server

# Juniper to Spines
connect juniper01 swp1 spine05 swp29
connect juniper01 swp2 spine05 swp30
connect juniper01 swp3 spine05 swp31
connect juniper01 swp4 spine05 swp32

connect juniper01 swp5 spine06 swp29
connect juniper01 swp6 spine06 swp30
connect juniper01 swp7 spine06 swp31
connect juniper01 swp8 spine06 swp32

connect juniper01 swp9 spine07 swp29
connect juniper01 swp10 spine07 swp30
connect juniper01 swp11 spine07 swp31
connect juniper01 swp12 spine07 swp32

connect juniper01 swp13 spine08 swp29
connect juniper01 swp14 spine08 swp30
connect juniper01 swp15 spine08 swp31
connect juniper01 swp16 spine08 swp32


# Leafs to Spines
connect leaf50 swp49 spine05 swp1 
connect leaf50 swp50 spine05 swp2
connect leaf50 swp51 spine06 swp1 
connect leaf50 swp52 spine06 swp2
connect leaf50 swp53 spine07 swp1 
connect leaf50 swp54 spine07 swp2
connect leaf50 swp55 spine08 swp1 
connect leaf50 swp56 spine08 swp2

connect leaf51 swp49 spine05 swp3 
connect leaf51 swp50 spine05 swp4
connect leaf51 swp51 spine06 swp3 
connect leaf51 swp52 spine06 swp4
connect leaf51 swp53 spine07 swp3 
connect leaf51 swp54 spine07 swp4
connect leaf51 swp55 spine08 swp3 
connect leaf51 swp56 spine08 swp4

#connect leaf52 swp49 spine05 swp5 
#connect leaf52 swp50 spine05 swp6
#connect leaf52 swp51 spine06 swp5 
#connect leaf52 swp52 spine06 swp6
#connect leaf52 swp53 spine07 swp5 
#connect leaf52 swp54 spine07 swp6
#connect leaf52 swp55 spine08 swp5 
#connect leaf52 swp56 spine08 swp6

#connect leaf53 swp49 spine05 swp7 
#connect leaf53 swp50 spine05 swp8
#connect leaf53 swp51 spine06 swp7 
#connect leaf53 swp52 spine06 swp8
#connect leaf53 swp53 spine07 swp7 
#connect leaf53 swp54 spine07 swp8
#connect leaf53 swp55 spine08 swp7 
#connect leaf53 swp56 spine08 swp8

#connect leaf54 swp49 spine05 swp9 
#connect leaf54 swp50 spine05 swp10
#connect leaf54 swp51 spine06 swp9
#connect leaf54 swp52 spine06 swp10
#connect leaf54 swp53 spine07 swp9
#connect leaf54 swp54 spine07 swp10
#connect leaf54 swp55 spine08 swp9
#connect leaf54 swp56 spine08 swp10

#connect leaf55 swp49 spine05 swp11 
#connect leaf55 swp50 spine05 swp12
#connect leaf55 swp51 spine06 swp11 
#connect leaf55 swp52 spine06 swp12
#connect leaf55 swp53 spine07 swp11 
#connect leaf55 swp54 spine07 swp12
#connect leaf55 swp55 spine08 swp11 
#connect leaf55 swp56 spine08 swp12

#connect leaf56 swp49 spine05 swp13 
#connect leaf56 swp50 spine05 swp14
#connect leaf56 swp51 spine06 swp13 
#connect leaf56 swp52 spine06 swp14
#connect leaf56 swp53 spine07 swp13 
#connect leaf56 swp54 spine07 swp14
#connect leaf56 swp55 spine08 swp13 
#connect leaf56 swp56 spine08 swp14



connect leaf60 swp49 spine05 swp15 
connect leaf60 swp50 spine05 swp16
connect leaf60 swp51 spine06 swp15 
connect leaf60 swp52 spine06 swp16
connect leaf60 swp53 spine07 swp15 
connect leaf60 swp54 spine07 swp16
connect leaf60 swp55 spine08 swp15 
connect leaf60 swp56 spine08 swp16

connect leaf61 swp49 spine05 swp17
connect leaf61 swp50 spine05 swp18
connect leaf61 swp51 spine06 swp17
connect leaf61 swp52 spine06 swp18
connect leaf61 swp53 spine07 swp17
connect leaf61 swp54 spine07 swp18
connect leaf61 swp55 spine08 swp17
connect leaf61 swp56 spine08 swp18

#connect leaf62 swp49 spine05 swp19
#connect leaf62 swp50 spine05 swp20
#connect leaf62 swp51 spine06 swp19
#connect leaf62 swp52 spine06 swp20
#connect leaf62 swp53 spine07 swp19
#connect leaf62 swp54 spine07 swp20
#connect leaf62 swp55 spine08 swp19
#connect leaf62 swp56 spine08 swp20

#connect leaf63 swp49 spine05 swp21
#connect leaf63 swp50 spine05 swp22
#connect leaf63 swp51 spine06 swp21
#connect leaf63 swp52 spine06 swp22
#connect leaf63 swp53 spine07 swp21
#connect leaf63 swp54 spine07 swp22
#connect leaf63 swp55 spine08 swp21
#connect leaf63 swp56 spine08 swp22

#connect leaf64 swp49 spine05 swp23
#connect leaf64 swp50 spine05 swp24
#connect leaf64 swp51 spine06 swp23
#connect leaf64 swp52 spine06 swp24
#connect leaf64 swp53 spine07 swp23
#connect leaf64 swp54 spine07 swp24
#connect leaf64 swp55 spine08 swp23
#connect leaf64 swp56 spine08 swp24

#connect leaf65 swp49 spine05 swp25 
#connect leaf65 swp50 spine05 swp26
#connect leaf65 swp51 spine06 swp25 
#connect leaf65 swp52 spine06 swp26
#connect leaf65 swp53 spine07 swp25 
#connect leaf65 swp54 spine07 swp26
#connect leaf65 swp55 spine08 swp25 
#connect leaf65 swp56 spine08 swp26

#connect leaf66 swp49 spine05 swp27 
#connect leaf66 swp50 spine05 swp28
#connect leaf66 swp51 spine06 swp27 
#connect leaf66 swp52 spine06 swp28
#connect leaf66 swp53 spine07 swp27 
#connect leaf66 swp54 spine07 swp28
#connect leaf66 swp55 spine08 swp27 
#connect leaf66 swp56 spine08 swp28


# Peerlinks
connect leaf50 swp47 leaf60 swp47
connect leaf50 swp48 leaf60 swp48

connect leaf51 swp47 leaf61 swp47
connect leaf51 swp48 leaf61 swp48

#connect leaf52 swp47 leaf62 swp47
#connect leaf52 swp48 leaf62 swp48

#connect leaf53 swp47 leaf63 swp47
#connect leaf53 swp48 leaf63 swp48

#connect leaf54 swp47 leaf64 swp47
#connect leaf54 swp48 leaf64 swp48

#connect leaf55 swp47 leaf65 swp47
#connect leaf55 swp48 leaf65 swp48

#connect leaf56 swp47 leaf66 swp47
#connect leaf56 swp48 leaf66 swp48


# Servers - 1 in each rack, connected to swp25 of its leafs.
connect server01 eth1 leaf50 swp25
connect server01 eth2 leaf60 swp25

connect server02 eth1 leaf51 swp25
connect server02 eth2 leaf61 swp25

#connect server03 eth1 leaf52 swp25
#connect server03 eth2 leaf62 swp25

#connect server04 eth1 leaf53 swp25
#connect server04 eth2 leaf63 swp25

#connect server05 eth1 leaf54 swp25
#connect server05 eth2 leaf64 swp25

#connect server06 eth1 leaf55 swp25
#connect server06 eth2 leaf65 swp25

#connect server07 eth1 leaf56 swp25
#connect server07 eth2 leaf66 swp25

# Outside connect to Juniper
connect outside01 eth1 juniper01 swp17

