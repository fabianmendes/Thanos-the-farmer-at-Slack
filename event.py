import command as comando, infinite
import bot as titan

class Event:
	def __init__(self, bot):
		self.bot = bot #esto pareciera que esta demás. Pero no lo está...
		self.command = comando.Command()
		self.dimension = infinite.Dimension(bot)



	def wait_for_event(self):
		events = self.bot.slack_client.rtm_read() # ..aquí podemos verlo.

		if events and len(events) > 0:
			for event in events:
				# "prints" the event
				self.parse_event(event)


	def parse_event(self, event):

		#verifications, if event["channel"] in diccionario de bot.Bot().places_to_handle and its value is True:
		# if False:  escuchar el text y to-do eso (que ya está escrito).
		# comment else: .
		gem = titan.Bot().places_to_handle
		#  verify listing places   "  ".
		types = ["message", ]
		if event and  in event and
		if event["channel"] in gem and gem[event["channel"]]:
			# now verifies phase,
			Tata = True # each phase.
			if self.dimension.phases == Tata:

				# TODO aca uno de los methods para que registry!
				#
				return








		if event and 'text' in event and self.bot.bot_id in event['text']:
			self.handle_mention(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])

		if event and ('text' or 'reaction') in event: #..and
			self.wait_for_event()
	
	def handle_mention(self, user, command, channel):
		if command and channel:
			print("Received command: " + command + " in channel: " + channel + " from user: " + user)
			response = self.command.handle_command(user, command)
			self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

