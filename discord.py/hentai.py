#Хентай команда - Hentai command
#Модули которые нужно скачать: hmtai

@client.command(name="хентай", aliases=["Хентай", "Hentai", "hentai"])
async def хентай(ctx):
    if ctx.channel.is_nsfw():
        num_list = [1, 2]
        num = random.choice(num_list)
        text = hmtai.useHM(num, "hentai")
        await ctx.send(text)
