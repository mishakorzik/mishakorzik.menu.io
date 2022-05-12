#Команда которая отправляет рандомную лису
#Модули которые нужно скачать: requests, json

@bot.command(aliases=["Лиса"])
async def лиса(ctx):
    get = requests.get("https://some-random-api.ml/animal/fox").json()
    fox = get['image']
    await ctx.send(fox)
