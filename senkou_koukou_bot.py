import discord #discordでBOTを使うのにこれが必ずいる
import random

client = discord.Client()

@client.event #BOT起動時にCMDに表示される部分で無くてもよい
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): #メッセージを受け取る関数なので必ず必要
    if message.content.startswith("start"):
        select = [message.author.name + "さんが先攻です",message.author.name + "さんが後攻です"] #メッセージのリスト
        choice = random.choice(select) #randomモジュールでselectリストからランダムに一つを選出
        await message.channel.send(choice) #結果を出力
    if message.content.startswith("ガンダムファイトレディーゴー"):
        select = [message.author.name + "さんが先攻です",message.author.name + "さんが後攻です"] #メッセージのリスト
        choice = random.choice(select) #randomモジュールでselectリストからランダムに一つを選出
        await message.channel.send(choice) #結果を出力
    if message.content.startswith("dice"):
        select = [message.author.name + "さんのサイコロの目は１です",message.author.name + "さんのサイコロの目は２です",message.author.name + "さんのサイコロの目は３です",message.author.name + "さんのサイコロの目は４です",message.author.name + "さんのサイコロの目は５です",message.author.name + "さんのサイコロの目は６です"] #メッセージのリスト
        choice = random.choice(select) #randomモジュールでselectリストからランダムに一つを選出
        await message.channel.send(choice) #結果を出力
# この＊＊＊に自分のトークンを書き替える
client.run('Njk4ODcwNTYxODY2MTIxMjI4.XpMIzg.mtzeoQZBrCg4fz3F7R2IKwlE39A')
