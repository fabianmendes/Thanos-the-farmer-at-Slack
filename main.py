from slackclient import SlackClient
from slackeventsapi import SlackEventAdapter
import schedule
import time
import os

BOT_NAME = "thanos"
slack_token = os.environ["SLACK_SIGNING_SECRET"]  # I'll do it w/ secret signing.
sc = SlackClient(slack_token)

sea = SlackEventAdapter(slack_token, endpoint="/slack/events")


#  SLACK_SIGNING_SECRET,

@sea.on("hear")
def handle_message(event_data):
    hear = event_data["event"]
    return hear


hear = handle_message()


def whispper():
    somebody = hear["user"]
    return somebody


def say(something, towho=False):
    global channel
    channel = hear["channel"]
    tosay = something
    return sc.apicall("chat.postMessage",
                      channel=channel,
                      text=tosay,
                      user=towho)


if hear.get("subtype") is None and "hi" in hear.get['text']:
    greetings = "Hello <@%s>! :tada:" % hear["user"]
    say(greetings)

count = 0
hand = True
quantite = 0  # número de necesidades


def need(number):
    needl = "need" + str(number + 1)
    return needl


seeds = {"need1": 0,
         "need2": 0,
         "need3": 0}


class Seed:

    def __init__(self, seed):
        # its 'name', e. g. need1 = Seeds('')
        # The name will be 'need'+ str(number) <- it is need(), formely.'''
        # EXAMPLE:
        # mot = message['text'] <- it's relation w/ hear= handle_message()
        # needl = need()
        # needl.add_mot('mot')
        # then, if we: print(need1.mot) -> ['', '', 'etc']
        self.seed = seed
        self.mots = []

        def add_mot(self, mot):
            self.mots.append(mot)
            self.submots = []

        def add_submot(self, submot):
            self.submots.append(submot)


repetidas = {}  # dictionary


def checking(out):
    # out = word

    tupla = tuple(seeds)  # dict.keys(), by default
    listas = list(seeds.values())  # seeds (needings).
    try:
        listas.remove(0)
    except:
        pass
    finally:
        times = len(listas)

    for n in range(times):
        necesidad = tupla[n]
        if out in necesidad.mots:  # needs
            try:
                if out not in repetidas:
                    repetidas[out] = 0
            finally:
                repetidas[out] = + 1
        for m in range(len(necesidad.mots)):
            if out in necesidad.submots:
                if out not in repetidas:
                    repetidas[out] = 0
            repetidas[out] = + 1


def scythe(mot, cual, donde, chicle, parte):  # 2nd harvest!
    # word, harvest and needl.
    global A, turn

    if cual == 0:
        donde.add_mot(mot)
    else:  # cual = 1. It means 2nd harvest is on.
        chicle = + 1  # añade al contador, que estará dentro del while.
        # cuenta los ciclos, es decir que si es igual al nro de len()..
        donde.add_submot(mot)

        if turn == len(parte):  # se iguala al número de participantes
            if chicle == len(donde.mots):
                A = + 1  # contador para la clase Seeds -> needs.
                donde = need(A)
                chicle = 0
            turn = 0
            this = donde.mots[chicle]
            say(this)
    return


def harvesting():
    global chicle

    if harvesting != 1 and True != (chicle < len(aux)):
        if chicle == len(aux):
            schedule.cancel_job(harvesting)

        else:
            time.sleep(1)
        harvest = 1  # (2nd harvesting)
        chicle = 0

    chicle = + 1  # cycle !
    needl = need(chicle - 1)

    if harvest != 1:
        say(print(seeds[needl]))

    parte = list(participants)
    while True:

        if turn > len(participants):
            turn = 0  # counts this list!
            parte = list(participants)
            # ^ this line rewrites the list.

        if harvest == 1 and chicle == len(needl.mots):
            chicle = 0  # counts this
            needl = need()
            say(print(needl.mot))

        if hear.get("subtype") is None:
            word = hear.get["text"]

            turn = + 1
            if whispper() != parte[turn]:
                try:
                    damn = print(participants.pop(turn)) + " had talked. Let's continue.."
                    if harvest != 1 or whispper() not in parte:
                        turn = - 1  # se retribuye! Se compensa..
                except:
                    damn = "be quite <@%s>" % whispper()
                    pass
                finally:
                    say(damn)

        scythe(word, harvest, needl, chicle, parte)



def uP(): # getting ready!
    userPrepare = ["start", "La siembra", "harvest", "la siembra", "sembrar"]
    for i in range(len(userPrepare) + 1):
        up = userPrepare[i]
        return up # user prepare

global principal
if hear.get("subtype") is None and uP() in hear.get['text']:
    principal = whispper()
    comeon = "Give me/dame the seeds/las semillas, <@%s>" % hear["user"]
    say(comeon)


def soul():
    global users

    if sc.api_call('users.list').get('ok'):
        members = sc.api_call('users.list').get('members')
        for user in members:
            if 'name' in user and user.get('name') == (BOT_NAME or "Thanos"):
                global BOT_ID
                BOT_ID = '<@{}>'.format(user.get('id'))
    users = sc.api_call('users.list')
    return users


participants = { principal, }
'''  # (sets).
 done_TODO HEAR THE MESSAGE AND SAVE THE SEEDS/NEEDS into the dictionary "seeds".'''
if hear.get("subtype") is None and (whispper == principal) and (len(participants) == 1):
    banned = ['', " ", ",", "y", "and", "et"]
    # ^ later we should create a properly file! (AI alike, huh?).

    ''' I've just realized that this next before decoration could be a
    function, in fact this is "the SEEDING", so it'd be actually -def-
    seeding():                    '''
    for y in range(len(banned)):
        global aux
        aux = hear["text"]

        supre = banned[y]
        if supre in aux:
            aux.remove(supre)
    for x in range(len(aux)):
        d = Seed(aux[x])

        seeds[need(x)] = d.seed  # dict[key] = value
    # print(need(x)) -> prints that respective value !
    # need(x).add_mot(WORD) # adds a mot into the [value] Seed class.
    sayP = "Registrado, necesidades: " + print(seeds)
    say(sayP, whispper())

    soul()
    # now, we start to ask people who wants to join the harvesting!
    while True:

        time.sleep(1)
        if hear.get("subtype", whispper) is None and ("listo" or "ready") in hear.get["text"]:
            # I would like to print all participants. And if we are in Slack, Thanos as BOT should show it as an attachment.
            # But well- as simple/easily to do so, first; It's necessary to have in mind the thing about be able in being 'compatible' w/ the next versions after completing the Slack BOT. (I mean, Telegram and whatsapp) But I know, let's get FOCUS!

            break
        if hear.get("subtype") is None and ("yo" or "Yo" or "I" or "i" or ":raising_han:" or "me" or 'moi' or "mi") in hear.get['text']:
            participants.add(whispper())


say("Ok, let's start!")

schedule.every(60).seconds.do(harvesting())
harvesting()


# -----------------. Done, good so far! [27.mar'19 - 01:44PM]

def voting():
    palm = {}  # set 'local'.

    def passing():  # returns False
        return False

    for n in range(len(aux)):  # 'getting gems'? Or energy..
        candide = set(need(n).mot)
        candido = set(need(n).submot)
        for e in range(len(candide)):
            palm.add(list(candide)[e])
        for o in range(len(candido)):
            palm.add(list(candido)[o])

    for l in range(len(palm)):
        say(list(palm[l]))  # converts set into a list every each row.
        schedule.every(3).minutes.do(passing())  # schedule its False.
        message = hear.get["ts"]

        while True:
            time.sleep(1)

            if "next" or "siguiente" in hear.get["text"]:
                schedule.cancel_job(passing())
                break
'''
            @sea.on("reaction_added")
            def reaction_added(event_data):
                event = event_data["event"]
                emoji = event["reaction"]
                channel = event["item"]["channel"]

                if reaction_added(hear()) == ":"

                else:

                return

            try:
            # if
            finally:
                continue
'''