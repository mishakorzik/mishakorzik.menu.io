#random geometry dash level

@client.command(name = "geometry", aliases=['Geometry', 'gd', 'Gd', 'геометри', 'Геометри', 'гд', 'Гд'])
async def geometry(ctx):
    gd_levels = ["уровень 1", "уровень 2", "уровень 3"]
    gd_level = random.choice(gd_levels)
    title = " 🌀 "+ctx.author.name+" успішно!"
    await ctx.send(embed = discord.Embed(colour = discord.Color.green(), title = title, description = "Успішно! Ось уровень geometry dash. "+gd_level))
