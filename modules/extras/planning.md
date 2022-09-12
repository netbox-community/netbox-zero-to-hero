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