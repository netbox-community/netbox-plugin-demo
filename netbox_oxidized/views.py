from django.shortcuts import get_object_or_404, render
from dcim.models import Device
from .models import DeviceBackup

def device_backup_view(request, pk):
    device = get_object_or_404(Device, pk=pk)
    backups = DeviceBackup.objects.filter(device=device)
    return render(request, 'netbox_oxidized/device_backup.html', {
        'device': device,
        'backups': backups,
    })
