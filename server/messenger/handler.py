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

    if payload == "is_pulling":
      sendTextMessage(sender_psid, "breathing_explain", "No need to fret. Kudos to you for hitting me up 😎! Let's first do a quick breathing exercise.")
      sendGIF(sender_psid, "breathing_gif", "https://media.giphy.com/media/3ouRtqtUQaw0PNQIz4/giphy.gif")
      sendQuickReplies(sender_psid, "breathing_gif", "Do that for 30 seconds. Let me know when you're done.", [("I'm done", "finish_breathe_flow")])

    # Send breather
    elif payload == "need_breather":
      sendTextMessage(sender_psid, None, "Let's do a quick inhale-exhale exercise. Take a breather in your day! Do that for 30 seconds.")
      sendGIF(sender_psid, "breathing_gif", "https://media.giphy.com/media/3ouRtqtUQaw0PNQIz4/giphy.gif")
      sendQuickReplies(sender_psid, "solo_breathing_gif", "Let me know when you're done.", [("I'm done", "breathing_done")])

    # Start MGH-HPS
    elif payload == "start_benchmark":
      sendTextMessage(sender_psid, None, "Ok! I'm going to ask you a few questions which will help Deborah understand how you're doing.")
      sendTextMessage(sender_psid, None, "This shouldn't take more than 15 minutes.")
      sendQuickReplies(sender_psid, "confirm_ready", "Ready to start?", [
        ("Let's do this!", "a")
      ])

    # Catch all
    else:
      sendTextMessage(sender_psid, "hi", "👋")

  # Benchmark question 1
  elif last_chat_state.prompt_key == "confirm_ready":
    sendQuickReplies(sender_psid, "benchmark_q1", """
      [1/7] On an average day, *how often* did you feel the urge to pull your hair?\n
      0 - This week I felt *no* urges to pull my hair.
      1 - This week I felt an *occasional* urge to pull my hair.
      2 - This week I felt an urge to pull my hair *often*.
      3 - This week I felt an urge to pull my hair *very often*.
      4 - This week I felt near *constant* urges to pull my hair.
    """, [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
      ])

  # Benchmark question 2
  elif last_chat_state.prompt_key == "benchmark_q1":
    sendQuickReplies(sender_psid, "benchmark_q2", """
      [2/7] On an average day, *how intense or “strong”* were the urges to pull your hair?\n
      0 - This week I *did not feel* any urges to pull my hair. 
      1 - This week I felt *mild* urges to pull my hair.
      2 - This week I felt *moderate* urges to pull my hair. 
      3 - This week I felt *severe* urges to pull my hair. 
      4 - This week I felt *extreme* urges to pull my hair. 
    """, [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
      ])

  # Benchmark question 3
  elif last_chat_state.prompt_key == "benchmark_q2":
    sendQuickReplies(sender_psid, "benchmark_q3", """
      [3/7] On an average day, *how much control* do you have over the urges to pull your hair? \n
      0 - This week I could *always* control the urges, or I did not feel any urges to pull my hair.  
      1 - This week I was always able to distract myself from the urges to pull my hair *most of the time*. 
      2 - This week I was able to distract myself from the urges to pull my hair *some of the time*. 
      3 - This week I was able to distract myself from the urges to pull my hair *rarely*. 
      4 - This week I was *never* able to distract myself from the urges to pull my hair. 
    """, [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
      ])

  # Benchmark question 4
  elif last_chat_state.prompt_key == "benchmark_q3":
    sendQuickReplies(sender_psid, "benchmark_q4", """
      [4/7] On an average day, *how often* did you actually pull your hair? \n
      0 - This week I *did not* pull my hair. 
      1 - This week I pulled my hair *occasionally*.
      2 - This week I pulled my hair *often*.
      3 - This week I pulled my hair *very often*.
      4 - This week I pulled my hair so often I felt like I was *always* doing it.
    """, [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
      ])

  # Benchmark question 5
  elif last_chat_state.prompt_key == "benchmark_q4":
    sendQuickReplies(sender_psid, "finish_flow", """
      [5/7] On an average day, *how often did you make an attempt to stop* yourself from actually pulling your hair?  \n
      0 - This week I felt no urges to pull my hair.
      1 - This week I tried to resist the urge to pull my hair *almost all of the time*. 
      2 - This week I tried to resist the urge to pull my hair *some of the time*. 
      3 - This week I tried to resist the urge to pull my hair *rarely*.
      4 - This week I *never* tried to resist the urge to pull my hair. 
    """, [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
      ])

  # Send breathing excercise
  elif last_chat_state.prompt_key == "solo_breathing_gif":
    sendTextMessage(sender_psid, "finish_flow", "👋")

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

  # Handle end of dialogs with nothing
  elif last_chat_state.prompt_key == "finishing_pull_flow":
    sendTextMessage(sender_psid, "finish_flow", "👋")

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
      ("I'm pulling 😔", "is_pulling"),
      ("I need a breather 💨", "need_breather"),
      ("Take the MGH-HPS 📝", "start_benchmark")
    ]
    sendQuickReplies(sender_psid, "menu", "How can I help? 👋", menuOptions)

  # Send next message depending on the previous prompt key

  # SAVE reponse in CLIENT DATA
  # if received_message == "help":

def sendGIF(sender_psid, prompt_key, from_url):
  message_data = {
    'recipient': {
      'id': sender_psid
    },
    'message': {
      "attachment": {
        "type": "image", 
        "payload":{
          "url": from_url, 
          "is_reusable": True
        }
      }
    }
  }
  callSendAPI(sender_psid, prompt_key, message_data)

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
