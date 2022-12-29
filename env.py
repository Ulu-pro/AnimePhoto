# Bot
TOKEN = ''

# Images
DIRECTORY = 'images'
FILE = '%d.jpg'
COUNT = 3

# Messages
START = 'Send me a photo'
WAIT = 'Please, wait...'
READY = 'All is ready!'

# API
URL = 'https://ai.tu.qq.com/trpc.shadow_cv.ai_processor_cgi.AIProcessorCgi/Process'
GENERATED = 'https://act-artifacts'
HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,uk-UA;q=0.8,uk;q=0.6,en-US;q=0.4,en;q=0.2',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '448320',
    'Content-Type': 'application/json',
    'Cookie': 'iip=0; '
              'pac_uid=0_ce27c744a8be3; '
              'pgv_info=ssid=s2755604992; '
              'pgv_pvid=9635260140; '
              'ariaDefaultTheme=undefined',
    'Host': 'ai.tu.qq.com',
    'Origin': 'https://h5.tu.qq.com/',
    'Referer': 'https://h5.tu.qq.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
}
COOKIES = {
    'iip': '0',
    'pac_uid': '0_ce27c744a8be3',
    'pgv_info': 'ssid=s2755604992',
    'pgv_pvid': '9635260140',
    'ariaDefaultTheme': 'undefined',
}
JSON = {
    'busiId': 'ai_painting_anime_entry',
    'extra': '{"face_rects":[],'
             '"version":2,'
             '"platform":"web",'
             '"data_report":{'
             '"parent_trace_id":"323b8a31-2487-494c-6d0e-3baabf3c608a",'
             '"root_channel":"",'
             '"level":0}}',
    'images': [],
}
