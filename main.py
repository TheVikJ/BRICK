import requests
import json
import discord
from pyunsplash import PyUnsplash
import random
import os

pu = PyUnsplash(api_key=os.environ['api_key'])

client = discord.Client()
TOKEN = os.environ['TOKEN']

general_links = ["http://www.counseling.org/,", "http://www.apa.org/","http://www.nimh.nih.gov/","http://www.nmha.org/","http://www.healthywomen.org/","http://www.nami.org/", "http://www.samhsa.gov/","http://www.wfmh.org/","http://www.healthyplace.com/"]

suicide_links = ["http://www.afsp.org/", "http://www.save.org/","http://www.metanoia.org/suicide/", "http://beyondmeds.com/", "http://www.helpguide.org/articles/depression/dealing-with-depression.htm", "http://douglascootey.com/", "http://depressionmarathon.blogspot.com/", "http://blogs.psychcentral.com/depression/", "https://www.imalive.org/"]

depression_links = ["http://www.apa.org/topics/depress/recover.aspx","https://www.vandrevalafoundation.com/", "https://depression.org.nz/","https://www.helpguide.org/home-pages/depression.htm","https://www.who.int/news-room/fact-sheets/detail/depression","https://adaa.org/","https://www.psychiatry.org/patients-families/depression","https://www.healthline.com/health/depression/help-for-depression","https://www.mayoclinic.org/diseases-conditions/depression/diagnosis-treatment/drc-20356013","https://www.helpguide.org/articles/depression/coping-with-depression.htm","https://my.clevelandclinic.org/health/diseases/9290-depression","https://www.nimh.nih.gov/health/publications/depression"]

anxiety_links = ["http://www.adaa.org/","http://www.helpguide.org/articles/anxiety/how-to-stop-worrying.htm","http://www.positivelypositive.com/","http://www.anxietyguru.net/","http://www.anxietyslayer.com/","http://socialanxietydisorder.about.com/","http://psychcentral.com/lib/6-ways-to-overcome-social-anxiety/","http://anxietynetwork.com/","http://www.apa.org/pubinfo/panic.html"]

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.lower().startswith("!dogpic"):
    res = json.loads(requests.get("https://dog.ceo/api/breeds/image/random").text)
    await message.channel.send(res["message"])

  if message.content.lower().startswith("!catpic"):
    res = requests.get("https://aws.random.cat/meow")
    data = json.loads(res.text)
    await message.channel.send(data['file'])

  if message.content.lower().startswith("!foxpic"):
    res = json.loads(requests.get("https://randomfox.ca/floof/").text)
    await message.channel.send(res['image'])

  if message.content.lower().startswith("!general"):
    msg = "Thanks for requesting for some mental health resources.\nHere are some general links to help with mental health: "
    for link in general_links:
      msg += "\n" + link
    await message.reply(content=msg)

  if message.content.lower().startswith("!suicide"):
    msg = "Thanks for requesting for some mental health resources.\nHere are some links to help with ymental health and suicidal thoughts: "
    for link in suicide_links:
      msg += "\n" + link
    await message.reply(content=msg)

  if message.content.lower().startswith("!depression"):
    msg = "Thanks for requesting for some mental health resources.\nHere are some general links to help with mental health, depression and mood disorders: "
    for link in depression_links:
      msg += "\n" + link
    await message.reply(content=msg)

  if message.content.lower().startswith("!anxiety"):
    msg = "Thanks for requesting for some mental health resources.\nHere are some general links to help with mental health and anxiety: "
    for link in anxiety_links:
      msg += "\n" + link
    await message.reply(content=msg)

  if message.content.lower().startswith("!mindfulness"):
    msg = "Here's a mindfulness prompt: \n"
    photos = pu.photos(type_='random', count=1, featured=True, query=random.choice(["ocean", "river", "nature", "forest", "mountain"]))
    [photo] = photos.entries
    msg += str(photo.link_download)[:-len("download")]
    await message.reply(content=msg)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  print("Number of servers: " + str(len(client.guilds)))

client.run(TOKEN)