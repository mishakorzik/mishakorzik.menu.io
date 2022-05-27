#random geometry dash level

@client.command(name = "geometry", aliases=['Geometry', 'gd', 'Gd', 'геометри', 'Геометри', 'гд', 'Гд'])
async def geometry(ctx):
    gd_level = random.choice(gd_levels)
    title = "⊰🌀⊱ • "+ctx.author.name+" успешно!"
    await ctx.send(embed = discord.Embed(colour = discord.Color.green(), title = title, description = "Успешно! Вот уровень из geometry dash. "+gd_level))
