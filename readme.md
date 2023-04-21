## A simple telegram bot with openAI integration. Made with python and Flask(Quart).

This application was created along with an article: https://medium.com/hyperskill/telegram-conversation-summarizer-bot-with-chatgpt-and-flask-quart-bb2e19884c
To learn more about developing web applications with Flask, check Hyperskill’s [Flask track](https://hyperskill.org/tracks/29).

### Getting started
* install requirements
```
$ pip install -r requirements.txt
```

* export environment variables
```
$ export TELEGRAM_TOKEN=YouRTeleGRam:toKenSTrinG
$ export OPENAI_TOKEN=yOurOpenAItoKeNStrIng
$ export TELEGRAM_CORE_API_ID=YouRTeleGRamApiID
$ export TELEGRAM_CORE_API_HASH=YouRTeleGRamApiHaSH
```
optional: set application port (as `TELEGRAM_BOT_PORT`)

* run main.py
```
python main.py
```
