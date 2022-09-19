# Overall Planning
Company name: TLE Consulting
10 x regional branch sites
2 x regional corporate headquarters, each with an on-premises data center
1 new branch site for project

## Tenants
Tenant Group: Departments
- Sales
- Finance
- IT
- Marketing
- Consulting

## Regions 
- Africa
  - South Africa 
    - Johannesburg
- Asia Pacific
  - Australia
    - Brisbane (planned)
    - Melbourne
    - Sydney
  - New Zealand
    - Auckland
  - Malaysia
    - Kuala Lumpur
- Europe
  - United Kingdom 
    - London
- North America
  - Canada
    - Montreal
  - United States
    - Colorado
      - Denver
    - California
      - Los Angeles
    - Chicago
      - Illinois

## Site Groups, Sites, Locations, Racks, Rack Roles
- Branch
  - ZAJNB01
    - Comms Room
      - Rack R001
        - Infrastructure
  - NZAKL01
    - Comms Room
      - Rack R001
        - Infrastructure
  - MYKUL01 
    - Comms Room
      - Rack R001
        - Infrastructure
  - AUSYD01
    - Comms Room
      - Rack R001
        - Infrastructure
  - AUMEL01
    - Comms Room
      - Rack R001
        - Infrastructure
  - AUBRI01 (planned)
    - Comms Room
      - Rack R001
        - Infrastructure
  - CAMON01  
    - Comms Room
      - Rack R001
        - Infrastructure
  - USDEN01
    - Comms Room
      - Rack R001
        - Infrastructure
  - USLAX01 
    - Comms Room
      - Rack R001
        - Infrastructure
- Corporate
  - UKLON01
    - Data Center
      - Rack R001
        - Infrastructure
      - Rack R002
      - Infrastructure
      - Rack R003
        - Compute  
      - Rack R004
        - Storage
    - Comms Room
      - Rack R005
        - Infrastructure
  - USCHG01
    - Data Center
      - Rack R001
        - Infrastructure
      - Rack R002
      - Infrastructure
      - Rack R003
        - Compute  
      - Rack R004
        - Storage
    - Comms Room
      - Rack R005
        - Infrastructure

## Contact Groups, Roles and Contacts: 
Contact Groups: 
  - IT
  - Facilities Management
  
- Roles:
  - Operations
  - Emergency

- Contacts: 
  - Susan 
  - Eric
  - Alexa 

## New Site
AUBRI01
aubri01
planned
asia pacific - australia - brisbane
branch
australia/brisbane
TLE departments
consulting
30 Mills Street BRISBANE, Queensland(QLD), 4000
-27.611508
152.903083

## Devices
manufacturers
Cisco
Juniper
Panduit
Avocent 

Device Roles
WAN Router
Access Switch
Wireless AP
Patch Panel
Console Server

Platforms
Cisco IOS
Juniper JunOS
Meraki Cloud Managed

devices
patch panel x 1 AUBRI01-PAN-1
router x 1 AUBRI01-RTR-1
switch x 1 AUBRI01-SW-1
AP x 2 AUBRI01-AP-1+2
ISP Router/Circuit
console server AUBRI01-CON-1

Device Types
Cisco ISR4321
Juniper EX4300-48P
Cisco MR56
Avocent ACS16
Panduit CPP48HDEWBL

## 
RIRs and aggregates:
  - RFC1918
  - 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
  
IP roles:
- loopback

Prefix/VLAN Roles:
- Data 
- Voice
- Management
- Corp Wifi
- Guest Wifi 

Prefixes, IP ranges, and IP addresses

VLAN groups

and VLANs

Interface IP address assignments

| Device | Interface | VLAN |
| --- | --- | --- | 
| AUBRI01-RTR-1 | GigabitEthernet0 | AUBRI01_MGMT (50) |
| AUBRI01-RTR-1 | GigabitEthernet0/0/0 | AUBRI01_P2P (60) |
| AUBRI01-SW-1|  me0 | AUBRI01_MGMT (50) |
| AUBRI01-SW-1 | ge-0/0/0 | AUBRI01_P2P (60) |
| AUBRI01-SW-1 | vlan.10 | AUBRI01_DATA (10) |
| AUBRI01-SW-1 | vlan.20 | AUBRI01_VOICE (20) |
| AUBRI01-SW-1 | vlan.30 | AUBRI01_BRANCH_WIFI (30) |
| AUBRI01-SW-1 | vlan.40 | AUBRI01_GUEST_WIFI (40) |
| AUBRI01-SW-1 | vlan.50 | AUBRI01_MGMT (50) |
| AUBRI01-SW-1 | vlan.60 | AUBRI01_P2P (60) |
| AUBRI01-AP-1 |  main | AUBRI01_MGMT (50) |
| AUBRI01-AP-2 |  main | AUBRI01_MGMT (50) |
| AUBRI01-CON-1 | Ethernet | AUBRI01_MGMT (50) |