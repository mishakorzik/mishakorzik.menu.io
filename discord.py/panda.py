#Команда которая отправляет рандомную панду
#Модули которые нужно скачать: requests, json

@client.command(aliases=["Панда"])
async def панда(ctx):
    get = requests.get("https://some-random-api.ml/animal/panda").json()
    panda = get['image']
    await ctx.send(panda)
