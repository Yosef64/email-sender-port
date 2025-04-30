from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import requests
import smtplib

app = FastAPI()
key = os.getenv("APP_KEY","hxqp eito aaud eslj")
bot_token = os.getenv("BOT_TOKEN", "")
chat_id = os.getenv("CHAT_ID", "")
origins = [
    "https://yosephalemu.vercel.app",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send-email")
async def send_email(request: Request):
    data = await request.json()
    message = data.get("message")
   
    try:

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            print("Message sent successfully")
            return JSONResponse({"message": "Message sent successfully"}, status_code=200)
        else:
            print("Failed to send message")
            return JSONResponse({"message": "Failed to send message"}, status_code=500)
    except KeyError:
        return JSONResponse({"message": "Missing required fields"}, status_code=400)
    except smtplib.SMTPAuthenticationError:
        return JSONResponse({"message": "Email authentication failed"}, status_code=500)
    except Exception as e:
        print(e)
        return JSONResponse({"message": "Failed to send email"}, status_code=500)
   

@app.get("/")
async def index(request: Request):
    return {"message": "ok"}