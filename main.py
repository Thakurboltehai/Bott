import random
import requests
import time

class RDXBinScraper:
    def __init__(self, bot_token, chat_id):
        self.bot_token = "7690743721:AAHXcW0CWPsKoVzsrXyA0c5NprnnYkQ5KA4"
        self.chat_id = "-1002614715708"
        self.bin_prefixes = {
            'VISA': ['4'],
            'MASTERCARD': ['51', '52', '53', '54', '55'],
            'AMEX': ['34', '37'],
            'DISCOVER': ['6011', '65'],
            'MAESTRO': ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']
        }
        self.countries = {
            'US': {'flag': '🇺🇸', 'banks': ['Chase', 'Bank of America', 'Wells Fargo', 'Citibank']},
            'UK': {'flag': '🇬🇧', 'banks': ['Barclays', 'HSBC UK', 'Lloyds Bank', 'NatWest']},
            'CA': {'flag': '🇨🇦', 'banks': ['RBC', 'TD Canada Trust', 'Scotiabank', 'BMO']},
            'AU': {'flag': '🇦🇺', 'banks': ['Commonwealth Bank', 'ANZ', 'NAB', 'Westpac']}
        }
        self.card_levels = ['CLASSIC', 'GOLD', 'PLATINUM', 'SIGNATURE', 'WORLD']
        self.card_types = ['PREPAID', 'CHARGE', 'DEBIT', 'CREDIT', 'VIRTUAL']

    def generate_bin(self):
        card_brand = random.choice(list(self.bin_prefixes.keys()))
        prefix = random.choice(self.bin_prefixes[card_brand])
        bin_number = prefix + ''.join([str(random.randint(0, 9)) for _ in range(6 - len(prefix))])
        
        country = random.choice(list(self.countries.keys()))
        bank = random.choice(self.countries[country]['banks'])
        card_type = random.choice(self.card_types)
        
        return {
            'bin': bin_number,
            'brand': card_brand,
            'type': card_type,
            'country': country,
            'flag': self.countries[country]['flag'],
            'bank': bank,
            'level': random.choice(self.card_levels)
        }

    def send_to_telegram(self, message):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        params = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }
        try:
            requests.post(url, params=params)
            return True
        except:
            return False

    def format_bin(self, bin_info):
        return (
            f"𝗕𝗜𝗡 𝗦𝗖𝗥𝗔𝗣𝗣𝗘𝗥\n\n"
            f"⚙ 𝗕𝗜𝗡 ⇾ {bin_info['bin']}\n"
            f"🏛️ 𝗕𝗿𝗮𝗻𝗱 ⇾ {bin_info['brand']}\n"
            f"♻️ 𝗧𝘆𝗽𝗲 ⇾ {bin_info['type']}\n"
            f"💳 𝗟𝗲𝗩𝗲𝗟 ⇾ {bin_info['level']}\n"
            f"💵 𝗕𝗮𝗻𝗸 ⇾ {bin_info['bank']}\n"
            f"🌎 𝗖𝗼𝗨𝗻𝘁𝗿𝘆 ⇾ {bin_info['country']} {bin_info['flag']}\n\n"
            f"𝗗𝗘𝗩 ⇾ @RDXxxCARDER"
        )

    def start_scraping(self, interval=5, drop_size=1):
        print("🚀 RDX BIN Scraper Activated")
        print("👑 BOT OWNER: @RDXxxCARDER")
        try:
            while True:
                for _ in range(drop_size):
                    bin_info = self.generate_bin()
                    formatted = self.format_bin(bin_info)
                    if self.send_to_telegram(formatted):
                        print(f"✅ Sent: {bin_info['bin']} | Type: {bin_info['type']}")
                    else:
                        print("❌ Failed to send")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n🛑 Scraping stopped")

TELEGRAM_BOT_TOKEN = "7656779369:AAG_SXh8nBmqvq1CYWES3UC0xbRJlCM1mvI"
TELEGRAM_CHAT_ID = "-1002614715708"

if __name__ == "__main__":
    bot = RDXBinScraper(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
    bot.start_scraping(interval=5, drop_size=1)
