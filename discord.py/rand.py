#Рандомное число от 1 до 100 - random number from 1 to 100
#Модули которые нужно скачать: random

def roll_convert(argument):
    intarg = int(argument)
    switcher = {
        1: ":one:",
        2: ":two:",
        3: ":three:",
        4: ":four:",
        5: ":five:",
        6: ":six:",
        7: ":seven:",
        8: ":eight:",
        9: ":nine:",
        0: ":zero:"
    }
    return switcher.get(intarg, "what")

@client.command(aliases = ['random', 'Random', 'Roll', 'roll', 'Рандом', 'рандом'])
async def __roll(ctx):
    r = str(random.randrange(1, 101))
    mes = 'Рандомное число  -  '
    for m in r:
        mes += roll_convert(m)
    await ctx.send(embed = discord.Embed(colour = discord.Color.gold(), description = mes))
