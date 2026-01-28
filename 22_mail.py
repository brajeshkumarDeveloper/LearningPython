# password='urfbtrxuvzgxzqhu'
import smtplib

hostname = 'smtp.gmail.com'
email = ''
password = ''  # use env variable ideally
receive_email = ''

try:
    with smtplib.SMTP(hostname, 587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receive_email,
            msg="Subject:Test Python Email\n\nHi Developer, This is a test email"
        )
    print("Email sent successfully")
except Exception as e:
    print("Failed to send email:", e)

