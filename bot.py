# working on. Last: Nov.01 2019 w/ SoulGEM @ infinite.py
import time, event as evento, os
from slackclient import SlackClient


class Bot(object):
    def __init__(self):
        self.slack_token = os.environ.get("Bot_User_OAuth_Access_Token")
        self.slack_client = SlackClient(self.slack_token)
        self.bot_name = os.environ.get("BOT_NAME")  # thanos__the_farmer.
        self.bot_id = self.get_bot_id()

        if self.bot_id is None:
            exit("Error, could not find " + self.bot_name)

        self.event = evento.Event(self)
        self.places_to_handle = { } # id as keys and value as name.
        self.listen()

    def get_bot_id(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self.bot_name:
                    return "<@" + user.get('id') + ">"

            return None

    #
    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            print("Successfully connected, already listening")
            while True:
                self.event.wait_for_event()
                # lo llama, y lo hace. (lugar, punto, clase; punto metodo)
                # ¡y se queda en este bucle forever! Bucle clave.

                time.sleep(1)
        else:
            exit("Error, Connection Failed")

