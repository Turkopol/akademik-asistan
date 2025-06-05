import yagmail

def send_announcement(df_students, subject, message):
    sender = "youremail@gmail.com"
    yag = yagmail.SMTP(user=sender, password="YOUR_APP_PASSWORD")

    for index, row in df_students.iterrows():
        receiver = row['email']
        personalized_msg = f"Merhaba {row['name']},\n\n{message}"
        yag.send(to=receiver, subject=subject, contents=personalized_msg)
