#Список плохих пользователей - Bad users list
#Модули которые нужно скачать: discord_components.

@client.command(name="плохие", aliases=['Плохие', 'Bad', 'bad', 'плохие'])
async def плохие(ctx):
    emojis = ['🍎', '🍓', '🍒', '🍑', '🍋', '🍏', '🍐', '🥝', '🍇', '🥥', '🍠', '🥑']
    guild = ctx.guild
    try:
          emoji001 = random.choice(emojis)
          title = "⊰"+emoji001+"⊱ • "+ctx.author.name+" просмотр списка!"
          await ctx.send(embed = discord.Embed(colour = discord.Color.gold(), title = title, description = 'Упс. Мой список плохих слишком большой и я немогу отправить эго в чат, но ты можеш посмотреть эго! Внизу будет кнопка просто нажми на неё.'),
              components=[
                  Button(style=ButtonStyle.URL, emoji = "📜", label="Посмотреть список", url="https://raw.githubusercontent.com/mishakorzik/mishakorzik.menu.io/master/%D0%A1%D0%B5%D1%80%D0%B2%D0%B5%D1%80/bad_users.txt"),
              ],
          )

          res = await bot.wait_for("button_click")
          if res.channel == ctx.channel:
              await res.respond(
                   type=InteractionType.ChannelMessageWithSource,
                   content=f'{res.component.label} clicked'
          )
    except:
          title = "⊰"+emoji001+"⊱ • "+ctx.author.name+" ошибка!"
          await ctx.send(embed = discord.Embed(colour = discord.Color.red(), title = title, description = 'Ошибка! Случилась непредвиденая ошибка, и я не смог отправить вам список плохих. Код ошибки: 500'))
