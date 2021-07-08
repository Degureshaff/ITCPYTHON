import websockets
import asyncio

# list Пользователи 
users = []


async def on_message(websocket, path):
    while True:
        message = await websocket.recv()        
        if message.find('init:') == 0:
            msq_spl = message.split(':')
            print(msq_spl[1], 'присоединился')
            users.add({
                'user_name':msq_spl[1],
                'client_socket':websocket
            })
            for user in users:
                if user['client_socket'].closed == False:
                    await user['client_socket'].send(
                        msq_spl[1]+'>>присоединился'
                    )
        else:          
            print('->', message)
            for user in users:
                if user['client_socket'].closed == False:
                    await user['client_socket'].send(message)
            

# Создаем сервер веб чата на порту 3030
server = websockets.serve(on_message, port=3030)
print('Наш консольный чат сервер запущен...')

# Запуск веб чат сервера
asyncio.get_event_loop().run_until_complete(server)
# Запуск сервера на постоянную основу
asyncio.get_event_loop().run_forever()