import yagmail

receiver = 'tyneha56@gmail.com'  # receiver email address

a = "Report" # Tittle
#loc = r"C:\Users\Ankit\Desktop\Study\Project\FRAS\Attendance\Attendance_2021-07-12_12-56-51.csv" # Attachment Location
loc = input("Enter Attendence File Location: ")
body = []
body.append(a)
body.append(loc)

# mail information
Sender = "senprod34xx.gn@gmail.com"
passwd = "@F4BCW#gcbqb#rq68b#mwcf8#XW6XB@"
yag = yagmail.SMTP(user=Sender, password=passwd)

# sent the mail
yag.send(
    to = receiver,
    subject = "Attendence Report",  # email subject
    contents = body,  # email body
)
print("\n*******SENT SUCCESSFULL*******")