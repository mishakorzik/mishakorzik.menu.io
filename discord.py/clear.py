@bot.command(name="clear", usage="очистить <количество сообщений>", aliases=['Очистить', 'очистить'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, kolvo = 100):
    messages = await ctx.channel.purge( limit = kolvo )
    await ctx.send(embed = discord.Embed(colour = discord.Color.green(), description = f"✅ очисщено {len(messages)} сообщения!"))
