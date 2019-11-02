#working on. Last: Nov. 10 2019 w/ wait_for_event [in_action] & SoulGEM @ infinite.py
# yes

import command as comando, infinite

class Event:
	def __init__(self, bot):
		self.bot = bot #esto pareciera que esta demás. Pero no lo está...
		self.command = comando.Command()
		self.dimension = infinite.Dimension(bot, )



	def wait_for_event(self):
		events = self.bot.slack_client.rtm_read() # ..aquí podemos verlo.

		if self.dimension.in_action == True:
			in_action = True
		else:
			in_action = False
		

		if events and len(events) > 0:
			for event in events:
				# "prints" the event
				self.parse_event(event, in_action)





















	def parse_event(self, event, action):

		if event and 'text' in event and self.bot.bot_id in event['text']:
			self.handle_mention(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])

		if event and ('text' or 'reaction') in event: #..and
			self.wait_for_event()
	
	def handle_mention(self, user, command, channel):
		if command and channel:
			print("Received command: " + command + " in channel: " + channel + " from user: " + user)
			response = self.command.handle_command(user, command)
			self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

