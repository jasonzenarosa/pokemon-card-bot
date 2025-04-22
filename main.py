import httpx, requests
from parsel import Selector
from time import sleep
from context import WEBHOOK_LINK

BASE_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US,en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
}

def scrape():
    with httpx.Client(http2=True, headers=BASE_HEADERS) as client:
        response = client.get("https://www.walmart.com/search?q=prismatic+evolution")

    sel = Selector(text=response.text)
    found = False

    # Find all <a> that contain a <span> with a title
    for link in sel.xpath('//a[span]'):
        href = link.xpath('./@href').get()
        href = "https://www.walmart.com" + href
        title = link.xpath('.//span//text()').getall()
        title = ' '.join(title).strip()

        if title == "Pokemon Scarlet & Violet - Prismatic Evolutions Elite Trainer Box":
            found = True
            # Go up to the outer div (role="group") then search *inside it* for the price
            group_div = link.xpath('ancestor::div[@role="group"][1]')
            price_str_list = group_div.xpath('.//div[@data-automation-id="product-price"]//text()').getall()
            price = -1
            for price_str in price_str_list:
                if price_str.startswith("current price"):
                    try:
                        price = float(price_str.split("$")[1])
                    except Exception:
                        pass

            print(f"Price: {price}")

            if price > -1 and price < 100:
                send_message(title, href, price)

    if not found:
        print("ALERT: ITEM NOT FOUND")

def send_message(title, link, price):
    data = {"content": f'PRICE LESS THAN 100\n{title}\n{link}\n${price}'}
    requests.post(WEBHOOK_LINK, json=data)

if __name__ == "__main__":
    while True:
        scrape()
        sleep(60)
