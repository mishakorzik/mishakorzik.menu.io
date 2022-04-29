#Команда пинг - ping command

@client.command(name="ping", aliases=['Пинг', 'Понг', 'понг', 'Пінг', 'пінг', 'Ping', 'пинг', 'ping']
async def ping(ctx, text = 'нету'):
    ms = f'Пинг бота: {round(bot.latency * 1000)}'
    text = ms+'ms'
    await ctx.send(embed = discord.Embed(description = text))
