import asyncio
import websockets

server_url = ''
username = ''

async def client_message():
    # Подключаемся к серверу асинхронный код
    async with websockets.connect(server_url) as websocket:
        # когда первый раз подключаемся
        # отправляем сообщение init чтобы сказать сказать серверу
        # что первый раз подключаемся
        await websocket.send('init:' + username)
        # Создаем бесконечный цикл для непрерывной
        # для отправки сообщении
        while True:
            message = input('Введите сообщение: ')

            # отключаем клиент когда мы пишем exit
            if message == 'exit' or websocket.closed == True:
                # завершаем соединение с сервером
                # await websocket.close()
                print('программа завершена')
                break

            await websocket.send(username+'>>>'+message)
            print('Сообщение отправлено')


# Запуска клиента консоль чата
asyncio.get_event_loop().run_until_complete(client_message())
