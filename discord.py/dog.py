#Команда которая отправляет рандомную кошку
#Модули которые нужно скачать: requests, json

@client.command(aliases=["Кот"])
async def кот(ctx):
    get = requests.get("https://some-random-api.ml/animal/dog").json()
    fox = get['image']
    await ctx.send(fox)
