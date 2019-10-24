from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = "dca61651750535f3f5f4534c6fb7023ebc50387c2fccb1e0b76619d1542aaf014c144eb0f33319c95e6d5"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "Привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет', 'random_id': 0})
                elif response == "помощь":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '||| Здравствуйте! Бот работает так! ||| Предмет класс номер |||', 'random_id': 0})
                elif response == "алгебра 9 1":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3m2', 'random_id': 0})
                elif response == "алгебра 9 2":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3oM', 'random_id': 0})
                elif response == "алгебра 9 3":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3oq', 'random_id': 0})
                elif response == "алгебра 9 4":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3qC', 'random_id': 0})
                elif response == "алгебра 9 5":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3qV', 'random_id': 0})    
                elif response == "алгебра 9 6":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3rR!', 'random_id': 0})
                elif response == "алгебра 9 7":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3x2', 'random_id': 0})
                elif response == "алгебра 9 8":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3xd', 'random_id': 0})
                elif response == "алгебра 9 9":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3yE', 'random_id': 0})
                elif response == "алгебра 9 10":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS3zQ', 'random_id': 0}) 
                elif response == "алгебра 9 11":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4Di', 'random_id': 0})
                elif response == "алгебра 9 12":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4EZ', 'random_id': 0})
                elif response == "алгебра 9 13":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4FM', 'random_id': 0})
                elif response == "алгебра 9 14":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4Fy', 'random_id': 0})
                elif response == "алгебра 9 15":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4Gg', 'random_id': 0}) 
                elif response == "алгебра 9 16":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4HU', 'random_id': 0})
                elif response == "алгебра 9 17":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4Ht', 'random_id': 0})
                elif response == "алгебра 9 18":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4JC', 'random_id': 0})
                elif response == "алгебра 9 19":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4JU', 'random_id': 0})
                elif response == "алгебра 9 20":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4K5', 'random_id': 0})         
                elif response == "алгебра 9 21":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4aP', 'random_id': 0})
                elif response == "алгебра 9 22":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4af', 'random_id': 0})
                elif response == "алгебра 9 23":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4bJ', 'random_id': 0})
                elif response == "алгебра 9 24":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4bs', 'random_id': 0})
                elif response == "алгебра 9 25":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4cC', 'random_id': 0})
                elif response == "алгебра 9 26":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4d5', 'random_id': 0})
                elif response == "алгебра 9 27":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4dJ', 'random_id': 0})
                elif response == "алгебра 9 28":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4dd', 'random_id': 0})
                elif response == "алгебра 9 29":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4e2', 'random_id': 0})
                elif response == "алгебра 9 30":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS4eG', 'random_id': 0})
                elif response == "алгебра 9 31":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 32":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 33":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 34":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 35":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 36":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 37":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 38":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 39":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 40":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 41":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 42":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 43":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 44":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 45":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 46":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 47":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 48":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 49":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 50":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})         
                elif response == "алгебра 9 51":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 52":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 53":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 54":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 55":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 56":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 57":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 58":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 59":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 60":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 61":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 62":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 63":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 64":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 65":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 66":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 67":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 68":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 69":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 70":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 71":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 72":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 73":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 74":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 75":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 76":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 77":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 78":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 79":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 80":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})         
                elif response == "алгебра 9 81":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 82":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 83":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 84":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 85":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 86":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 87":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 88":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 89":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 90":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 91":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 92":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 93":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 94":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 95":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 96":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 97":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 98":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 99":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 100":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 101":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 102":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 103":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 104":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 105":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 106":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 107":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 108":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 109":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 110":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})         
                elif response == "алгебра 9 111":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 112":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 113":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 114":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 115":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 116":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 117":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 118":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 119":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 120":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})   
                elif response == "алгебра 9 121":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 122":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 123":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 124":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 125":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 126":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 127":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 128":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 129":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 130":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 131":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 132":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 133":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 134":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 135":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 136":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 137":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 138":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 139":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 140":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Fb', 'random_id': 0})         
                elif response == "алгебра 9 141":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Ft', 'random_id': 0})
                elif response == "алгебра 9 142":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6GZ', 'random_id': 0})
                elif response == "алгебра 9 143":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6HV', 'random_id': 0})
                elif response == "алгебра 9 144":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Hm', 'random_id': 0})
                elif response == "алгебра 9 145":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Hy', 'random_id': 0})
                elif response == "алгебра 9 146":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6JJ', 'random_id': 0})
                elif response == "алгебра 9 147":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Je', 'random_id': 0})
                elif response == "алгебра 9 148":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6K7', 'random_id': 0})
                elif response == "алгебра 9 149":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6KL', 'random_id': 0})
                elif response == "алгебра 9 150":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6NX', 'random_id': 0})
                elif response == "алгебра 9 151":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Nn', 'random_id': 0})
                elif response == "алгебра 9 152":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Nz', 'random_id': 0})
                elif response == "алгебра 9 153":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6PJ', 'random_id': 0})
                elif response == "алгебра 9 154":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6PV', 'random_id': 0})
                elif response == "алгебра 9 155":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Py', 'random_id': 0})    
                elif response == "алгебра 9 156":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6QH', 'random_id': 0})
                elif response == "алгебра 9 157":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Qa', 'random_id': 0})
                elif response == "алгебра 9 158":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Qi', 'random_id': 0})
                elif response == "алгебра 9 159":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Qw', 'random_id': 0})
                elif response == "алгебра 9 160":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6tL', 'random_id': 0}) 
                elif response == "алгебра 9 161":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6RD', 'random_id': 0})
                elif response == "алгебра 9 162":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6RQ', 'random_id': 0})
                elif response == "алгебра 9 163":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Rk', 'random_id': 0})
                elif response == "алгебра 9 164":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6S4', 'random_id': 0})
                elif response == "алгебра 9 165":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Sa', 'random_id': 0}) 
                elif response == "алгебра 9 166":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6So', 'random_id': 0})
                elif response == "алгебра 9 167":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6TD', 'random_id': 0})
                elif response == "алгебра 9 168":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6TL', 'random_id': 0})
                elif response == "алгебра 9 169":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6Tb', 'random_id': 0})
                elif response == "алгебра 9 170":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6U3', 'random_id': 0})         
                elif response == "алгебра 9 171":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6UG', 'random_id': 0})
                elif response == "алгебра 9 172":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS6vB', 'random_id': 0})
                elif response == "алгебра 9 173":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS728', 'random_id': 0})
                elif response == "алгебра 9 174":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS72r', 'random_id': 0})
                elif response == "алгебра 9 175":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS735', 'random_id': 0})
                elif response == "алгебра 9 176":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS73L', 'random_id': 0})
                elif response == "алгебра 9 177":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS74G', 'random_id': 0})
                elif response == "алгебра 9 178":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS74g', 'random_id': 0})
                elif response == "алгебра 9 179":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS75T', 'random_id': 0})
                elif response == "алгебра 9 180":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS75j', 'random_id': 0}) 
                elif response == "алгебра 9 181":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS77m', 'random_id': 0})
                elif response == "алгебра 9 182":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS78C', 'random_id': 0})
                elif response == "алгебра 9 183":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS78W', 'random_id': 0})
                elif response == "алгебра 9 184":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS78c', 'random_id': 0})
                elif response == "алгебра 9 185":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS78s', 'random_id': 0})    
                elif response == "алгебра 9 186":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS79D', 'random_id': 0})
                elif response == "алгебра 9 187":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS79e', 'random_id': 0})
                elif response == "алгебра 9 188":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7AJ', 'random_id': 0})
                elif response == "алгебра 9 189":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7AZ', 'random_id': 0})
                elif response == "алгебра 9 190":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7Aw', 'random_id': 0}) 
                elif response == "алгебра 9 191":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7BH', 'random_id': 0})
                elif response == "алгебра 9 192":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7Bj', 'random_id': 0})
                elif response == "алгебра 9 193":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7Bz', 'random_id': 0})
                elif response == "алгебра 9 194":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7CK', 'random_id': 0})
                elif response == "алгебра 9 195":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7CY', 'random_id': 0}) 
                elif response == "алгебра 9 196":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7Cq', 'random_id': 0})
                elif response == "алгебра 9 197":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7DP', 'random_id': 0})
                elif response == "алгебра 9 198":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7Df', 'random_id': 0})
                elif response == "алгебра 9 199":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7Ds', 'random_id': 0})
                elif response == "алгебра 9 200":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JS7E7', 'random_id': 0})         
                elif response == "алгебра 9 201":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk75', 'random_id': 0})
                elif response == "алгебра 9 202":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk7L', 'random_id': 0})
                elif response == "алгебра 9 203":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk7c', 'random_id': 0})
                elif response == "алгебра 9 204":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk7x', 'random_id': 0})
                elif response == "алгебра 9 205":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk8F', 'random_id': 0})
                elif response == "алгебра 9 206":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk8b', 'random_id': 0})
                elif response == "алгебра 9 207":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk96', 'random_id': 0})
                elif response == "алгебра 9 208":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk9Q', 'random_id': 0})
                elif response == "алгебра 9 209":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk9n', 'random_id': 0})
                elif response == "алгебра 9 210":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSk9z', 'random_id': 0}) 
                elif response == "алгебра 9 211":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkCw', 'random_id': 0})
                elif response == "алгебра 9 212":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkDZ', 'random_id': 0})
                elif response == "алгебра 9 213":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkHi', 'random_id': 0})
                elif response == "алгебра 9 214":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkJF', 'random_id': 0})
                elif response == "алгебра 9 215":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkJP', 'random_id': 0})    
                elif response == "алгебра 9 216":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkKd', 'random_id': 0})
                elif response == "алгебра 9 217":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkLF', 'random_id': 0})
                elif response == "алгебра 9 218":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkLh', 'random_id': 0})
                elif response == "алгебра 9 219":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkMG', 'random_id': 0})
                elif response == "алгебра 9 220":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkN7', 'random_id': 0}) 
                elif response == "алгебра 9 221":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkag', 'random_id': 0})
                elif response == "алгебра 9 222":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkaw', 'random_id': 0})
                elif response == "алгебра 9 223":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkbF', 'random_id': 0})
                elif response == "алгебра 9 224":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkbc', 'random_id': 0})
                elif response == "алгебра 9 225":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkcp', 'random_id': 0}) 
                elif response == "алгебра 9 226":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkdQ', 'random_id': 0})
                elif response == "алгебра 9 227":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkde', 'random_id': 0})
                elif response == "алгебра 9 228":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkdv', 'random_id': 0})
                elif response == "алгебра 9 229":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkeG', 'random_id': 0})
                elif response == "алгебра 9 230":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkec', 'random_id': 0})         
                elif response == "алгебра 9 231":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkf9', 'random_id': 0})
                elif response == "алгебра 9 232":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkfY', 'random_id': 0})
                elif response == "алгебра 9 233":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkfx', 'random_id': 0})
                elif response == "алгебра 9 234":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkgF', 'random_id': 0})
                elif response == "алгебра 9 235":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkgf', 'random_id': 0})
                elif response == "алгебра 9 236":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkhC', 'random_id': 0})
                elif response == "алгебра 9 237":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkhV', 'random_id': 0})
                elif response == "алгебра 9 238":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkiS', 'random_id': 0})
                elif response == "алгебра 9 239 ":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkiY', 'random_id': 0})
                elif response == "алгебра 9 240 ":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkio', 'random_id': 0})
                elif response == "алгебра 9 241":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkjN', 'random_id': 0})
                elif response == "алгебра 9 242":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkjh', 'random_id': 0})
                elif response == "алгебра 9 243":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkjq', 'random_id': 0})
                elif response == "алгебра 9 244":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkkD', 'random_id': 0})
                elif response == "алгебра 9 245":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkkp', 'random_id': 0})    
                elif response == "алгебра 9 246":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkmL', 'random_id': 0})
                elif response == "алгебра 9 247":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkmb', 'random_id': 0})
                elif response == "алгебра 9 248":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkmo', 'random_id': 0})
                elif response == "алгебра 9 249":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSkn5', 'random_id': 0})
                elif response == "алгебра 9 250":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSknP', 'random_id': 0}) 
                elif response == "алгебра 9 251":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm5x', 'random_id': 0})
                elif response == "алгебра 9 252":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm6F', 'random_id': 0})
                elif response == "алгебра 9 253":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm6W', 'random_id': 0})
                elif response == "алгебра 9 254":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm6p', 'random_id': 0})
                elif response == "алгебра 9 255":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm7B', 'random_id': 0}) 
                elif response == "алгебра 9 256":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm7c', 'random_id': 0})
                elif response == "алгебра 9 257":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm7t', 'random_id': 0})
                elif response == "алгебра 9 258":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm8W', 'random_id': 0})
                elif response == "алгебра 9 259":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm9A', 'random_id': 0})
                elif response == "алгебра 9 260":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm9Z', 'random_id': 0})         
                elif response == "алгебра 9 261":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSm9p', 'random_id': 0})
                elif response == "алгебра 9 262":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmA3', 'random_id': 0})
                elif response == "алгебра 9 263":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmAS', 'random_id': 0})
                elif response == "алгебра 9 264":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmAY', 'random_id': 0})
                elif response == "алгебра 9 265":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmBT', 'random_id': 0})
                elif response == "алгебра 9 266":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmBv', 'random_id': 0})
                elif response == "алгебра 9 267":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmCJ', 'random_id': 0})
                elif response == "алгебра 9 268":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmCi', 'random_id': 0})
                elif response == "алгебра 9 269":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmCv', 'random_id': 0})
                elif response == "алгебра 9 270":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmD7', 'random_id': 0})
                elif response == "алгебра 9 271":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmDV', 'random_id': 0})
                elif response == "алгебра 9 272":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmDn', 'random_id': 0})
                elif response == "алгебра 9 273":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmE9', 'random_id': 0})
                elif response == "алгебра 9 274":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmEN', 'random_id': 0})    
                elif response == "алгебра 9 275":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmEc', 'random_id': 0})
                elif response == "алгебра 9 276":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmFA', 'random_id': 0})
                elif response == "алгебра 9 277":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmG9', 'random_id': 0})
                elif response == "алгебра 9 278":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmHw', 'random_id': 0})
                elif response == "алгебра 9 279":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmJJ', 'random_id': 0}) 
                elif response == "алгебра 9 280":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmUQ', 'random_id': 0})
                elif response == "алгебра 9 281":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmUj', 'random_id': 0})
                elif response == "алгебра 9 282":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmV3', 'random_id': 0})
                elif response == "алгебра 9 283":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmVQ', 'random_id': 0})
                elif response == "алгебра 9 284":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmW8', 'random_id': 0}) 
                elif response == "алгебра 9 285":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmWS', 'random_id': 0})
                elif response == "алгебра 9 286":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmWm', 'random_id': 0})
                elif response == "алгебра 9 287":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmX7', 'random_id': 0})
                elif response == "алгебра 9 288":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmXP', 'random_id': 0})
                elif response == "алгебра 9 289":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmXi', 'random_id': 0})         
                elif response == "алгебра 9 290":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmXu', 'random_id': 0})
                elif response == "алгебра 9 291":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmYP', 'random_id': 0})
                elif response == "алгебра 9 292":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmYq!', 'random_id': 0})
                elif response == "алгебра 9 293":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmZ8', 'random_id': 0})
                elif response == "алгебра 9 294":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmZP', 'random_id': 0})
                elif response == "алгебра 9 295":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmZu', 'random_id': 0})
                elif response == "алгебра 9 296":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmaL', 'random_id': 0})
                elif response == "алгебра 9 297":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmah', 'random_id': 0})
                elif response == "алгебра 9 298":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmbL', 'random_id': 0}) 
                elif response == "алгебра 9 299":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmbZ', 'random_id': 0})
                elif response == "алгебра 9 300":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JSmby', 'random_id': 0})
                elif response == "алгебра 9 301":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 302":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 303":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 304":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 305":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 306":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 307":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 308":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 309":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 310":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 311":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 312":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 313":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 314":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 315":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 316":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 317":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 318":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})         
                elif response == "алгебра 9 319":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 320":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 321":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 322":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 323":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 324":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 325":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 326":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 327":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 328":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 329":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 330":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 331":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 332":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 333":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 334":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 335":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 336":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 337":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 338":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 339":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 340":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 341":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 342":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 343":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 344":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 345":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 346":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 347":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 358":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})         
                elif response == "алгебра 9 359":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 360":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 361":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 362":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 363":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 364":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 365":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 366":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 367":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 368":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 369":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 370":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 371":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 372":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 373":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})    
                elif response == "алгебра 9 374":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 375":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 376":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 377":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 378":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 379":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 380":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 381":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 382":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 383":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0}) 
                elif response == "алгебра 9 384":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 385":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 386":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 387":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 388":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})         
                elif response == "алгебра 9 389":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 390":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 391":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 392":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 393":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 394":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 395":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 396":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 397":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 398":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 399":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "алгебра 9 400":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Тебе пишу!', 'random_id': 0})
                elif response == "геометрия 700":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JTzyB', 'random_id': 0})
                elif response == "геометрия 701":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JTzzS', 'random_id': 0})        
                elif response == "геометрия 702":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU22F', 'random_id': 0})  
                elif response == "геометрия 703":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU22U', 'random_id': 0})  
                elif response == "геометрия 704":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU22h', 'random_id': 0})  
                elif response == "геометрия 705":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU23F', 'random_id': 0}) 
                elif response == "геометрия 706":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU23X', 'random_id': 0})        
                elif response == "геометрия 707":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU23v', 'random_id': 0})  
                elif response == "геометрия 708":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU24E', 'random_id': 0})  
                elif response == "геометрия 709":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU25K', 'random_id': 0})  
                elif response == "геометрия 710":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU25W', 'random_id': 0})
                elif response == "геометрия 711":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU25n', 'random_id': 0})        
                elif response == "геометрия 712":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU26n', 'random_id': 0})  
                elif response == "геометрия 713":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU27C', 'random_id': 0})  
                elif response == "геометрия 714":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU27R', 'random_id': 0})  
                elif response == "геометрия 715":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU27j', 'random_id': 0})
                elif response == "геометрия 716":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU282', 'random_id': 0})        
                elif response == "геометрия 717":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU28L', 'random_id': 0})  
                elif response == "геометрия 718":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU28a', 'random_id': 0})  
                elif response == "геометрия 719":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU28j', 'random_id': 0})  
                elif response == "геометрия 720":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU293', 'random_id': 0})
                elif response == "геометрия 721":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU29T', 'random_id': 0})        
                elif response == "геометрия 722":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU29r', 'random_id': 0})  
                elif response == "геометрия 723":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2AA', 'random_id': 0})  
                elif response == "геометрия 724":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2AW', 'random_id': 0})  
                elif response == "геометрия 725":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Ai', 'random_id': 0})
                elif response == "геометрия 726":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2B6', 'random_id': 0})        
                elif response == "геометрия 727":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2BK', 'random_id': 0})  
                elif response == "геометрия 728":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Ba', 'random_id': 0})  
                elif response == "геометрия 729":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Bo', 'random_id': 0})  
                elif response == "геометрия 730":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Bw', 'random_id': 0})
                elif response == "геометрия 731":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2CH', 'random_id': 0})        
                elif response == "геометрия 732":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2CT', 'random_id': 0})  
                elif response == "геометрия 733":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Cg', 'random_id': 0})  
                elif response == "геометрия 734":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Ck', 'random_id': 0})  
                elif response == "геометрия 735":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Cu', 'random_id': 0})                                 
                elif response == "геометрия 736":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2D9', 'random_id': 0})        
                elif response == "геометрия 737":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2DM', 'random_id': 0})  
                elif response == "геометрия 738":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Da', 'random_id': 0})  
                elif response == "геометрия 739":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Dg', 'random_id': 0})  
                elif response == "геометрия 740":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Ds', 'random_id': 0}) 
                elif response == "геометрия 741":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2EJ', 'random_id': 0})        
                elif response == "геометрия 742":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2ES', 'random_id': 0})  
                elif response == "геометрия 743":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Eq', 'random_id': 0})  
                elif response == "геометрия 744":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2F2', 'random_id': 0})  
                elif response == "геометрия 745":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2FG', 'random_id': 0})
                elif response == "геометрия 746":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2FZ', 'random_id': 0})        
                elif response == "геометрия 747":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Fh', 'random_id': 0})  
                elif response == "геометрия 748":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Fr', 'random_id': 0})  
                elif response == "геометрия 749":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2GA', 'random_id': 0})  
                elif response == "геометрия 750":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2GH', 'random_id': 0})
                elif response == "геометрия 751":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Hh', 'random_id': 0})        
                elif response == "геометрия 752":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Hv', 'random_id': 0})  
                elif response == "геометрия 753":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2JE', 'random_id': 0})  
                elif response == "геометрия 754":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2JY', 'random_id': 0})  
                elif response == "геометрия 755":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Jq', 'random_id': 0})
                elif response == "геометрия 756":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2K6', 'random_id': 0})        
                elif response == "геометрия 757":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2KH', 'random_id': 0})  
                elif response == "геометрия 758":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Ka', 'random_id': 0})  
                elif response == "геометрия 759":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Kg', 'random_id': 0})  
                elif response == "геометрия 760":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2M5', 'random_id': 0})
                elif response == "геометрия 761":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2MD', 'random_id': 0})        
                elif response == "геометрия 762":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2MT', 'random_id': 0})  
                elif response == "геометрия 763":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Mf', 'random_id': 0})  
                elif response == "геометрия 764":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Mt', 'random_id': 0})  
                elif response == "геометрия 765":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2N2', 'random_id': 0})
                elif response == "геометрия 766":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 767":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 768":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 769":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 770":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})     
                elif response == "геометрия 771":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 772":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 773":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 774":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 775":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0}) 
                elif response == "геометрия 776":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 777":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 778":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 779":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 780":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 781":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 782":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 783":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 784":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 785":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 786":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 787":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 788":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 789":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 790":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 791":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 792":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 793":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 794":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия795":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 796":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 797":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 798":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 799":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 900":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqNW', 'random_id': 0})
                elif response == "геометрия 901":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqPj', 'random_id': 0})
                elif response == "геометрия 902":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqQB', 'random_id': 0})        
                elif response == "геометрия 902":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqQc', 'random_id': 0})  
                elif response == "геометрия 903":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU22U', 'random_id': 0})  
                elif response == "геометрия 904":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqR6', 'random_id': 0})  
                elif response == "геометрия 905":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqii', 'random_id': 0}) 
                elif response == "геометрия 906":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqiz', 'random_id': 0})        
                elif response == "геометрия 907":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqjL', 'random_id': 0})  
                elif response == "геометрия 908":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqjt', 'random_id': 0})  
                elif response == "геометрия 909":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqkF', 'random_id': 0})  
                elif response == "геометрия 910":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqkc', 'random_id': 0})
                elif response == "геометрия 911":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqmX', 'random_id': 0})        
                elif response == "геометрия 912":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqnm', 'random_id': 0})  
                elif response == "геометрия 913":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqqN', 'random_id': 0})  
                elif response == "геометрия 914":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUqqb', 'random_id': 0})  
                elif response == "геометрия 915":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrPn', 'random_id': 0})
                elif response == "геометрия 916":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrK9', 'random_id': 0})        
                elif response == "геометрия 917":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrQA', 'random_id': 0})  
                elif response == "геометрия 918":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrSN', 'random_id': 0})  
                elif response == "геометрия 919":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrUS', 'random_id': 0})  
                elif response == "геометрия 920":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrVi', 'random_id': 0})
                elif response == "геометрия 921":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrYY', 'random_id': 0})        
                elif response == "геометрия 922":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUrcn', 'random_id': 0})  
                elif response == "геометрия 923":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUreu', 'random_id': 0})  
                elif response == "геометрия 924":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUs5Y', 'random_id': 0})  
                elif response == "геометрия 925":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUs6b', 'random_id': 0})
                elif response == "геометрия 926":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsAP', 'random_id': 0})        
                elif response == "геометрия 927":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsB4', 'random_id': 0})  
                elif response == "геометрия 928":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsBF', 'random_id': 0})  
                elif response == "геометрия 929":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsBZ', 'random_id': 0})  
                elif response == "геометрия 930":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsBv', 'random_id': 0})
                elif response == "геометрия 931":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsC6', 'random_id': 0})        
                elif response == "геометрия 932":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsED', 'random_id': 0})  
                elif response == "геометрия 933":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsGJ', 'random_id': 0})  
                elif response == "геометрия 934":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsJB', 'random_id': 0})  
                elif response == "геометрия 935":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsJR', 'random_id': 0})                                 
                elif response == "геометрия 936":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsJf', 'random_id': 0})        
                elif response == "геометрия 937":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsJt', 'random_id': 0})  
                elif response == "геометрия 938":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsK2', 'random_id': 0})  
                elif response == "геометрия 939":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsKD', 'random_id': 0})  
                elif response == "геометрия 940":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JUsKR', 'random_id': 0}) 
                elif response == "геометрия 941":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 942":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 943":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 944":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 945":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 946":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2FZ', 'random_id': 0})        
                elif response == "геометрия 947":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Fh', 'random_id': 0})  
                elif response == "геометрия 948":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Fr', 'random_id': 0})  
                elif response == "геометрия 949":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2GA', 'random_id': 0})  
                elif response == "геометрия 950":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2GH', 'random_id': 0})
                elif response == "геометрия 951":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Hh', 'random_id': 0})        
                elif response == "геометрия 952":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Hv', 'random_id': 0})  
                elif response == "геометрия 953":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2JE', 'random_id': 0})  
                elif response == "геометрия 954":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2JY', 'random_id': 0})  
                elif response == "геометрия 955":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Jq', 'random_id': 0})
                elif response == "геометрия 956":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2K6', 'random_id': 0})        
                elif response == "геометрия 957":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2KH', 'random_id': 0})  
                elif response == "геометрия 958":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Ka', 'random_id': 0})  
                elif response == "геометрия 959":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Kg', 'random_id': 0})  
                elif response == "геометрия 960":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2M5', 'random_id': 0})
                elif response == "геометрия 961":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2MD', 'random_id': 0})        
                elif response == "геометрия 962":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2MT', 'random_id': 0})  
                elif response == "геометрия 963":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Mf', 'random_id': 0})  
                elif response == "геометрия 964":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2Mt', 'random_id': 0})  
                elif response == "геометрия 965":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'https://clck.ru/JU2N2', 'random_id': 0})
                elif response == "геометрия 966":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 967":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 968":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 969":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 970":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})     
                elif response == "геометрия 971":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 972":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 973":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 974":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 975":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0}) 
                elif response == "геометрия 976":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 977":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 978":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 979":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 980":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 981":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 982":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 983":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 984":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 985":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 986":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 987":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 988":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 989":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 990":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 991":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 992":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 993":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 994":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 995":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                elif response == "геометрия 996":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})        
                elif response == "геометрия 997":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 998":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 999":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})  
                elif response == "геометрия 900":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': '', 'random_id': 0})
                else:   
                    vk_session.method('messages.send', {'peer_id': event.user_id, 'message': 'Не понимаю тебя! Пропиши: помощь!', 'random_id': 0})                                                              