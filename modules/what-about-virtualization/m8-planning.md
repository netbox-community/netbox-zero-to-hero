M8 planning:

cluster type: 
    VMware vSphere 

cluster: 
    AUBRI01-VSPHERE-1

Devices:
    AUBRI01-VSP-1:
        ProLiant_DL380_Gen9.yaml
    AUBRI01-VSP-2:
        ProLiant_DL380_Gen9.yaml

VM's:
    AUBRI01-SQL-01:
        platform:
            Ubuntu 22.10
        Resources:
            128 GB Memory / 200 GB Disk / 32 CPUs
Services:
    PostgreSQL tcp/5432
    SSH tcp/22

Contacts:
    Susan, Operations, Primary


Steps: 
- fix vlan.10 and vlan.20 ip assignments to 192.168.0.1/25 abd 192.168.0.129/25
- add physical servers
  - add manufacturer - HPE
  - add device role - vSphere, green
  - add device type - HPE ProLiant DL380 Gen9
  - add devices to rack - position x and y - bulk upload
  - add connections (1m, green, cat6) - bulk upload
    - AUBRI01-VSP-1
      - iLO --> ge-0/0/44
      - Gig-E 1 --> ge-0/0/1
      - Gig-E 2 --> ge-0/0/2
    - AUBRI01-VSP-2
      - iLO --> ge-0/0/45
      - Gig-E 1 --> ge-0/0/3
      - Gig-E 2 --> ge-0/0/4
  - add LAG interfaces ae0 and ae1
  - add switch port 802.1q + descriptions
- add platform 
- add cluster type
- add cluster 
- assign devices
- add vm
- add vm interface (eth0)
- assign IP to vm interface from vlan 10 (via prefixes, 192.168.0.0/25 data vlan)
- add service templates
- add service, assign to VM, from template, IP address, description 'Brisbane PostgresSQL Server'
- add contact - Susan, Operations, Primary