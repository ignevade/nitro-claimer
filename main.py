import discord
import re
import requests
TOKEN = ''
regex = re.compile(r'discord(?:\.gift|\.com\/gifts)\/([a-zA-Z0-9]{22,24})')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        gift_codes = regex.findall(message.content)
        for code in gift_codes:
            print(f'Found gift code: {code}')
            await self.redeem_gift(code)

    async def redeem_gift(self, code):
        print(f'Found gift code! attempting to redeem...')
        url = f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem'
        headers = {
            'Authorization': TOKEN,
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f'Successfully redeemed gift code! Enjoy your nitro <3 ({code})')
        else:
            print(f'Failed to redeem gift code. ({response.status_code})')
client = MyClient()
client.run(TOKEN)