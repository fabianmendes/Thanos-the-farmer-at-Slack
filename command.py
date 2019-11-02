#not managed!
# TODO considerate the updagrades from infinite.py!
# TODO ...and event.py of course

import infinite, event, bot
class Command(object):
	def __init__(self, location = False):
		self.commands = { 
			"help" : self.help,
			"start" : self.harvesting(location)
		}

	def handle_command(self, user, command, location = False):
		response = "<@" + user + ">: "
	
		if command in self.commands:
			response += self.commands[command](location)  # para responder (tratandose de un Hola, o un help)
		else:
			response += "Sorry I don't understand the command: " + command + ". " + self.help()
		
		return response
	
	def hi(self):
		response = "Hi there!"
		return response
	
	def help(self):
		response = "Currently I support the following commands:\r\n"
		
		for command in self.commands:
			response += command + "\r\n"
			
		return response
	def harvesting(self, ON):
		response = "Ok, please tell me the seeds. Just two or three key words ONLY"
		turn = infinite.Dimension( bot.Bot().bot_id)


		return response
