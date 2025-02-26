import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import nodemailer from "nodemailer";

dotenv.config();

const app = express();
app.use(express.json());
app.use(cors({ origins: ["http://localhost:5173","yosephalemu.vercel.app"] })); 

const transporter = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 587, 
  service: "gmail",
  auth: {
    user: "yosefale65@gmail.com",
    pass: "hxqp eito aaud eslj",
  },
});

app.post("/send-email", async (req, res) => {
  try {
    const { email, subject, message, name } = req.body;

    const mailOptions = {
      from: email,
      to: "yosefale65@gmail.com", 
      subject: subject,
      text: `From: ${name} (${email})\n\n${message}`,
    };

    const mailOptions1 = {
      from: "yosefale65@gmail.com", 
      to: email,
      subject: `Confirmation: ${subject}`,
      text: `Hi ${name},\n\nWe received your message: "${message}"\n\nThanks!`,
    };

    await transporter.sendMail(mailOptions);
    await transporter.sendMail(mailOptions1);

    console.log("Emails sent successfully");
    res.json({ message: "Emails sent successfully" });
  } catch (error) {
    console.error("Error sending email:", error);
    res.status(500).json({ error: error.message });
  }
});

app.listen(5000, () => console.log("Server running on port 5000"));
