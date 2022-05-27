#Команда которая отправляет рандомную коалу
#Модули которые нужно скачать: requests, json

@client.command(aliases=["Куала"])
async def куала(ctx):
    get = requests.get("https://some-random-api.ml/animal/koala").json()
    koala = get['image']
    await ctx.send(koala)
