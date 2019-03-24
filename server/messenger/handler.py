from models import ChatState, ClientData
from store import DB as db

def handleMessage(sender_psid, received_message):
  print(received_message);

  # SAVE reponse in CLIENT DATA

  # Fetch most recent chat state row for this sender_psid
  # Send next message depending on the previous prompt key

def callSendAPI(sender_psid, prompt_key):
  new_chat_state = ChatState(sender_psid, prompt_key)
  db.session.add(new_chat_state)
  db.session.commit()

  # SEND TO MESSENGER
