import os
import discord
from discord.ext import commands
import numpy as np
import random

wall = "⬜"
innerWall = "⬛"
energy = "🍎"
snakeHead = "😍"
snakeBody = "🟨"
snakeLoose = "😵"


def getGameGrid():
    str = ""

    for item in snakeMatrix:
        # print(item)
        for i in item:
            if(i == 0):
                str += wall
            elif i == 1:
                str += innerWall
            elif i == 2:
                str += snakeHead
            elif i == 3:
                str += snakeBody
            elif i == 4:
                str += energy
            else:
                str += snakeLoose
        str += "\n"
        
    return str

def generateRandomEnergy():
    snakeMatrix[random.randint(1,10)][random.randint(1,10)] = 4

def checkEnergy(i, j):
    # print("i : {}".format(i))
    # print("j : {}".format(j))
    # print("Pos Val : {}".format(snakeMatrix[i][j]))
    return snakeMatrix[i][j] == 4

def handleEnergy(i, j):
    global points
    # print(checkEnergy(i, j))
    if(checkEnergy(i, j)):
        generateRandomEnergy()
        points += 1

def updateSnakePosition(i, j, k, l):
    snakeMatrix[i][j] = 2
    snakeMatrix[k][l] = 1

def isOuterBoundary(i, j):
    global isOut
    if(i == 0 or j == 0 or i == 11 or j == 11):
        # print("Out")
        snakeHeadPos = np.argwhere(snakeMatrix == 2)[0]
        snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]] = 5
        isOut = True
        print("isOut : {}".format(isOut))
        return True
    return False

def moveUp():
    # print("Up")
    snakeHeadPos = np.argwhere(snakeMatrix == 2)[0]
    # print(snakeHeadPos)
    # print(snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]])
    if(not isOuterBoundary(snakeHeadPos[0]-1, snakeHeadPos[1])):
        handleEnergy(snakeHeadPos[0]-1, snakeHeadPos[1])
        updateSnakePosition(snakeHeadPos[0]-1, snakeHeadPos[1], snakeHeadPos[0], snakeHeadPos[1])
    # snakeMatrix[snakeHeadPos[0]-1][snakeHeadPos[1]] = 2
    # snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]] = 1


def moveLeft():
    # print("Left")
    snakeHeadPos = np.argwhere(snakeMatrix == 2)[0]
    if(not isOuterBoundary(snakeHeadPos[0], snakeHeadPos[1]-1)):
        handleEnergy(snakeHeadPos[0], snakeHeadPos[1]-1)
        updateSnakePosition(snakeHeadPos[0], snakeHeadPos[1]-1, snakeHeadPos[0], snakeHeadPos[1])
    # snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]-1] = 2
    # snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]] = 1


def moveRight():
    # print("Right")
    snakeHeadPos = np.argwhere(snakeMatrix == 2)[0]
    if(not isOuterBoundary(snakeHeadPos[0], snakeHeadPos[1]+1)):
        handleEnergy(snakeHeadPos[0], snakeHeadPos[1]+1)
        updateSnakePosition(snakeHeadPos[0], snakeHeadPos[1] + 1, snakeHeadPos[0], snakeHeadPos[1])
    # snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]+1] = 2
    # snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]] = 1


def moveDown():
    # print("Down")
    snakeHeadPos = np.argwhere(snakeMatrix == 2)[0]
    if(not isOuterBoundary(snakeHeadPos[0]+1, snakeHeadPos[1])):
        handleEnergy(snakeHeadPos[0]+1, snakeHeadPos[1])
        updateSnakePosition(snakeHeadPos[0]+1, snakeHeadPos[1], snakeHeadPos[0], snakeHeadPos[1])
    # snakeMatrix[snakeHeadPos[0]+1][snakeHeadPos[1]] = 2
    # snakeMatrix[snakeHeadPos[0]][snakeHeadPos[1]] = 1

def reset():
    global snakeMatrix, isOut, points
    isOut = False
    # print("Reset")
    snakeMatrix = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    points = 0
    generateRandomEnergy()

def getNormalEmbededData(title, description):
    return discord.Embed(title=title, description=description, color=discord.Color.green())

def getErrorEmbededData(title, description):
    return discord.Embed(title=title, description=description, color=discord.Color.red())


async def sendMessage(message):
    embedVar=getNormalEmbededData(title="Pick Apple Game", description="{}".format(getGameGrid()))
    embedVar.add_field(name="Your Score", value=points, inline=True)
    await message.channel.send(embed=embedVar)

client = discord.Client()

@client.event
async def on_ready():
  print("You have logged in as {0.user}".format(client))

# await channel.send('hello')
@client.event
async def on_message(message):
  # print("Message Channel : {}".format(message.channel))
  # print(os.environ['CHANNEL_ID'])
  gameChannel = client.get_channel(int(os.environ['CHANNEL_ID']))
  # print("gameChannel Channel : {}".format(gameChannel))
  if(message.author == client.user):
        return
  if gameChannel == message.channel:
    if(message.content.startswith('!hello')):
        # print(message.channel)
        reset()
        embedVar = getNormalEmbededData(title="Welcome *{0.author}* to our Useless Game Channel ! Lets Play Game".format(message), description="⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜\n⬜⬛⬛⬛⬛⬛⬛⬛🍎⬛⬜\n⬜⬛🟨🟨⬛⬛⬛⬛⬛⬛⬜\n⬜⬛⬛🟨🟨🟨🟨⬛⬛⬛⬜\n⬜⬛⬛⬛⬛⬛🟨🟨⬛⬛⬜\n⬜⬛⬛⬛⬛⬛⬛🟨🟨😵⬜\n⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜\n⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜\n⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n\n` w ` -> Move Left\n` d ` -> Move Right\n` w ` -> Move Up\n` s ` -> Move Down\n` r ` -> Reset")
        await message.channel.send(embed=embedVar)
    elif(message.content.startswith('r')):
        print("Reset")
        reset()
        embedVar=getNormalEmbededData(title="Pick Apple Game", description="{}\nGame has been reset. You can start playing new game".format(getGameGrid()))
        embedVar.add_field(name="Your Score", value=points, inline=True)
        await message.channel.send(embed=embedVar)
    elif(isOut):
        embedVar=getErrorEmbededData(title="Game Over", description="Scored Point : {}".format(points))
        await message.channel.send(embed=embedVar)
    elif(message.content.startswith('w')):
        moveUp()
        await sendMessage(message)
    elif(message.content.startswith('a')):
        moveLeft()
        await sendMessage(message)
    elif(message.content.startswith('s')):
        moveDown()
        await sendMessage(message)
    elif(message.content.startswith('d')):
        moveRight()
        await sendMessage(message)
    else:
        embedVar = getErrorEmbededData(title="*Error*", description="Invalid Input Detected ! Please enter a valid input. \n ` w ` -> Move Left\n` d ` -> Move Right\n` w ` -> Move Up\n` s ` -> Move Down\n` r ` -> Reset")
        await message.channel.send(embed=embedVar)
  else:
    print("Wrong Channel")
        
@commands.command(name='test')
async def check(self, ctx):
    if ctx.channel.name == 'game':
        await ctx.send("Response message")

my_secret = os.environ['TOKEN']
points = 0
isOut = False
snakeMatrix = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])
generateRandomEnergy()
client.run("")
