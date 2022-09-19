## Installing Ansible
Ansible runs on Linux based systems, and is installed as a Python package. Follow these steps (they assume Git is already installed and set up on the system):

1. Clone the NetBox Zero to Hero Git repository and change into the Ansible directory:

```
git clone https://github.com/richbibby-NS1/netbox-zero-to-hero.git
cd netbox-zero-to-hero/ansible
```

2. Create a new Python Virtual Environment and activate it: 
```
python3 -m venv .
source bin/activate
```
3. Upgrade PIP (Python package manager) and install Pynetbox (NetBox API client library), and Ansible: 
```
python3 -m pip install --upgrade pip
pip3 install pynetbox
pip3 install ansible
```
4. Set up environment variables for NetBox (these are referenced by the Ansible playbooks):
```
export NETBOX_TOKEN=< YOUR_API_TOKEN >
export NETBOX_API=< YOUR_NETBOX_URL >
```
1. When you have finished working deactivate the Python virtual environment:
```
deactivate
```