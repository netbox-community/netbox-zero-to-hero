from dcim.choices import DeviceStatusChoices
from dcim.models import Device
from extras.reports import Report

class DeviceIPReport(Report):
    description = "Check that every device has either an IPv4 or IPv6 primary address assigned"

    def test_primary_ip4(self):
        for device in Device.objects.filter(status=DeviceStatusChoices.STATUS_ACTIVE):
            intcount = 0
            for interface in device.interfaces.all():
                if not interface.mgmt_only:
                    intcount += 1
            # There may be dumb devices with no interfaces so no IP addresses, that's OK
            if intcount == 0:
                if device.primary_ip4_id is not None:
                    if device.primary_ip6_id is not None:
                        self.log_failure(device, "Device has primary IPv4 and IPv6 address but no interfaces")
                    else:
                        self.log_warning(device, "Device has missing primary IPv4 addresses but no interfaces")
                else:
                    self.log_success(device)
            elif device.primary_ip4_id is None:
                if device.device_type.is_child_device is True:
                    self.log_success(device)
                else:
                    if device.primary_ip6_id is None:
                        self.log_failure(device, "Device is missing primary IPv4 and IPv6 address")
                    else:
                        self.log_warning(device, "Device is missing primary IPv4 addresses")
            else:
                if device.device_type.is_child_device is True:
                    self.log_success(device)
                else:
                    if device.primary_ip6_id is None:
                        self.log_info(device, "Device is missing primary IPv6 address")
                    else:
                        self.log_success(device)
