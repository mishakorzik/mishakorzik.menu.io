@bot.command(name="mute", aliases=['Мьют', 'мьют', 'Mute'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason='не указано'):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Mьют")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Mьют")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(colour = discord.Color.green(), description = f"{ctx.author.name} замьютил пользователя {member} по причине: "+reason)
    await ctx.send( embed = embed )
    title = "🤐 - "+member.name+" замьючен(а)."
    await member.send(embed = discord.Embed(colour = discord.Color.blue(), title = title, description = '> замьючен(а) на сервере: '+ctx.guild.name+'\n> Администратором: '+ctx.author.name+'\n> По причине: '+reason))
