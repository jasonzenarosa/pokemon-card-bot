# About
This Python script uses HTTPX and Parsel to scrape the price of Prismatic Evolution Elite Trainer Box from the Walmart website once per minute. If the price is less than $100, it sends a Discord message containing the link to the Walmart listing and the current price. 

# Instructions for Running
To run the script, you'll need [Python](https://www.python.org/downloads/) (the script was written on 3.13 but it should work with other versions), as well as the following modules: requests, httpx, parsel. You can use [pip](https://pip.pypa.io/en/stable/installation/) to install these modules.

```
// on windows
pip install requests
pip install httpx
pip install parsel

// on mac
pip3 install requests
pip3 install httpx
pip3 install parsel
```

You'll also need a [Discord Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) link in order for the script to publish Discord messages to a server. Once you have your link, duplicate the `context.example.py` file and rename the duplicated file `context.py`. Then, paste your link into the file in the appropriate section.

Finally, run the script.

```
// on windows
python main.py

// on mac
python3 main.py
```
