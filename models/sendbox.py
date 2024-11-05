import os
from twilio.rest import Client
import json
import logging

logging.basicConfig(level=logging.INFO)
def sendbox(phone_number, data, content_sid):
    try:
        account_sid = "AC2ab4c42295015a68595e14662812d8be"
        auth_token = "366518d91d66b63a406dde259151108e"
        messaging_service_sid = "MG5e51dae099b377e3dedef52672b8fb2b"
        client = Client(account_sid, auth_token)

        from_whatsapp = "whatsapp:+14155238886"
        if not phone_number.startswith("+"):
            raise ValueError("Phone number must be in international format, starting with '+'.")
        message = client.messages.create(
            content_sid=content_sid,
            to=f"whatsapp:{phone_number}",
            from_=from_whatsapp,
            content_variables=json.dumps(data), 
            messaging_service_sid=messaging_service_sid
        )

        logging.info(f"Message sent successfully to {phone_number} with SID: {message.sid}")
        return True

    except Exception as e:
        logging.error(f"Failed to send message: {str(e)}", exc_info=True)
        return False

