import discord
import random
client = discord.Client()

# setup
PATH = "C:\Program Files (x86)/chromedriver.exe"
voimalused = ["kivi", "paber", "käärid"]
@client.event

# peame alati checkima et bot endale ei vastaks
async def on_message(message):
    if message.author == client.user:
        return
    if "?play" in message.content:
        arvuti = random.choice(voimalused)
        player = random.choice(voimalused)
        if player == arvuti:
            await message.channel.send("VIIK :face_with_monocle: Arvuti sai " + arvuti + " ja Sina said " + player)
        elif player == "kivi":
            if arvuti == "paber":
                await message.channel.send("KAOTUS :cry: Arvuti sai " + arvuti + " ja Sina said " + player)
            else:
                await message.channel.send("VÕIT :partying_face: Arvuti sai " + arvuti + " ja Sina said " + player)
        elif player == "paber":
            if arvuti == "käärid":
                await message.channel.send("KAOTUS :cry: Arvuti sai " + arvuti + " ja Sina said " + player)
            else:
                await message.channel.send("VÕIT :partying_face: Arvuti sai " + arvuti + " ja Sina said " + player)
        elif player == "käärid":
            if arvuti == "kivi":
                await message.channel.send("KAOTUS :cry: Arvuti sai " + arvuti + " ja Sina said " + player)
            else:
                await message.channel.send("VÕIT :partying_face: Arvuti sai " + arvuti + " ja Sina said " + player)

# ye hui saate mu võtme
client.run("put your key here")
