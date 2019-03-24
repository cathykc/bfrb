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

PAGE_ACCESS_TOKEN = "EAALcZCqwNKDkBACyb88m5reKztGAHS72IGohR2GHaWEXeUYD23gWOslrXq0afeJxhuSKVk2UZBbi9M5gG9FrZAYeER72JF9GfL7qNcViZCWO8Gm8kl3SNGVxvj5iXuT5ZAaKckm555ZBERXfDAZBccA1ovFMpxjn3QdMmKFZBjSqpAZDZD"

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

  # Route to right intervention from the menu
  if last_chat_state.prompt_key == "menu":
    if payload == "hi":
      sendTextMessage(sender_psid, "hi", "Hi!")
    elif payload == "is_pulling":
      sendTextMessage(sender_psid, "breathing", "No need to fret. Let's first do a quick breathing exercise.")
    else:
      sendTextMessage(sender_psid, "hi", "Ok")

  # Introduction
  elif last_chat_state == None:
    sendTextMessage(sender_psid, u"introduction", "Hello! I'm Trichy the Pullbot 😁!")
    sendTextMessage(sender_psid, "query_name", "Let's start by getting to know each other :). What's your name?")

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
