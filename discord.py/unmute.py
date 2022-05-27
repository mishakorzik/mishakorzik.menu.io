#команда размьют - unmutu command

@client.command(name="unmute", aliases=['Unmute', 'Розмьт', 'розмьт', 'размьют', 'Размьют'])
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Зaглушен(а)")
    await member.remove_roles(mutedRole)
    await ctx.send(embed = discord.Embed(colour = discord.Color.green(), description = f"{member} Был розмьючен учасником, "+ctx.author.name))
    title = " 😀 "+member.name+" розмьючен(а)."
    await member.send(embed = discord.Embed(colour = discord.Color.red(), title = title, description = '> розмьючен на сервере: '+ctx.guild.name+'\n> Администратором: '+ctx.author.name))
