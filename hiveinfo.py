from selenium import webdriver
import discord
import xpath
client = discord.Client()
PATH = "C:\Program Files (x86)/chromedriver.exe"
account = ""
driver = webdriver.Chrome(PATH)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "?info " in message.content:
        account = message.content[6:99]
        lingiNimi = driver.get("https://wallet.hive.blog/@" + account + "/transfers")
        hive = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/div[2]")
        power = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[3]/div[2]")
        dollars = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[1]/div[4]/div[2]")
        embed=discord.Embed(title=" ", color=0x028de3)
        embed.set_author(name= "@" + account + " kontojääk:", icon_url="https://files.peakd.com/file/peakd-hive/hiveonboard/8inw3kx7-logo_transparent.png")
        embed.add_field(name="LIQUID", value=hive.text, inline=True)
        embed.add_field(name="POWER", value=power.text, inline=True)
        embed.add_field(name="DOLLAR", value=dollars.text, inline=True)
        await message.channel.send(embed=embed)
        
# yeah ill rather not show you my key
client.run("put your key here")
