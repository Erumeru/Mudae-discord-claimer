import discord
from discord.ext import commands
import requests
from colorama import init, Fore, Back, Style
import uuid

# Define the bot with the necessary intents
intents = discord.Intents.default()
intents.messages = True  # Enable the message content intent
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

#put para reaccionar a discord

# Define tu token de BOT
TOKEN = ""


mudaeCanalId=""


#Personajes a claimer, estos personajes deben coincidir exactamente con el nombre del personaje en mudae
personajes = [
    "Ramona Flowers", "Megumin", "Mai Sakurajima", "Rias Gremory",
    "Satoru Gojou", "Power", "Nezuko Kamado", "Asuna", "Albedo", "Miku Nakano",
    "Hange Zoë", "Violet Evergarden", "Shinobu Kochou", "Aqua", "Mitsuri Kanroji",
    "Rei Ayanami", "Rin Tohsaka", "Miku Nakano", "Raphtalia", "Ichika Nakano",
    "Yotsuba Nakano", "Fuutarou Uesugi", "Yuuji Itadori", "Rikka Takanashi",
    "Boa Hancock", "Tohru", "Shiro", "Maki Zenin", "Asuka Langley Souryuu",
    "Marin Kitagawa", "Hinata Hyuuga", "2B", "Roronoa Zoro", "Nobara Kugisaki",
    "Levi", "Kurumi Tokisaki", "Akeno Himejima", "Bongo Cat", "Esdeath", "Ram",
    "Monkey D. Luffy", "Yumeko Jabami", "Chika Fujiwara", "Nino Nakano", "Akame",
    "Evangelion Unit-00", "Evangelion Unit-01", "Evangelion Unit-02", "Gendou Ikari",
    "Lilith (NGE)", "Pen Pen", "Kaworu Nagisa", "Ritsuko Akagi", "Shinji Ikari",
    "Touji Suzuhara", "Scott Pilgrim", "Wallace Wells", "Lisa Miller", "Marinette Dupain-Cheng",
    "Envy Adams", "Gideon Graves", "Joseph Z", "Julie Powers", "Ken Katayanagi",
    "Kyle Katayanagi", "Lisa Miller", "Lynette Guycott", "Matthew Patel", "Mr. Chau",
    "Roxanne Richter", "Tamara Chen", "Todd Ingram", "Young Neil", "Kei Shirogane",
    "Miko Iino", "Yuu Ishigami", "Vicious", "Spike Spiegel", "Jet Black", "Ein", "Maomao",
    "Marinette Dupain-Cheng", "Sung Jin-Woo", "Cha Hae-In", "Akame", "Nezuko Kamado",
    "Momo Yaoyorozu", "Gelda", "Sabo", "Portgas D. Ace", "Lancelot (MnY)", "Tristan Liones",
    "Anne (MnY)", "Rin Tohsaka", "Kaori Miyazono","Ikuyo Kita","Hitori Gotou","Ryou Yamada","Seika Ijichi","Nijika Ijichi","Tanjirou Kamado","Asta","Ryuuko Matoi","Saitama","Guts","Soul of Cinder"
    ,"Kensuke Aida","Ryouji Kaji","Yui Ikari","Clementine","Rio Futaba","Nami","Kobayashi","Zero Two","Rem","Megumin","Hatsune Miku","Saber","Nico Robin","Kaguya Shinomiya","Ai Hayasaka"
    ,"Yor Forger","Himiko Toga","Sakuta Azusagawa","Knives Chau"
]
init()


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')


async def reaccionar(messageId, canalId):
    data = {'key': 'value'}
    #TOKENS DE USUARIOS QUE REACCIONAN
    headers1 = {'Authorization': ''} #eruma
    headers2 = {'Authorization': ''} #arredondospo
    headers3 = {'Authorization': ''} #elmerfon
    headers4 = {'Authorization': ''} #Reodca

    urlreaccionar = f"https://discord.com/api/v9/channels/{canalId}/messages/{messageId}/reactions/%E2%9C%85/%40me?location=Message&type=0"
    response1 = requests.put(urlreaccionar, json=data, headers=headers1)
    response2 = requests.put(urlreaccionar, json=data, headers=headers2)
    response3 = requests.put(urlreaccionar, json=data, headers=headers3)
    response4 = requests.put(urlreaccionar, json=data, headers=headers4)

    if response1.status_code == 204:
        print('Petición PUT exitosa.')
    else:
        print('Error al hacer la petición PUT.')
        print('Código de estado:', response1.status_code)
    if response2.status_code == 204:
        print('Petición PUT exitosa.')
    else:
        print('Error al hacer la petición PUT.')
        print('Código de estado:', response2.status_code)
    if response3.status_code == 204:
        print('Petición PUT exitosa.')
    else:
        print('Error al hacer la petición PUT.')
        print('Código de estado:', response3.status_code)
    if response4.status_code == 204:
        print('Petición PUT exitosa.')
    else:
        print('Error al hacer la petición PUT.')
        print('Código de estado:', response4.status_code)

# Funcion para comparar el nombre
def contiene_personajes_clave(message, personajes):
    return any(personaje.lower() == message.lower() for personaje in personajes)


#se supone esta debe hacer el wish
async def send_interaction(messageId, custom_id_btn_id, canalId):
    # Define the URL for the Discord API endpoint
    url = "https://discord.com/api/v9/interactions"


    #TOKENS DE USUARIOS QUE REACCIONAN
    headers4 = {'Authorization': ''} #eruma
    headers2 = {'Authorization': ''} #arredondospo
    headers3 = {'Authorization': ''} #elmerfon
    headers1 = {'Authorization': ''} #Reodca
    nonce = str(uuid.uuid4())[:32]
    # Define the JSON payload
    payload = {
        "type": 3, #STOCk
        "nonce": nonce,
        "guild_id": "", #Guild id NO
        "channel_id": canalId, #Channel id NO
        "message_flags": 0, #STOCK NO
        "session_id":"", #PUEDESER
        "message_id": messageId, #Message id SI
        "application_id": "", #Mudae Id NO
        "data": {   #STOCK
            "component_type": 2,
            "custom_id": custom_id_btn_id
        }
    }

    # Send the POST request
    response1 = requests.post(url, json=payload, headers=headers1)
    response2 = requests.post(url, json=payload, headers=headers2)
    response3 = requests.post(url, json=payload, headers=headers3)
    response4 = requests.post(url, json=payload, headers=headers4)

    # Print the response
    if response1.status_code == 204:
        print("Request was successful")
        print(response1.text)
    else:
        print("Failed to send request")
        print(f"Status code: {response1.status_code}")
        print(response1.text)
# Print the response
    if response2.status_code == 204:
        print("Request was successful")
        print(response2.text)
    else:
        print("Failed to send request")
        print(f"Status code: {response2.status_code}")
        print(response2.text)
# Print the response
    if response3.status_code == 204:
        print("Request was successful")
        print(response3.text)
    else:
        print("Failed to send request")
        print(f"Status code: {response3.status_code}")
        print(response3.text)
# Print the response
    if response4.status_code == 204:
        print("Request was successful")
        print(response4.text)
    else:
        print("Failed to send request")
        print(f"Status code: {response4.status_code}")
        print(response4.text)



@bot.event
async def on_message(message):
    # Imprime el contenido del mensaje y el nombre del autor en la consola
    print(f"Message from {message.author}: {message}")
    #print(f"mensaje:{message.message_content}")
    #await send_interaction(messageId=message.id, custom_id_btn_id=message.components[0].components[0].custom_id)
    if message.components:
        #if message.components[0].children[0].emoji.name != 'wleft':
        await send_interaction(messageId=message.id, custom_id_btn_id=message.components[0].children[0].custom_id, canalId=message.channel.id)
    if message.embeds:
        print(f"Message from MUDAE {message.author}: {message.embeds[0].author.name}")
        if contiene_personajes_clave(message.embeds[0].author.name,personajes):
            print(message.id)
            print(mudaeCanalId)
            await reaccionar(messageId=message.id, canalId=message.channel.id)
            print(Fore.GREEN+"Se reaccionó a: "+message.embeds[0].author.name+Style.RESET_ALL)
    # await message.add_reaction("🤙")
    # Procesa los comandos si los hay
    await bot.process_commands(message)

# Ejecuta el bot con el token especificado
bot.run(TOKEN)