from pyrogram import Client, filters
import time, datetime
import sqlite3, asyncio
from contextlib import redirect_stdout

app = Client("my_account")

@app.on_message(filters.command("челы", prefixes="."))
async def get_chat_members(client, message):
    try:
        members = ""
        async for member in app.get_chat_members(message.chat.id):
            if members is None:
                continue
            members += str(f"@{member.user.username}\n")
        await app.send_message(message.chat.id, members)
    except Exception as e:
        await app.send_message(message.chat.id, e)

@app.on_message(filters.command("лс", prefixes="."))
async def send_msg(client, message):
    if message.from_user.id == 1982062215:
        try:
            user = await app.get_users(user_ids=message.reply_to_message.from_user.id)
        except:
            pass

        reply = message.reply_to_message.from_user.id
        if user.username is None:
            user_ = "Хуй его знает"
        else:
            user_ = user.username
        await app.edit_message_text(message.chat.id, message.id, f"Отправка сообщения..\n" \
                                                                f"Получатель: @{user_}\n" \
                                                                f"Текст сообщение: {message.text.split()[1]}")
        await app.send_message(reply, message.text.split()[1])

@app.on_message(filters.command("py", prefixes="."))
async def test(client, message):
    try:
        if message.from_user.id == 391363367:
            pass
        else:
            code = message.text[4:]

            exec_vars = {**globals(), **locals()}

            exec(
                'async def func(message):\n\t' + '\n\t'.join(code.splitlines()),
                exec_vars,
                exec_vars
            )

            await exec_vars['func'](message)

            await app.edit_message_text(message.chat.id, message.id, "Выполнение кода\n\n"\
                                                                        f"```{code}```\n\n"\
                                                                        f"Result:\n"\
                                                                        f"``````")
    except Exception as e:
        await app.send_message(message.chat.id, "Error!\n\n"\
                                                    f"```{e}```")



@app.on_message()
async def glavnaya(client, message):
    db = sqlite3.connect("server.db")
    sql = db.cursor()
    sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER)")
    db.commit()

    try:
        user = await app.get_users(user_ids=message.reply_to_message.from_user.id)
    except:
        pass

    elif message.text == ".2ч":
        await app.edit_message_text(message.chat.id, message.id, ":-(")

    elif message.text == "all users":
        all_users = ""
        await app.edit_message_text(message.chat.id, message.id, "Собираю всех пользователей...")
        await asyncio.sleep(1.5)
        for i in sql.execute("SELECT id FROM users"):
            all_users += f"{i[0]}\n"
        await app.edit_message_text(message.chat.id, message.id, f"Айди пользователей:\n{all_users}")


    elif message.text == "ыы":
        await app.edit_message_text(message.chat.id, message.id, "🌑✨✨🌏✨✨✨")
        await asyncio.sleep(1)
        await app.edit_message_text(message.chat.id, message.id, "✨🌑✨🌏✨✨✨")
        await asyncio.sleep(1)
        await app.edit_message_text(message.chat.id, message.id, "✨✨🌑🌏✨✨✨")
        await asyncio.sleep(1)
        await app.edit_message_text(message.chat.id, message.id, "✨✨✨🌏🌕✨✨")
        await asyncio.sleep(1)
        await app.edit_message_text(message.chat.id, message.id, "✨✨✨🌏✨🌕✨")
        await asyncio.sleep(1)
        await app.edit_message_text(message.chat.id, message.id, "✨✨✨🌏✨✨🌕")

    elif message.text == "ы":
        await app.edit_message_text(message.chat.id, message.id, "🌑🌒🌓🌔🌕🌖🌗🌘")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌘🌗🌖🌕🌔🌓🌒🌑")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌗🌖🌕🌔🌓🌒🌑🌘")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌖🌕🌔🌓🌒🌑🌘🌗")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌕🌔🌓🌒🌑🌘🌗🌖")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌔🌓🌒🌑🌘🌗🌖🌕")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌓🌒🌑🌘🌗🌖🌕🌘")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌒🌑🌘🌗🌖🌕🌘🌓")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌑🌒🌓🌔🌕🌖🌗🌘")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌘🌗🌖🌕🌔🌓🌒🌑")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌗🌖🌕🌔🌓🌒🌑🌘")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌖🌕🌔🌓🌒🌑🌘🌗")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌕🌔🌓🌒🌑🌘🌗🌖")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌔🌓🌒🌑🌘🌗🌖🌕")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "🌓🌒🌑🌘🌗🌖🌕🌘")
        await app.edit_message_text(message.chat.id, message.id, "🌒🌑🌘🌗🌖🌕🌘🌓")

    elif message.text == "ыыы":
        await app.edit_message_text(message.chat.id, message.id, "☣       🦍💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣        🦍💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣         🦍💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣          🦍💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣           🦍💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣            🦍💨💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣             🦍💨💨💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣              🦍💨💨💨💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣             🦍💨💨💨💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣            🦍💨💨💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣           🦍💨💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣          🦍💨💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣         🦍💨💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣👀======🦍💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣👀=====🦍💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣👀====🦍💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣👀===🦍💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣👀==🦍💨💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣👀==💢🦍💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "☣💦💢🦍💨💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "💥💦💦💢🦍💨")
        await asyncio.sleep(0.5)
        await app.edit_message_text(message.chat.id, message.id, "💥💥💥💥💥")


    elif message.text == "пинг":
        await app.send_message(message.chat.id, "ПОНГ")

    elif message.text == "инфо":
        if user.is_bot == True:
            bot = "да"
        else:
            bot = "нет"

        if user.is_verified == True:
            verif = "да"
        else:
            verif = "нет"

        if user.is_premium == True:
            premium = "да"
        else:
            premium = "нет"

        if user.is_contact == True:
            in_contact = "да"
        else:
            in_contact = "нет"

        if user.is_deleted == True:
            deleted = "да"
        else:
            deleted = "нет"

        if user.is_self == True:
            is_self = "да"
        else:
            is_self = "нет"

        if user.is_mutual_contact == True:
            is_mutual = "да"
        else:
            is_mutual = "нет"

        if user.is_restricted == True:
            restricted = "да"
        else:
            restricted = "нет"

        if user.is_scam == True:
            scam = "да"
        else:
            scam = "нет"

        if user.is_fake == True:
            fake = "да"
        else:
            fake = "нет"
        await app.edit_message_text(message.chat.id, message.id, "получаю информацию")
        time.sleep(1)
        await app.edit_message_text(message.chat.id, message.id, f"Айди пользователя: {user.id}\n"\
                                    f"Имя: {user.first_name}\n"\
                                    f"Бот: {bot}\n"
                                    f"Верифицирован: {verif}\n"
                                    f"Обладатель премиума: {premium}\n"
                                    f"Username: {user.username}\n"\
                                    f"В контактах: {in_contact}\n"\
                                    f"Удалённый аккаунт: {deleted}\n"\
                                    f"Мой аккаунт: {is_self}\n"\
                                    f"Взаимный контакт: {is_mutual}\n"\
                                    f"Ограничения: {restricted}\n"\
                                    f"В базе скама: {scam}\n"\
                                    f"Фейковый аккаунт: {fake}")

    elif message.text == "уд":
        if message.reply_to_message.from_user.id == 1982062215:
            if message.from_user.id == 1982062215:
                await app.delete_messages(message.chat.id, message.reply_to_message.id)
                await app.delete_messages(message.chat.id, message.id)
            else:
                await app.send_message(message.chat.id, "❌ идёшь нахуй")
        else:
            await app.edit_message_text(message.chat.id, message.id, "❌ невозможно удалить это собщение")

    elif message.text == "тест":
        await app.send_message(message.chat.id, message)


    elif message.text == "юху":
        try:
            await app.edit_message_text(message.chat.id, message.id, message.chat.id)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, message.chat.type)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, message.from_user.id)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, message.from_user.is_contact)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, message.from_user.status)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, message.from_user.next_offline_date)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, message.chat.title)
            await asyncio.sleep(0.1)
            await app.edit_message_text(message.chat.id, message.id, "AQADAgADEb4xG8KXmUoAEAIAA4feI3YABAM5VEMIn9E6AAQeBA")
            await asyncio.sleep(0.2)
            await app.edit_message_text(message.chat.id, message.id, "Готово!\nВсе данные отправлены в лс")
        except:
            await app.edit_message_text(message.chat.id, message.id, "Готово!\nВсе данные отправлены в лс")



app.run()  # Automatically start() and idle()
