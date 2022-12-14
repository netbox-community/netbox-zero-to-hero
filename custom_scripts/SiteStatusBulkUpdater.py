from extras.scripts import *

from dcim.models import Device, Site, Rack, Location
from dcim.choices import DeviceStatusChoices, SiteStatusChoices, RackStatusChoices, LocationStatusChoices
from virtualization.choices import VirtualMachineStatusChoices, ClusterStatusChoices
from virtualization.models import VirtualMachine, Cluster

class SiteStatusBulkUpdater(Script):
    class Meta:
        name = "Site Status Bulk Updater"
        description = "Update the status of a Site, and all Locations, racks, devices, clusters and VMs at the updated site"

    site_name = ObjectVar(
        description="Site To Update",
        model=Site,
        required=True
    )
    site_status = ChoiceVar(
        SiteStatusChoices, 
        default=SiteStatusChoices.STATUS_ACTIVE,
        description="Site Status",
        required=True
    )
    location_status = ChoiceVar(
        LocationStatusChoices, 
        default=LocationStatusChoices.STATUS_ACTIVE,
        description="Location Status",
        required=False        
    )
    rack_status = ChoiceVar(
        RackStatusChoices, 
        default=RackStatusChoices.STATUS_ACTIVE,
        description="Rack Status",
        required=False
    )
    device_status = ChoiceVar(
        DeviceStatusChoices, 
        default=DeviceStatusChoices.STATUS_ACTIVE,
        description="Device Status",
        required=False
    )
    cluster_status = ChoiceVar(
        ClusterStatusChoices, 
        default=ClusterStatusChoices.STATUS_ACTIVE,
        description="Cluster Status",
        required=False
    )
    vm_status = ChoiceVar(
        VirtualMachineStatusChoices, 
        default=VirtualMachineStatusChoices.STATUS_ACTIVE,
        description="VM Status",
        required=False
    )

    def run(self, data, commit):

        # Update the site status

        site = Site.objects.get(name=data['site_name'])
        if site.pk and hasattr(site, 'snapshot'):
            site.snapshot()
        site.status=(data['site_status'])
        site.full_clean()
        site.save()
        self.log_success(f"Updated Status of Site {site} to {data['site_status']}")

        # Update all Locations, racks, devices, clusters and VMs at the site

        for location in Location.objects.filter(site=data['site_name']):
            if location.pk and hasattr(site, 'snapshot'):
                location.snapshot()
            location.status=(data['location_status'])
            location.full_clean()
            location.save()
            self.log_success(f"Updated Status of Location {location} to {data['location_status']}")

        for rack in Rack.objects.filter(site=data['site_name']):
            if rack.pk and hasattr(site, 'snapshot'):
                rack.snapshot()
            rack.status=(data['rack_status'])
            rack.full_clean()
            rack.save()
            self.log_success(f"Updated Status of Rack {rack} to {data['rack_status']}")

        for device in Device.objects.filter(site=data['site_name']):
            if device.pk and hasattr(site, 'snapshot'):
                device.snapshot()
            device.status=(data['device_status'])
            device.full_clean()
            device.save()
            self.log_success(f"Updated Status of Device {device} to {data['device_status']}")

        for cluster in Cluster.objects.filter(site=data['site_name']):
            if cluster.pk and hasattr(site, 'snapshot'):
                cluster.snapshot()
            cluster.status=(data['cluster_status'])
            cluster.full_clean()
            cluster.save()
            self.log_success(f"Updated Status of Cluster {cluster} to {data['cluster_status']}")

        for vm in VirtualMachine.objects.filter(site=data['site_name']):
            if vm.pk and hasattr(site, 'snapshot'):
                vm.snapshot()
            vm.status=(data['vm_status'])
            vm.full_clean()
            vm.save()
            self.log_success(f"Updated Status of VM {vm} to {data['vm_status']}")
