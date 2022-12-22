import re

from dcim.choices import DeviceStatusChoices
from dcim.models import Device
from extras.reports import Report

# A modified John Anderson's NetBox Day 2020 Presentation by adding a check for all sites, not just LAX
# All credit goes to @lampwins

class DeviceHostnameReport(Report):
   description = "Verify each device conforms to naming convention Example: (site_name)-RTR-1 or (site_name)-SW-2"

   def test_device_naming(self):
       for device in Device.objects.filter(status=DeviceStatusChoices.STATUS_ACTIVE):
           # Change the naming standard based on the re.match
           if re.match(str(device.site.name) + "-[a-zA-Z]+-[0-9]+", str(device.name), re.IGNORECASE):
               self.log_success(device)
           else:
               self.log_failure(device, "Hostname does not conform to standard!")