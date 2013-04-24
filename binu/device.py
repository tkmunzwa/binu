import logging

logger = logging.getLogger(__name__)

SIZE_SMALL = "s"
SIZE_MEDIUM = "m"
SIZE_LARGE = "l"
SIZE_XLARGE = "xl"
SIZE_XXLARGE = "xxl"

APP_SIZES = { SIZE_SMALL: {
                   "font_size": 12,
                   "line_height": 14,
                   "title_indent": 15,
                   "indent": 2,
                   "size": SIZE_SMALL,
                   },
            SIZE_MEDIUM: {
                   "font_size": 15,
                   "line_height": 17,
                   "title_indent": 18,
                   "indent": 3,
                   "size": SIZE_MEDIUM,
                   },
            SIZE_LARGE: {
                   "font_size": 18,
                   "line_height": 20,
                   "title_indent": 21,
                   "indent": 3,
                   "size": SIZE_LARGE,
                   },
             SIZE_XLARGE: {
                   "font_size": 23,
                   "line_height": 27,
                   "title_indent": 21,
                   "indent": 3,
                   "size": SIZE_XLARGE,
                   },
             SIZE_XXLARGE: {
                   "font_size": 30,
                   "line_height": 40,
                   "title_indent": 21,
                   "indent": 3,
                   "size": SIZE_XXLARGE,
                   },
            }

def get_device_info(request):
    info = {'id': '0000',
            'ip': '0.0.0.0'
            }
    try:
        info['device_id'] = request.cookies['binusys_device_id']
        info['device_ip'] = request.cookies['binusys_device_ip']
    except: pass
    logger.debug('device info is {}'.format(info))
    return info

def get_screen_info(request):

#    width = 120
#    height = 120
    width = 480
    height = 320
#    width = 240
#    height = 240

    try:
        dimensions = request.COOKIES.get('binusys_size', None)
        width, height = dimensions.split('x')
    except Exception as e: 
        logger.error(e)
    res = int(width) * int(height)
    
    if res <= 26000:
        app_info = APP_SIZES[SIZE_SMALL]
    elif res <= 40000:
        app_info = APP_SIZES[SIZE_MEDIUM]
    elif res <= 100000:
        app_info = APP_SIZES[SIZE_LARGE]
    elif res <= 185000:
        app_info = APP_SIZES[SIZE_XLARGE]
    else:
        app_info = APP_SIZES[SIZE_XXLARGE]
    app_info.update({'width': width, 'height': height})
    logger.info('cookies have is {}'.format(request.COOKIES))
    logger.debug('screen info is {}'.format(app_info))

    return app_info
