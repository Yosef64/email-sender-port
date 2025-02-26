import nodemailer from "nodemailer";
// const nodemailer = require("nodemailer");
const transporter = nodemailer.createTransport({
  port: "smtp.gmail.com",
  service: "gmail",
  auth: {
    user: "yosefale65@gmail.com",
    pass: "hxqp eito aaud eslj",
  },
});
const mailOptions = {
  from: "Yoseph Alemu",
  to: "josiqlex@gmail.com",
  subject: "Test Email",
  text: "Hello! This is a test email sent using Nodemailer with ES modules.",
};
export async function main() {
  try {
    const info = await transporter.sendMail(mailOptions);
    console.log("Email sent:", info.response);
  } catch (error) {
    console.error("Error:", error);
  }
}
main().catch(console.error);
