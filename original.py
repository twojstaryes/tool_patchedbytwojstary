# Patched by twojstary


import tls_client
import threading
import platform
import websocket
import requests
import logging
import toml
import random
import ctypes
import uuid
import time
import base64
import json
import sys
import os
import pymysql
from pystyle import Colorate, Colors
from colorama import Fore, Style
from websocket import WebSocket
from datetime import datetime
from uuid import uuid4
color_pink = Fore.LIGHTMAGENTA_EX
color_gray = Fore.LIGHTBLACK_EX
color_reset = Style.RESET_ALL
color_magenta = Fore.MAGENTA
color_yellow = Fore.YELLOW
color_green = Fore.GREEN
color_blue = Fore.BLUE
color_cyan = Fore.CYAN
color_red = Fore.RED

def check_system():
    os_name = platform.system()
    if os_name == 'Windows':
        system = 'windows'
    else:  # inserted
        if os_name == 'Linux':
            system = 'linux'
        else:  # inserted
            if os_name == 'Darwin':
                system = 'darwin'
    return system

def cls():
    system = check_system()
    if system == 'windows':
        os.system('cls')
    else:  # inserted
        os.system('clear')

def tokens_amount():
    with open('./data/tokens.txt', 'r') as file:
        tokens_amount = len(file.readlines())
        return tokens_amount

def window_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def main_title():
    tokens = tokens_amount()
    window_title(f'Made by Stritixx | Patched by twojstary | Tokens: {tokens}')

def clean_tokens():
    with open('./data/tokens.txt', 'r+') as file:
        lines = file.readlines()
        lines = [line for line in lines if line.strip()]
        file.seek(0)
        file.writelines(lines)
        file.truncate()

def company_name():
    print(Colorate.Horizontal(Colors.purple_to_blue, '\n                                  ______  ____________________________________  ___________\n                                  ___  / / /__    |__  __/__    |_  ____/__  / / /__  ____/\n                                  __  /_/ /__  /| |_  /  __  /| |  /    __  /_/ /__  __/   \n                                  _  __  / _  ___ |  /   _  ___ / /___  _  __  / _  /___   \n                                  /_/ /_/  /_/  |_/_/    /_/  |_\\____/  /_/ /_/  /_____/   \n          \n    ', 1))

def double_break():
    print('\n\n')

def check_license():
    with open('./config/config.toml', 'r') as file:
        data = toml.load(file)
        license = data.get('login', {}).get('license', None)
        if license == '':
            return
        return license

def add_login(user_key):
    try:
        data = {'login': {'license': user_key}}
        with open('./config/config.toml', 'w') as file:
            toml.dump(data, file)
        initialize_ui()
    except:
        initialize_ui()
        input(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} Nie udało się zapisać danych logowania!")

def menu():
    print(f'                 {color_pink}01{color_reset} > ᴊᴏɪɴᴇʀ             {color_pink}06{color_reset} > ɢᴜɪʟᴅ ᴄʜᴇᴄᴋᴇʀ      {color_pink}11{color_reset} > ᴛᴏᴋᴇɴ ғᴏʀᴍᴀᴛᴛᴇʀ      {color_pink}16{color_reset} > ᴠᴏɪᴄᴇ sᴘᴀᴍᴍᴇʀ')
    print(f'                 {color_pink}02{color_reset} > ʟᴇᴀᴠᴇʀ             {color_pink}07{color_reset} > ᴛᴏᴋᴇɴ ᴄʜᴇᴄᴋᴇʀ      {color_pink}12{color_reset} > ᴛᴏᴋᴇɴ ᴏɴʟɪɴᴇʀ        {color_pink}17{color_reset} > sᴏᴜɴᴅ sᴘᴀᴍᴍᴇʀ')
    print(f'                 {color_pink}03{color_reset} > ᴀᴅᴅ ʀᴇᴀᴄᴛɪᴏɴ       {color_pink}08{color_reset} > ɴᴀᴍᴇ ᴄʜᴀɴɢᴇʀ       {color_pink}13{color_reset} > ʙɪᴏ ᴄʜᴀɴɢᴇʀ          {color_pink}18{color_reset} > ᴏɴʙᴏᴀʀᴅ ʙʏᴘᴀss')
    print(f'                 {color_pink}04{color_reset} > ᴅᴇʟ ʀᴇᴀᴄᴛɪᴏɴ       {color_pink}09{color_reset} > ʀᴜʟᴇs ʙʏᴘᴀss       {color_pink}14{color_reset} > ᴛʜʀᴇᴀᴅ sᴘᴀᴍᴍᴇʀ       {color_pink}19{color_reset} > ᴄᴀʟʟ sᴘᴀᴍᴍᴇʀ')
    print(f'                 {color_pink}05{color_reset} > ʙᴜᴛᴛᴏɴ ʙʏᴘᴀss      {color_pink}10{color_reset} > sᴘᴀᴍᴍᴇʀ            {color_pink}15{color_reset} > ғʀɪᴇɴᴅ sᴘᴀᴍᴍᴇʀ       {color_pink}20{color_reset} > ???')

def initialize_ui():
    cls()
    double_break()
    clean_tokens()
    company_name()
    main_title()
    double_break()

def initialize_ui_with_menu():
    cls()
    double_break()
    clean_tokens()
    company_name()
    double_break()
    main_title()
    menu()
    double_break()

def all_tokens():
    clean_tokens()
    with open('./data/tokens.txt', 'r') as file:
        return file.read().splitlines()

def check_setup():
    with open('./config/config.toml', 'r') as file:
        data = toml.load(file)
        proxy = data.get('setup', {}).get('proxy', None)
        if proxy == '':
            return
        return proxy

def joiner(token, invite):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'referer': 'https://discord.com/channels/@me', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjQ2NjAzMDcxMjQ4NzY3Mzg2MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI3NjIxMDQ2MzAyMjU1MzQ5OTciLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzA2MjA4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'}
    paylaod = {'session_id': str(uuid.uuid4())}
    rr = session.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers, json=paylaod, proxy=proxy)
    if rr.status_code == 200:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[JOINED]{color_reset}")
    else:  # inserted
        if rr.status_code == 400:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_yellow}[CAPTCHA]{color_reset}")
        else:  # inserted
            if rr.status_code == 403 and '40007' in rr.text:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[BANNED]{color_reset}")
            else:  # inserted
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
                logging.basicConfig(filename='./data/logs/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
                logging.error(f'=> Joiner => {rr.status_code} => {rr.text}')

def leaver(token, guild_id):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'ar', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzA2MjA4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'}
    payload = {'lurking': False}
    rr = session.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild_id}', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[LEFT SERVER]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10004' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[TOKEN ISN\'T IN SERVER]{color_reset}")
        else:  # inserted
            if rr.status_code == 401:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID TOKEN]{color_reset}")
            else:  # inserted
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
                logging.basicConfig(filename='./data/logs/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
                logging.error(f'=> Leaver => {rr.status_code} => {rr.text}')

def add_reaction(token, message_link, emoji):
    channel = message_link.split('/')[5]
    message = message_link.split('/')[6]
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'ar', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzA2MjA4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'}
    params = {'location': 'Message', 'type': '0'}
    rr = session.put(f'https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji}/@me', headers=headers, params=params, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[REACTED]{color_reset}")
    if rr.status_code == 404 and '10003' in rr.text:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID CHANNEL ID]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10008' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID MESSAGE ID]{color_reset}")
        else:  # inserted
            if rr.status_code == 403 and 'Missing Access' in rr.text:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[MISSING ACCESS]{color_reset}")
            else:  # inserted
                if rr.status_code == 401:
                    print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID TOKEN]{color_reset}")

def add_custom_reaction(token, message_link, emoji_number):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    emoji_number = emoji_number - 1
    channel = message_link.split('/')[5]
    message = message_link.split('/')[6]
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'ar', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MzA2MjA4LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'}
    params = {'limit': '50', 'around': message}
    rr = session.get(f'https://discord.com/api/v9/channels/{channel}/messages', params=params, headers=headers, proxy=proxy)
    data = rr.json()
    all_messages = [checking_message for checking_message in data if checking_message.get('id') == str(message)]
    emoji_name = ''
    should_continue = False
    for check_message in all_messages:
        if 'reactions' in check_message:
            reactions_amount = min(len(check_message['reactions']), 20)
            for index, reakcja in enumerate(check_message['reactions'][:reactions_amount]):
                emoji_name = reakcja['emoji']['name']
                emoji_id = reakcja['emoji']['id']
                if 0 <= emoji_number < reactions_amount:
                    emoji_name = check_message['reactions'][emoji_number]['emoji']['name']
                    emoji_id = check_message['reactions'][emoji_number]['emoji']['id']
                else:  # inserted
                    should_continue = True
                    break
        if should_continue:
            print(f"{color_magenta} {datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} Your emoji number is wrong!")
            break
    rr = session.put(f'https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji_name}:{emoji_id}/@me', headers=headers, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[REACTED]{color_reset}")
    if rr.status_code == 404 and '10003' in rr.text:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID CHANNEL ID]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10008' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID MESSAGE ID]{color_reset}")
        else:  # inserted
            if rr.status_code == 403 and 'Missing Access' in rr.text:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[MISSING ACCESS]{color_reset}")
            else:  # inserted
                if rr.status_code == 401:
                    print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID TOKEN]{color_reset}")

def remove_reaction(token, message_link, emoji):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    params = {'location': 'Message', 'burst': 'false'}
    channel = message_link.split('/')[5]
    message = message_link.split('/')[6]
    rr = session.delete(f'https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji}/@me', headers=headers, params=params, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[DELETED REACTION]{color_reset}")
    if rr.status_code == 404 and '10003' in rr.text:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID CHANNEL ID]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10008' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID MESSAGE ID]{color_reset}")
        else:  # inserted
            if rr.status_code == 403 and 'Missing Access' in rr.text:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[MISSING ACCESS]{color_reset}")
            else:  # inserted
                if rr.status_code == 401:
                    print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID TOKEN]{color_reset}")

def remove_custom_reaction(token, message_link, emoji_number):
    channel = message_link.split('/')[5]
    message = message_link.split('/')[6]
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    params = {'limit': '50', 'around': message}
    rr = session.get(f'https://discord.com/api/v9/channels/{channel}/messages', params=params, headers=headers, proxy=proxy)
    data = rr.json()
    all_messages = [checking_message for checking_message in data if checking_message.get('id') == str(message)]
    emoji_name = ''
    should_continue = False
    for check_message in all_messages:
        if 'reactions' in check_message:
            reactions_amount = min(len(check_message['reactions']), 20)
            for index, reakcja in enumerate(check_message['reactions'][:reactions_amount]):
                emoji_name = reakcja['emoji']['name']
                emoji_id = reakcja['emoji']['id']
            if 0 <= emoji_number < reactions_amount:
                emoji_name = check_message['reactions'][emoji_number]['emoji']['name']
                emoji_id = check_message['reactions'][emoji_number]['emoji']['id']
            else:  # inserted
                should_continue = True
                break
        if should_continue:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} Your emoji number is wrong!")
            break
    params = {'location': 'Message', 'burst': 'false'}
    rr = session.delete(f'https://discord.com/api/v9/channels/{channel}/messages/{message}/reactions/{emoji_name}:{emoji_id}/@me', headers=headers, params=params, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[DELETED REACTION]{color_reset}")
    if rr.status_code == 404 and '10003' in rr.text:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID CHANNEL ID]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10008' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID MESSAGE ID]{color_reset}")
        else:  # inserted
            if rr.status_code == 403 and 'Missing Access' in rr.text:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[MISSING ACCESS]{color_reset}")
            else:  # inserted
                if rr.status_code == 401:
                    print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID TOKEN]{color_reset}")

def button_bypass(token, message_link, button_number):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    guild_id = message_link.split('/')[4]
    channel_id = message_link.split('/')[5]
    message_id = message_link.split('/')[6]
    rr = session.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, proxy=proxy)
    data = rr.json()
    all_messages = [checking_message for checking_message in data if checking_message.get('id') == str(message_id)]
    button_ids = []
    for message in all_messages:
        bot_data = message.get('author')
        bot_id = bot_data['id']
        for component in message['components']:
            for button in component['components']:
                if button.get('custom_id', {}):
                    custom_id = button['custom_id']
                    button_ids.append(custom_id)
    button_id = button_ids[button_number - 1]
    payload = {'type': 3, 'message_id': message_id, 'channel_id': channel_id, 'guild_id': guild_id, 'data': {'component_type': 2, 'custom_id': button_id}, 'application_id': bot_id, 'session_id': uuid4().hex}
    rr = session.post('https://discord.com/api/v9/interactions', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CLICKED BUTTON]{color_reset}")
    if rr.status_code == 404 and '10003' in rr.text:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID CHANNEL ID]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10008' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID MESSAGE ID]{color_reset}")
        else:  # inserted
            if rr.status_code == 403 and 'Missing Access' in rr.text:
                print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[MISSING ACCESS]{color_reset}")
            else:  # inserted
                if rr.status_code == 401:
                    print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[INVALID TOKEN]{color_reset}")

def guild_checker(token, guild_id):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    rr = session.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers, proxy=proxy)
    if rr.status_code == 200:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[IN SERVER]{color_reset}")
    else:  # inserted
        if rr.status_code == 404 and '10004' in rr.text:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[OUT OF SERVER]{color_reset}")
        else:  # inserted
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
            logging.basicConfig(filename='./data/logs/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(f'=> Guild checker => {rr.status_code} => {rr.text}')

def token_checker(token, valid_tokens, locked_tokens, invalid_tokens):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    rr = session.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers, proxy=proxy)
    if rr.status_code in [200, 204]:
        valid_tokens.append(token)
    else:  # inserted
        if rr.status_code == 403:
            locked_tokens.append(token)
        else:  # inserted
            if rr.status_code == 401:
                invalid_tokens.append(token)
            else:  # inserted
                invalid_tokens.append(token)

def nick_changer(token, nickname):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    payload = {'global_name': f'{nickname}'}
    rr = session.patch('https://discord.com/api/v9/users/@me', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 200:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CHANGED NICKNAME]{color_reset}")
    else:  # inserted
        if rr.status_code == 400:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_yellow}[CAPTCHA]{color_reset}")
        else:  # inserted
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
            logging.basicConfig(filename='./data/logs/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(f'=> Nick changer => {rr.status_code} => {rr.text}')

def rules_bypass(token, guild_id):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    payload = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false', headers=headers, proxy=proxy).json()
    rr = session.put(f'https://discord.com/api/v9/guilds/{guild_id}/requests/@me', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 201:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[RULES BYPASSED]{color_reset}")
    else:  # inserted
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
        logging.basicConfig(filename='./data/logs/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.error(f'=> Rules bypass => {rr.status_code} => {rr.text}')

def spammer(channels_ids, message):
    while True:  # inserted
        tokens = all_tokens()
        token = random.choice(tokens)
        channel_id = random.choice(channels_ids)
        session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
        session.get('https://discord.com')
        cookies = session.cookies.get_dict()
        session.cookies.update(cookies)
        headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
        payload = {'content': f'{message}'}
        rr = session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
        if rr.status_code == 200:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[SPAMMING]{color_reset}")
        else:  # inserted
            if rr.status_code == 429 and 'retry_after' in rr.text:
                timeout = rr.json().get('retry_after', {})
                time.sleep(timeout)

class Utils:
    def rangeCorrector(ranges):
        if [0, 99] not in ranges:
            ranges.insert(0, [0, 99])
        return ranges

    def getRanges(index, multiplier, memberCount):
        initialNum = int(index * multiplier)
        rangesList = [[initialNum, initialNum + 99]]
        if memberCount > initialNum + 99:
            rangesList.append([initialNum + 100, initialNum + 199])
        return Utils.rangeCorrector(rangesList)

    def parseGuildMemberListUpdate(response):
        memberdata = {'online_count': response['d']['online_count'], 'member_count': response['d']['member_count'], 'id': response['d']['id'], 'guild_id': response['d']['guild_id'], 'hoisted_roles': response['d']['groups'], 'types': [], 'locations': [], 'updates': []}
        for chunk in response['d']['ops']:
            memberdata['types'].append(chunk['op'])
            if chunk['op'] in ['SYNC', 'INVALIDATE']:
                memberdata['locations'].append(chunk['range'])
                if chunk['op'] == 'SYNC':
                    memberdata['updates'].append(chunk['items'])
                else:  # inserted
                    memberdata['updates'].append([])
            else:  # inserted
                if chunk['op'] in ['INSERT', 'UPDATE', 'DELETE']:
                    memberdata['locations'].append(chunk['index'])
                    if chunk['op'] == 'DELETE':
                        memberdata['updates'].append([])
                    else:  # inserted
                        memberdata['updates'].append(chunk['item'])
        return memberdata

class DiscordSocket(websocket.WebSocketApp):
    def __init__(self, token, guild_id, channel_id):
        self.token = token
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.blacklisted_roles, self.blacklisted_users = ([], [])
        self.socket_headers = {'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Pragma': 'no-cache', 'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
        super().__init__('wss://gateway.discord.gg/?encoding=json&v=9', header=self.socket_headers, on_open=lambda ws: self.sock_open(ws), on_message=lambda ws, msg: self.sock_message(ws, msg), on_close=lambda ws, close_code, close_msg: self.sock_close(ws, close_code, close_msg))
        self.endScraping = False
        self.guilds = {}
        self.members = {}
        self.ranges = [[0, 0]]
        self.lastRange = 0
        self.packets_recv = 0

    def run(self):
        self.run_forever()
        return self.members

    def scrapeUsers(self):
        if self.endScraping == False:
            self.send('{\"op\":14,\"d\":{\"guild_id\":\"' + self.guild_id + '\",\"typing\":true,\"activities\":true,\"threads\":true,\"channels\":{\"' + self.channel_id + '\":' + json.dumps(self.ranges) + '}}}')

    def sock_open(self, ws):
        self.send('{\"op\":2,\"d\":{\"token\":\"' + self.token + '\",\"capabilities\":125,\"properties\":{\"os\":\"Windows\",\"browser\":\"Firefox\",\"device\":\"\",\"system_locale\":\"it-IT\",\"browser_user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0\",\"browser_version\":\"94.0\",\"os_version\":\"10\",\"referrer\":\"\",\"referring_domain\":\"\",\"referrer_current\":\"\",\"referring_domain_current\":\"\",\"release_channel\":\"stable\",\"client_build_number\":103981,\"client_event_source\":null},\"presence\":{\"status\":\"online\",\"since\":0,\"activities\":[],\"afk\":false},\"compress\":false,\"client_state\":{\"guild_hashes\":{},\"highest_last_message_id\":\"0\",\"read_state_version\":0,\"user_guild_settings_version\":-1,\"user_settings_version\":-1}}}')

    def heartbeatThread(self, interval):
        try:
            while True:  # inserted
                self.send('{\"op\":1,\"d\":' + str(self.packets_recv) + '}')
                time.sleep(interval)
        except Exception as e:
            return

    def sock_message(self, ws, message):
        decoded = json.loads(message)
        if decoded is None:
            return
        if decoded['op']!= 11:
            self.packets_recv += 1
        if decoded['op'] == 10:
            threading.Thread(target=self.heartbeatThread, args=(decoded['d']['heartbeat_interval'] / 1000,), daemon=True).start()
        if decoded['t'] == 'READY':
            for guild in decoded['d']['guilds']:
                self.guilds[guild['id']] = {'member_count': guild['member_count']}
        if decoded['t'] == 'READY_SUPPLEMENTAL':
            self.ranges = Utils.getRanges(0, 100, self.guilds[self.guild_id]['member_count'])
            self.scrapeUsers()
        else:  # inserted
            if decoded['t'] == 'GUILD_MEMBER_LIST_UPDATE':
                parsed = Utils.parseGuildMemberListUpdate(decoded)
                if parsed['guild_id'] == self.guild_id and ('SYNC' in parsed['types'] or 'UPDATE' in parsed['types']):
                    for elem, index in enumerate(parsed['types']):
                        if index == 'SYNC':
                            if len(parsed['updates'][elem]) == 0:
                                self.endScraping = True
                                break
                            for item in parsed['updates'][elem]:
                                if 'member' in item:
                                    mem = item['member']
                                    obj = {'tag': mem['user']['username'] + '#' + mem['user']['discriminator'], 'id': mem['user']['id']}
                                    if not mem['user'].get('bot'):
                                        self.members[mem['user']['id']] = obj
                        else:  # inserted
                            if index == 'UPDATE':
                                for item in parsed['updates'][elem]:
                                    if 'member' in item:
                                        mem = item['member']
                                        obj = {'tag': mem['user']['username'] + '#' + mem['user']['discriminator'], 'id': mem['user']['id']}
                                        if not mem['user'].get('bot'):
                                            self.members[mem['user']['id']] = obj
                        self.lastRange += 1
                        self.ranges = Utils.getRanges(self.lastRange, 100, self.guilds[self.guild_id]['member_count'])
                        time.sleep(0.45)
                        self.scrapeUsers()
                if self.endScraping:
                    self.close()

    def sock_close(self, ws, close_code, close_msg):
        return

def scrape(token, guild_id, channel_id):
    try:
        sb = DiscordSocket(token, guild_id, channel_id)
        return sb.run()
    except:
        print('saddsa')

def scraper(guildid, channelid):
    with open('data/scraper.txt', 'w+') as f:
        f.truncate(0)
    token = ''
    tokensinguild = []
    token = random.choice(all_tokens())

    def checktokens(token):
        proxy = check_setup()
        session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
        session.get('https://discord.com')
        cookies = session.cookies.get_dict()
        session.cookies.update(cookies)
        headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
        rr = session.get(f'https://discord.com/api/v9/guilds/{guildid}', headers=headers, proxy=proxy)
        if rr.status_code == 200:
            tokensinguild.append(token)
    threads = []
    for token in all_tokens():
        t = threading.Thread(target=checktokens, args=(f'{token}',))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    try:
        token = random.choice(tokensinguild)
    except:
        input(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[NO VALID TOKENS IN GUILD]{color_reset}")
    members = scrape(token, f'{guildid}', f'{channelid}')
    for member in members:
        open('data/scraper.txt', 'a+').write(str(member) + '\n')

def spam_messages_with_ping(channels_ids, message, pings_amount, ghostping):
    while True:  # inserted
        session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
        session.get('https://discord.com')
        cookies = session.cookies.get_dict()
        session.cookies.update(cookies)
        tokens = all_tokens()
        token = random.choice(tokens)
        headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
        with open('./data/scraper.txt', 'r') as file:
            ids = file.readlines()
            random_ids = [random.choice(ids).strip() for _ in range(pings_amount)]
        payload = {'content': f"{message} {' '.join([f'<@{random_id}>' for random_id in random_ids])}"}
        channel_id = random.choice(channels_ids)
        rr = session.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
        if rr.status_code == 200:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[SPAMMING]{color_reset}")
        else:  # inserted
            if rr.status_code == 429 and 'retry_after' in rr.text:
                timeout = rr.json().get('retry_after', {})
                time.sleep(timeout)
        if ghostping == True:
            while True:  # inserted
                session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
                session.get('https://discord.com')
                cookies = session.cookies.get_dict()
                session.cookies.update(cookies)
                headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
                try:
                    data = rr.json()
                    message_id = data['id']
                    rr = session.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
                    if rr.status_code == 204:
                        continue
                    if rr.status_code == 429 and 'retry_after' in rr.text:
                        timeout = rr.json().get('retry_after', {})
                        time.sleep(timeout)
                    else:  # inserted
                        continue
                except Exception:
                    continue

def token_formatter():
    try:
        with open('./data/formatter.txt', 'r') as file:
            lines = file.readlines()
        cleaned_values = [line.split(':')[(-1)].strip() for line in lines if ':' in line]
        if not cleaned_values:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>>{color_reset} Can\'t find tokens to format!")
            return
        with open('./data/tokens.txt', 'a') as file:
            file.write('\n' + '\n'.join(cleaned_values) + '\n')
        with open('./data/formatter.txt', 'w') as file:
            remaining_lines = [line for line in lines if line.strip() and ':' not in line]
            file.write(''.join(remaining_lines))
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>>{color_reset} Successfully formated tokens!")
    except Exception as e:
        print(f'{e}')

def token_onliner(token):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    rr = session.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers, proxy=proxy)
    if rr.status_code in [200, 204]:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[ONLINE]{color_reset}")
    else:  # inserted
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[OFFLINE]{color_reset}")
    randomstatus = ['online']
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
    response = ws.recv()
    event = json.loads(response)
    auth = {'op': 2, 'd': {'token': token, 'capabilities': 61, 'properties': 'Windows', 'presence': {'os': 'Chrome', 'browser': '', 'device': 'en-GB', 'system_locale': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'browser_user_agent': '90.0.4430.212', 'browser_version': '10', 'os_version': '', 'referrer': '', 'referring_domain': '', 'referrer_current': '', 'referring_domain_current': '', 'release_channel': 'stable', 'client_build_number': '85108', 'client_event_source': 'null'}, 'compress': {'status': random.choice(randomstatus), 'since': 0, 'activities': [], 'afk': False}, 'client_state': {'guild_hashes': False, 'highest_last_message_id': '0', 'read_state_version': 0}}}
    ws.send(json.dumps(auth))

def bio_changer(token, bio):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    payload = {'bio': bio}
    rr = session.patch('https://discord.com/api/v9/users/%40me/profile', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 200:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CHANGED BIO]{color_reset}")
    elif rr.status_code == 400:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_yellow}[CAPTCHA]{color_reset}")
    else:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[FAILED]{color_reset}")

def thread_spammer(token, channel_id):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    payload = {'auto_archive_duration': 4320, 'type': 11, 'name': str(uuid.uuid4()), 'localization': 'message'}
    for i in range(4):
        rr = session.post(f'https://discord.com/api/v9/channels/{channel_id}/threads', headers=headers, json=payload, proxy=proxy)
        if rr.status_code == 201:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CREATED]{color_reset}")
        else:  # inserted
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[FAILED]{color_reset}")

def friend_spammer(token, username):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    payload = {'username': username, 'discriminator': None}
    rr = session.post('https://discord.com/api/v9/users/@me/relationships', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 204:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[SENT]{color_reset}")
    else:  # inserted
        if rr.status_code == 400:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_yellow}[CAPTCHA]{color_reset}")
        else:  # inserted
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
            logging.basicConfig(filename='./data/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(f'=> Voice joiner => {rr.status_code} => {rr.text}')

def voice_spammer(token, guild_id, channel_id):
    while True:  # inserted
        ws = websocket.WebSocket()
        ws.connect('wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream')
        ws.send(json.dumps({'op': 2, 'd': {'token': token, 'capabilities': 30717, 'properties': {'os': 'Windows', 'browser': 'Chrome', 'device': '', 'system_locale': 'pl-PL', 'browser_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'browser_version': '126.0.0.0', 'os_version': '10', 'referrer': 'https://www.google.com/', 'referring_domain': 'www.google.com', 'search_engine': 'google', 'referrer_current': '', 'referring_domain_current': '', 'release_channel': 'stable', 'client_build_number': 303105, 'client_event_source': None, 'design_id': 0}, 'presence': {'status': 'unknown', 'since': 0, 'activities': [], 'afk': False}, 'compress': False, 'client_state': {'guild_versions': {}}}}))
        join = {'op': 4, 'd': {'guild_id': guild_id, 'channel_id': channel_id, 'self_mute': False, 'self_deaf': False, 'self_video': True, 'flags': 2}}
        ws.send(json.dumps(join))
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CONNECTED]{color_reset}")
        time.sleep(random.randint(1, 5))
        ws.close()
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[DISCONNECTED]{color_reset}")

def sound_spammer(token, guild_id, channel_id):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream')
    ws.send(json.dumps({'op': 2, 'd': {'token': token, 'capabilities': 30717, 'properties': {'os': 'Windows', 'browser': 'Chrome', 'device': '', 'system_locale': 'pl-PL', 'browser_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'browser_version': '126.0.0.0', 'os_version': '10', 'referrer': 'https://www.google.com/', 'referring_domain': 'www.google.com', 'search_engine': 'google', 'referrer_current': '', 'referring_domain_current': '', 'release_channel': 'stable', 'client_build_number': 303105, 'client_event_source': None, 'design_id': 0}, 'presence': {'status': 'unknown', 'since': 0, 'activities': [], 'afk': False}, 'compress': False, 'client_state': {'guild_versions': {}}}}))
    join = {'op': 4, 'd': {'guild_id': guild_id, 'channel_id': channel_id, 'self_mute': False, 'self_deaf': False, 'self_video': True, 'flags': 2}}
    ws.send(json.dumps(join))
    print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CONNECTED]{color_reset}")
    while True:  # inserted
        proxy = check_setup()
        session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
        session.get('https://discord.com')
        cookies = session.cookies.get_dict()
        session.cookies.update(cookies)
        headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
        time.sleep(0.7)
        sound_number = random.randint(1, 5)
        payload = {'sound_id': sound_number, 'emoji_id': None, 'emoji_name': '🔊'}
        rr = session.post(f'https://discord.com/api/v9/channels/{channel_id}/send-soundboard-sound', headers=headers, json=payload, proxy=proxy)
        if rr.status_code == 204:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[PLAYING KIT {sound_number}]{color_reset}")
        else:  # inserted
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[FAILED]{color_reset}")

def onboarding_bypass(token, guild_id):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    try:
        rr = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/onboarding', headers=headers, proxy=proxy)
        data = rr.json()
        onboarding_responses = []
        onboarding_prompts_seen = {}
        onboarding_responses_seen = {}
        time_now = time.time()
        time_now_ms = int(time_now * 1000)
        prompts = data['prompts']
        for prompt in prompts:
            if prompt.get('required') == True:
                onboarding_prompts_seen[prompt['id']] = time_now_ms
        for prompt in prompts:
            if prompt.get('required') == True:
                for option in prompt.get('options', []):
                    onboarding_responses_seen[option['id']] = time_now_ms
        for prompt in prompts:
            if prompt.get('required') == True:
                options = prompt.get('options', [])
                if options:
                    selected_option = random.choice(options)
                    onboarding_responses.append(selected_option['id'])
        payload = {'onboarding_responses': onboarding_responses, 'onboarding_prompts_seen': onboarding_prompts_seen, 'onboarding_responses_seen': onboarding_responses_seen}
        rr = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/onboarding-responses', headers=headers, proxy=proxy, json=payload)
        if rr.status_code == 200:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[ONBOARDING BYPASSED]{color_reset}")
        else:  # inserted
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
            logging.basicConfig(filename='./data/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            logging.error(f'=> Onboard Bypass => {rr.status_code} => {rr.text}')
    except:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[CHECK LOGS]{color_reset}")
        logging.basicConfig(filename='./data/access.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.error(f'=> Onboard Bypass => {rr.status_code} => {rr.text}')

def call_spammer(token, user_id):
    proxy = check_setup()
    session = tls_client.Session(client_identifier='chrome_120', random_tls_extension_order=True)
    session.get('https://discord.com')
    cookies = session.cookies.get_dict()
    session.cookies.update(cookies)
    headers = {'accept': '*/*', 'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7', 'authorization': token, 'content-type': 'application/json', 'origin': 'https://discord.com', 'priority': 'u=1, i', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'x-debug-options': 'bugReporterEnabled', 'x-discord-locale': 'pl', 'x-discord-timezone': 'Europe/Warsaw', 'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNjIwOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=='}
    payload = {'recipients': [user_id]}
    rr = session.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json=payload, proxy=proxy)
    if rr.status_code == 200:
        data = rr.json()
        try:
            channel_id = data['id']
        except:
            print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[FAILED]{color_reset}")
    else:  # inserted
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_red}[FAILED]{color_reset}")
    while True:  # inserted
        ws = WebSocket()
        ws.connect('wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream')
        ws.send(json.dumps({'op': 2, 'd': {'token': token, 'capabilities': 30717, 'properties': {'os': 'Windows', 'browser': 'Chrome', 'device': '', 'system_locale': 'pl-PL', 'browser_user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36', 'browser_version': '126.0.0.0', 'os_version': '10', 'referrer': 'https://www.google.com/', 'referring_domain': 'www.google.com', 'search_engine': 'google', 'referrer_current': '', 'referring_domain_current': '', 'release_channel': 'stable', 'client_build_number': 303390, 'client_event_source': None, 'design_id': 0}, 'presence': {'status': 'unknown', 'since': 0, 'activities': [], 'afk': False}, 'compress': False, 'client_state': {'guild_versions': {}}}}))
        call = {'op': 4, 'd': {'guild_id': None, 'channel_id': channel_id, 'self_mute': True, 'self_deaf': False, 'self_video': False, 'flags': 2}}
        ws.send(json.dumps(call))
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} {token[:(-15)]} {color_green}[CALLED]{color_reset}")
        time.sleep(1)
        leave = {'op': 4, 'd': {'guild_id': None, 'channel_id': None, 'self_mute': True, 'self_deaf': False, 'self_video': False, 'flags': 2}}
        ws.send(json.dumps(leave))
        time.sleep(1)
while True:  # inserted
    initialize_ui()
    license = check_license()
    if license == None:
        print(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} Witaj w HatacheTOOL, {color_pink}zaloguj się!{color_reset}")
        user_key = input(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}AUTH{color_reset}] {color_yellow}>> {color_reset} ")
        rr = requests.post('https://hatache-tool-api.vercel.app/api/login', json={'license': user_key})
        if rr.status_code == 200:
            data = rr.json()
        if data['valid'] == True:
            logged = True
        else:  # inserted
            logged = False
    else:  # inserted
        rr = requests.post('https://hatache-tool-api.vercel.app/api/login', json={'license': license})
        if rr.status_code == 200:
            data = rr.json()
            if data['valid'] == True:
                logged = True
            else:  # inserted
                logged = False
        else:  # inserted
            input(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} Nie udało się wysłać zapytania do {color_red}API!{color_reset}")
            sys.exit()
        initialize_ui()
        input(f"{color_magenta}{datetime.now().strftime('%H:%M:%S')}{color_reset} [{color_pink}INFO{color_reset}] {color_yellow}>> {color_reset} Wpisano niepoprawny kod, {color_pink}spróbuj ponownie!{color_reset}")