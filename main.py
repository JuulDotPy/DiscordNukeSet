import threading, random
import requests
import time, colorama
from colorama import Fore


print("")
print("▒█░▄▀ ░▀░ █░░ █░░ █▀▀ █▀▀█")
print("▒█▀▄░ ▀█▀ █░░ █░░ █▀▀ █▄▄▀")
print("▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀")


print("[1] = spam a message in a channel")
print("[2] = dming every user which is in DM")
print("[3] = spamming a webhook")
what = input(f"\n")

if what == "1":
    token = input("token: ")
    channel = input('Id of channel: ')
    mess = input('Message to spam: ')
    delay = float(input('Delay: '))





    def spam(token, channel, mess):
        url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
        data = {"content": mess}
        header = {"authorization": token}
        y = 0
        x = 0
        while True:
            time.sleep(delay)
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
                x = x + 1
                y = y + 1 
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} MESSAGE SENT     {x} out of {y} were sent")
            else:
                y = y + 1 
                print(f"{Fore.LIGHTRED_EX}[+] {Fore.RESET} MESSAGE FAILED   {x} out of {y} were sent")
                

    def thread():
        channel_id = channel
        text = mess
    
        time.sleep(int(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()



    start = thread()


elif what == "2":
    token = input("token: ")
    rs = requests.Session()


    def randstr(lenn):
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        text = ''
        for i in range(0, lenn):
            text += alpha[random.randint(0, len(alpha) - 1)]
        return text


    def mass_dm():
        colorama.init()
        message = input('Message: ')
        headers = {"authorization": token, "user-agent": "Mozilla/5.0"}

        reqmas = rs.get(
            "https://discord.com/api/v9/users/@me/channels", headers=headers
        ).json()
        for chen in reqmas:
            json = {"content": message}
            time.sleep(1)
            rs.post(
                f"https://discord.com/api/v9/channels/{chen['id']}/messages",
                headers=headers,
                data=json,
            )
            print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} {chen['id']} Sent")


    mass_dm()

elif what == "3":
    from discord_webhooks import DiscordWebhooks

    webhook_url = input('Enter WEBHOOK URL: ')

    message = input('Enter Message: ')
    delay = float(input('Delay: '))

    webhook = DiscordWebhooks(webhook_url, rate_limit_retry=True)

    webhook.set_content(title=message,
                        description=message,
                        color=0xF58CBA)



    while True:
        time.sleep(delay)
        webhook.send()
        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} WEBHOOK Sent")

else:
    print("NOT FOUND")
    time.sleep(5)
