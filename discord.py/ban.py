@client.command(name="ban", aliases=['Забанить', 'Бан', 'бан', 'Забанити', 'забанити', 'забанить', 'Ban'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason = 'Не указано'):
    title = "⊰💾⊱ • "+member.name+" забанен(а)."
    async with ctx.typing():
        await member.ban(reason=reason)
        msg = await ctx.send(embed = discord.Embed(colour = discord.Color.green(), description = f"{member} Был забанен на сервере навсегда пользователем, "+ctx.author.name))
