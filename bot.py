from pyrogram import Client, filters

# فقط توکن ربات لازم است
app = Client(
    "my_bot",
    bot_token="8054005328:AAGMU8MvwmPTKoOCeoK_ERZMiGeAJ2M6mnk"
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("سلام! ربات بدون VPN فعاله 😎")

app.run()
