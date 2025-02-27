from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import smtplib
app = FastAPI()
key = os.getenv("APP_KEY")
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
async def send_email(request:Request):
    data = await request.json()
    try:
        email, subject, message, name = data['email'], data['subject'], data['message'], data['name']
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("yosefale65@gmail.com",key)
        server.sendmail("yosefale65@gmail.com",email,message)
        server.quit()
        return JSONResponse({"message":"ok"},status_code=200)
    except Exception as e:
        return JSONResponse({"message":e},status_code=500)
    
    
    




    


