import discord
import random

client = discord.Client()


cards_and_values = {"poti_2": 2, "poti_3": 3, "poti_4": 4, "poti_5": 5, "poti_6": 6, "poti_7": 7, "poti_8": 8, "poti_9": 9, "poti_10": 10, "poti_poiss": 10, "poti_emand": 10, "poti_kunn": 10, "poti_ace": 11,
                    "ruutu_2": 2, "ruutu_3": 3, "ruutu_4": 4, "ruutu_5": 5, "ruutu_6": 6, "ruutu_7": 7, "ruutu_8": 8, "ruutu_9": 9, "ruutu_10": 10, "ruutu_poiss": 10, "ruutu_emand": 10, "ruutu_kunn": 10, "ruutu_ace": 11,
                    "artu_2": 2, "artu_3": 3, "artu_4": 4, "artu_5": 5, "artu_6": 6, "artu_7": 7, "artu_8": 8, "artu_9": 9, "artu_10": 10, "artu_poiss": 10, "artu_emand": 10, "artu_kunn": 10, "artu_ace": 11,
                    "risti_2": 2, "risti_3": 3, "risti_4": 4, "risti_5": 5, "risti_6": 6, "risti_7": 7, "risti_8": 8, "risti_9": 9, "risti_10": 10, "risti_poiss": 10, "risti_emand": 10, "risti_kunn": 10, "risti_ace": 11}



@client.event
async def on_message(message): # checks whether message author is the bot itself or not
    if message.author == client.user:
        return
    
    if message.content.startswith("?blackjack"):
        await message.channel.send("```Proovi saada võimalikult lähedale 21-le punktile. Et saada uus kaart, kirjuta ?hit, kui sa ei soovi uut kaarti, kirjuta ?pass```")
        salvestatud_dealer = 0 # need to define those otherwise we get an UnboundLocalError
        salvestatud_player = 0
        
        for i in range(2): # ranges player's and dealer's hands 2 times
            dealer_random_setup = random.choice(list(cards_and_values.items())) # gets us both keys and values
            dealer_random_key = "\\" + dealer_random_setup[0] + ".png" # puts only key in embed
            dealer_random_value = dealer_random_setup[1] # puts only value in embed
            embed = discord.Embed(title="Diileri käsi:", description= dealer_random_value + salvestatud_dealer, color=0xff0000) #creates embed
            file = discord.File(r"put your folder location here" + dealer_random_key, filename="image.png")
            embed.set_image(url="attachment://image.png")
            salvestatud_dealer = dealer_random_value
            global desc_dealer
            desc_dealer = embed.description
            await message.channel.send(file=file, embed=embed, delete_after=60) # sends
            player_random_setup = random.choice(list(cards_and_values.items()))
            player_random_key = "\\" + player_random_setup[0] + ".png"
            player_random_value = player_random_setup[1]
            embed = discord.Embed(title="Sinu käsi:", description= player_random_value + salvestatud_player, color=0x0011ff)
            file = discord.File(r"put your folder location here" + player_random_key, filename="image.png")
            embed.set_image(url="attachment://image.png")
            salvestatud_player = player_random_value
            global desc_player
            desc_player = embed.description #desc_player equals player_random_value and salvestatud_player
            await message.channel.send(file=file, embed=embed, delete_after=60)
        print(str(desc_dealer)) # we print it just in case, we might want to inspect some shit later
        print(str(desc_player))

    if desc_dealer == desc_player:
        await message.channel.send("```Kiire viik! Pole mõtet edasi mängida```")
    elif message.content.startswith("?hit"):
        await message.channel.send("```Sa hitid, annan sulle kaardi!```", delete_after=60)
        player_random_setup = random.choice(list(cards_and_values.items()))
        player_random_key = "\\" + player_random_setup[0] + ".png"
        player_random_value = player_random_setup[1]
        embed = discord.Embed(title="Sinu käsi:", description= player_random_value + desc_player, color=0x0011ff)
        file = discord.File(r"put your folder location here" + player_random_key, filename="image.png")
        embed.set_image(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed, delete_after=60)
        print(embed.description)
        if embed.description > 21:
            if desc_dealer > 21:
                if embed.description > desc_dealer:
                    await message.channel.send("```Kahjuks sa kaotasid! Ka dealeri punktid läksid üle 21, aga sinu skoor oli 21-st kaugemal!```")
                if embed.description < desc_dealer:
                    await message.channel.send("```Sa võitsid! Ka sinu punktid läksid üle 21, aga sinu skoor oli 21-le lähemal, kui dealeril!```")
                if embed.description == desc_dealer:
                    await message.channel.send("```Jäid dealeriga viiki!```")
                
        if embed.description == 21:
            await message.channel.send("```Sa võitsid! Said täpselt 21 punkti!```")
        if embed.description == desc_dealer:
            await message.channel.send("```Jäid dealeriga viiki!```")
        if desc_dealer == 21:
            await message.channel.send("```Sa kaotasid! Dealer sai täpselt 21 punkti!```")
        if embed.description > 21:
            if desc_dealer < 21:
                await message.channel.send("```Sa kaotasid! Su punktid läksid üle 21```")
        if embed.description < 21:
            if desc_dealer < 21:
                if embed.description < desc_dealer:
                    await message.channel.send("```Kahjuks sa kaotasid, dealer on 21-le lähemal!```")
                if embed.description > desc_dealer:
                    await message.channel.send("```Sa võitsid, sa oled 21-le lähemal, kui dealer!```")
                
        
            
            
    elif message.content.startswith("?pass"): # !!!
        global kaart_antud # this is super important, it prevents players from cheating
        kaart_antud = True # without this system players could just pass even if the dealer had perfect score                
        if desc_player > desc_dealer:
            kaart_antud = False
            await message.channel.send("```Sa passid, annan dealerile kaardi!```", delete_after=60)
            dealer_random_setup = random.choice(list(cards_and_values.items()))
            dealer_random_key = "\\" + dealer_random_setup[0] + ".png"
            dealer_random_value = dealer_random_setup[1]
            embed = discord.Embed(title="Diileri käsi:", description= dealer_random_value + desc_dealer, color=0xff0000)
            file = discord.File(r"put your folder location here" + dealer_random_key, filename="image.png")
            embed.set_image(url="attachment://image.png")
            await message.channel.send(file=file, embed=embed, delete_after=60)
            global embed_description
            embed_description = embed.description
            kaart_antud = True
        if kaart_antud == True:
            if embed_description > 21:
                if desc_player > 21:
                    if embed_description > desc_player:
                        await message.channel.send("```Sa võitsid! Ka sinu punktid läksid üle 21, aga sinu skoor oli 21-le lähemal, kui dealeril!```")
                    if embed_description < desc_player:
                        await message.channel.send("```Sa võitsid! Ka sinu punktid läksid üle 21, aga sinu skoor oli 21-le lähemal, kui dealeril!```")
                    if embed_description == desc_player:
                        await message.channel.send("```Jäid dealeriga viiki!```")
        if embed_description > 21:
            await message.channel.send("```Sa võitsid! Delari punktid läksid üle 21!```")
        if embed_description == 21:
            await message.channel.send("```Sa kaotasid! Dealer sai täpselt 21 punkti!```")
        if embed_description == desc_dealer:
            await message.channel.send("```Jäid dealeriga viiki!```")
        if embed_description < 21:
            if desc_player < 21:
                if embed_description < desc_player:
                    await message.channel.send("```Sa võitsid! Su punktid on 21-le lähemal, kui dealeril!```")
                if embed_description > desc_player:
                    await message.channel.send("```Sa kaotasid! Dealeri punktid on 21-le lähemal, kui sul!```")
        if embed_description < 21:
            if desc_player < 21:
                if embed_description < desc_dealer:
                    await message.channel.send("```Kahjuks sa kaotasid, dealer on 21-le lähemal!```")
                if embed_description > desc_dealer:
                    await message.channel.send("```Sa võitsid, sa oled 21-le lähemal, kui dealer!```")
            

client.run("put your token here")
