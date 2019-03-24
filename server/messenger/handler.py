# -*- coding: utf-8 -*-

from models import ChatState, ClientData
from store import DB as db
from sqlalchemy import desc
import requests

# DEFAULT_FLOW = [
#   { prompt_key: 'site', prompt_text: 'Where are you picking' },
#   { prompt_key: 'nextq', prompt_text: 'Where are you picking' },
#   { prompt_key: 'site', prompt_text: 'Where are you picking' },
#   { prompt_key: 'site', prompt_text: 'Where are you picking' },
#   { prompt_key: 'site', prompt_text: 'Where are you picking' },
#   { prompt_key: 'site', prompt_text: 'Where are you picking' },
# ]

PAGE_ACCESS_TOKEN = "EAALcZCqwNKDkBAKKNbrItcJU9JFQdER2qNZAl0JOavKpKWPtRZBqeEdU6pkDiAro4o8aUjv0DMjSZC4212v43lPjG8J87I9PD27zVydKmZBCFsCMpT4kBGhfDUvZBZAMp1xlDLgTpLyB0sEIZAMm6r2wmW2oy9T6dR7Rwye3g0U5UwZDZD"

def handleMessage(sender_psid, received_message, payload):
  print(received_message);

  # Fetch most recent chat state row for this sender_psid
  # chat_state = ChatState.objects.get(client_id=sender_psid)
  last_chat_state = ChatState.query.filter_by(client_id=sender_psid).order_by(desc(ChatState.id)).first()

  onboarded_state = ChatState.query.filter_by(prompt_key="onboarded").first()
  is_onboarded = onboarded_state != None

  # Print out state-relevant variables
  if payload:
    print("Payload " + payload)
  if last_chat_state:
    print("Last Chat State: " + last_chat_state.prompt_key)

  # Introduction
  if last_chat_state == None:
    sendTextMessage(sender_psid, u"introduction", "Hello! I'm Trichy the Pullbot 😁!")
    sendTextMessage(sender_psid, "query_name", "Let's start by getting to know each other :). What's your name?")

  # Route to right intervention from the menu
  elif last_chat_state.prompt_key == "menu":
    if payload == "hi":
      sendTextMessage(sender_psid, "hi", "Hi!")
    elif payload == "is_pulling":
      sendTextMessage(sender_psid, "breathing_explain", "No need to fret. Kudos to you for hitting me up 😎! Let's first do a quick breathing exercise.")
      sendQuickReplies(sender_psid, "breathing_gif", "[INSERT KRISTEN's GIF HERE]", [("I'm done", "breathing_done")])
    else:
      sendTextMessage(sender_psid, "hi", "Ok")

  # Send breathing excercise
  elif last_chat_state.prompt_key == "breathing_gif":
    sendTextMessage(sender_psid, None, "I'm going to ask you a couple of questions.")
    sendQuickReplies(sender_psid, "query_location", "Where are you right now?", [
      ("Home 🏠", "home"),
      ("Work 🖥", "work"),
      ("School 🏫", "school"),
      ("Somewhere else", "other"),
    ])

  # Query for location
  elif last_chat_state.prompt_key == "query_location":
    pull_location = payload
    # addClientData(sender_psid, "query_location", pull_location)
    sendQuickReplies(sender_psid, "query_site", "Where were you pulling from?", [
      ("Head", "head"),
      ("Eyebrows", "eyebrows"),
      ("Eyelashes", "eyelashes"),
      ("Other", "other"),
    ])

  # Store location, and query pull site
  elif last_chat_state.prompt_key == "query_site":
    pull_site = payload
    # addClientData(sender_psid, "query_site", pull_site)
    sendQuickReplies(sender_psid, "query_severity", "How bad did you pull from 1 (just a hair or two) to 5 (it was a long session 😢)?", [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
      ])

  # Store pull site, and query severity
  elif last_chat_state.prompt_key == "query_severity":
    pull_severity = payload
    # addClientData(sender_psid, "query_severity", pull_severity)
    sendQuickReplies(sender_psid, "start_query_thoughts", "Do you have a few minutes to tell me about how you were feeling and what you were thinking?", [
      ("Sure", "sure"),
    ])

  # Store severity, and query thoughts
  elif last_chat_state.prompt_key == "start_query_thoughts":
    sendQuickReplies(sender_psid, "query_feelings", "When the pulling started, how were you feeling?", [
        ("Happy 😁", "happy"),
        ("Sad 😞", "sad"),
        ("Stressed 😰", "stressed"),
        ("Tired😴", "tired"),
        ("Bored 😒", "bored"),
      ])

  # Store feeling, and query for thoughts
  elif last_chat_state.prompt_key == "query_feelings":
    pull_feeling = payload
    # addClientData(sender_psid, "query_feelings", pull_feeling)
    sendTextMessage(sender_psid, "query_thoughts", "What were you thinking about?")

  # Store thoughts, and thank the user
  elif last_chat_state.prompt_key == "query_thoughts":
    pull_thoughts = payload
    # addClientData(sender_psid, "query_thoughts", pull_thoughts)
    sendQuickReplies(sender_psid, "finishing_pull_flow", "Thanks for your answers. Now get back out there 😁!", [
      ("😎 Yea! 💪", "ok"),
    ])

  # Ask for name
  elif last_chat_state.prompt_key == "query_name":
    name = received_message
    # TODO(ben): do something with the name
    sendTextMessage(sender_psid, "query_duration", "How long have you been dealing with this issue?")

  # Ask how long they've struggled with Trich
  elif last_chat_state.prompt_key == "query_duration":
    duration = received_message
    # TODO(ben): do something with duration of disorder
    sendTextMessage(sender_psid, None, u"Don't be too hard on yourself 🤷‍♀️. Deborah and I are going team up together and tell you about some tools that you can use to cope with Trich!")
    sendTextMessage(sender_psid, None, "We're going to do a few things that are related to an evidence-based treatment called habit-reversal therapy.")
    sendTextMessage(sender_psid, None, u"That's the complicated way of saying that we'll work on some proven techniques to help you better control your pulling habit! 💪")
    addChatState(sender_psid, "onboarded")

  # Catchall menu
  elif is_onboarded:
    menuOptions = [
      (u"I'm pulling 😔", "is_pulling"),
      (u"Hi 👋", "hi"),
    ]
    sendQuickReplies(sender_psid, "menu", "How can I help? 👋", menuOptions)

  # Send next message depending on the previous prompt key

  # SAVE reponse in CLIENT DATA
  # if received_message == "help":


def sendTextMessage(sender_psid, prompt_key, text):
  message_data = {
    'recipient': {
      'id': sender_psid
    },
    'message': {
      'text': text
    }
  }
  callSendAPI(sender_psid, prompt_key, message_data)

def sendQuickReplies(sender_psid, prompt_key, text, options):
  message_data = {
    'recipient': {
      'id': sender_psid
    },
    'message': {
      'text': text,
      'quick_replies': [
        dict(content_type="text", title=title, payload=payload) for (title, payload) in options
      ]
    }
  }
  callSendAPI(sender_psid, prompt_key, message_data)

def addChatState(sender_psid, prompt_key):
  new_chat_state = ChatState(sender_psid, prompt_key)
  db.session.add(new_chat_state)
  db.session.commit()

def addClientData(sender_psid, prompt_key, response):

  # determine session_id from the number of `query_thoughts` client datas that exist
  num_client_data = ClientData.query.filter_by(prompt_key='query_thoughts').all()
  session_id = num_client_data

  new_client_data = ClientData(sender_psid, -1, session_id, prompt_key, response)
  db.session.add(new_client_data)
  db.session.commit()


def callSendAPI(sender_psid, prompt_key, message_data):
  if prompt_key:
    new_chat_state = ChatState(sender_psid, prompt_key)
    db.session.add(new_chat_state)
    db.session.commit()

  # SEND TO MESSENGER
  print("--- Sending Message ---")
  print(message_data)
  url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(PAGE_ACCESS_TOKEN)
  r = requests.post(url, json=message_data)
  if not r.status_code == requests.codes.ok:
    print(r)
    raise Exception("There was an error sending a message.")
