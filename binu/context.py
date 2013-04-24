from binu import device
import settings

def app_info(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    device_info = device.get_device_info(request)
    screen_info = device.get_screen_info(request)

    return {
        'SCREEN': screen_info,
        'DEVICE': device_info,
        'app_id': settings.BINU_APP_ID,
        'dev_id': settings.BINU_DEV_ID
    }
    
