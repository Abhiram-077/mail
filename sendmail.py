import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

sender = "abhmp777@gmail.com"
receiver = "vjtctqoig@laste.ml"
subject = 'Test mail using python'
contents = '''
This is the content side for sending mail
'''

yag =yagmail.SMTP(user=sender,password=os.getenv('password'))
yag.send(to=receiver,subject=subject,contents=contents)
print("Email send")
