from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import smtplib

app = FastAPI()
key = os.getenv("APP_KEY","hxqp eito aaud eslj")

origins = [
    "https://victory-contest.vercel.app",
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
    print(key)
    try:
        email, subject, message, name = data['email'], data['subject'], data['message'], data['name']
        msg = MIMEMultipart()
        msg["From"] = "yosefale65@gmail.com"
        msg["To"] = email
        msg["Subject"] = subject
        msg.attach(MIMEText(f"From: {name}\n\n{message}", "plain"))

        
        server = smtplib.SMTP("smtp.gmail.com")
        server.starttls()
        server.login("yosefale65@gmail.com", key)
        server.sendmail("yosefale65@gmail.com", email, msg.as_string())
        server.quit()
    
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