# working on it. Last: Nov.01 2019 w/ SpaceGEM (still with SoulGEM)
import bot
class Dimension:
    ''' Where is the brainstorm will take place! La siembra, propiamente.'''
    def __init__(self, bot):
        self.bot = bot

        self.channel_id = False
        # self.channel_name = name_place # disable, it is not necessary.

        self.host_user = {}  # a person. Its i.d., actually
        self.participants = {} # a set

        self.in_action = False

        # self.date =13
        self.phases = []
        '''     done/processing/doing/not yet there.
        This next it's just a reference of it's meaning. Up to 5!
            ["0" : "semillas",
             "1" : "primera siembra",
             "2" : "segunda siembra",
             "3" : "votacion",
             "4" : "printing"]
        '''


class Gauntlet:
    def __init__(self):

        self.here = Dimension(bot)
        self.lies = self.here.bot.places_to_handle
        global place, there
        there = self.here #
        place = self.lies # list from bot.Bot()
        self.stones= {
            "Space" : "space", # places and harvesting. Also locations!
            "Time"  : "time", # Schedule thing! And timing stuff.
            "Soul"  : "soul", # it should be the participants thing.
            "Reality" : "real", # I -just- don't know.
            "Power" : "he do power", #admin and user doings inside.
            "Mind"  : "he says" # talkative things, you know.
        }

    class SpaceGEM:

        def add_place(self, id_c, c_name):
            try:
                there.bot.places_to_handle = place + {id_c : c_name}
            except KeyError:
                print("There's a channel already registered,\n" +\
                      "\t maybe just Thanos is Harvesting on there.")
                pass
            finally:
                print("Channels registered: ")
                for i in place:
                    print(i +"\n")
                    # imprime cada una de los lugares que tiene allí.
            return None

        def place_coordinates(self, event):
            # still working on it.
            nro_planet = event["channel"]
            Gauntlet().here.bot.slack_client.api_call()
            name_planet = nro_planet["name"]
            # It seems to be together with SoulGEM enhance_soulMate
            # putting on it the same variable as this one (event)


        def confirming_location(self):
            if there.channel_id in bot.Bot().places_to_handle:
                # might ups out a False or an error, because the way of calling it.
                return True
            else:
                return False


    class SoulGEM:

        def enhance_soulMate(self, event):
            person = event["user"]
            global alias
            api_call = there.bot.api_call("users.list")
            users = api_call.get('members')
            for user in users:
                if 'id' in user == person:
                    alias = user.get('name')

            self.hosting_user(person, alias)
            return None

        def hosting_user(self, id_person, its_name):
            try:
                # Dimension(bot) is there
                there.host_user += {id_person : its_name}
                # this adds our host to the respective Dimension!
            except KeyError:
                print("The harvesting is already hosted by " +
                      there.host_user[id_person] +
                      ",\n with the alias: " + its_name)
                pass
            finally:
                return None













































    def say_channel(self)
        print("Channel id: " + self.channel_id + " & name: " + self.channel_name)
            # p1 = Person("John", 36)
            # p1.say_channel()  ... self es la clase, p1. And say_channel() a function on that class with same self)


    def get_channel_id(self, place):
        """place must be event["channel"]"""
        take = place  # event["channel"]
        api_call = self.bot.slack_client.api_call("channels.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            channels = api_call.get('channels')
            for channel in channels:
                if take in channels and channel.get('name') == message["channel"]:
                    print(channel.get('id') + " is named: " + channel.get('name'))

                    return channel.get('id'), channel.get('name')

            return None

    def parse_event(self, event, gauntlet = False):

        if event and 'text' in event and self.bot.bot_id in event['text']:
            self.handle_event(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(),
                              event['channel'])
    '''
        if self.bot.Bot.columns.get(event['channel']) == True and gauntlet:
            # busca a ver si la siembra está encendida en dicho canal!
            return
    '''



    def hagalo(self, n, palabra, lista):
        tomato = "harvesting" + n  # harvesting1, harvesting2
        tomato["need" + n] = lista.append(palabra)

    def realityGem(self):
        # "prepara los mundos" (en el que será anfitrion)

        canal_id = self.get_channel("id")
        canal_name = self.get_channel("name")
        summoner =

        Dimension(canal_id, canal_name, summoner, participantes, self)

        Dimension.channel_name = self.get_channel("name")

        Dimension.in_action = True


planeta = Dimension("Thanos", "id_thanos","nombre")
