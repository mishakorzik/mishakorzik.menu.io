

@client.command(name="kick", aliases=['Кикнуть', 'кик', 'Кик', 'кикнуть', 'Kick'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = 'не указано'):
    title = "👢 • "+member.name+" кикнут(а)."
    async with ctx.typing():
        await member.kick()
        msg = await ctx.send(embed = discord.Embed(colour = discord.Color.red(), description = f"{member} Был кикнутый пользователем, "+ctx.author.name+" по причине: "+reason))
