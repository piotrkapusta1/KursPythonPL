import smtplib
     
mailFrom = 'Testowy serwer 5G'
mailTo = ['kamil.mazela@imif.lukasiewicz.gov.pl', 'bartlomiej.sikora@imif.lukasiewicz.gov.pl']
mailSubject = 'Test aplikacji 5G 1000%'
mailBody = '''Elo
     
No gitara siema
     
Have a nice day!'''
     
message = '''From: {}
Subject: {}
     
{}
'''.format(mailFrom, mailSubject, mailBody)
     
user = ''
password = ''
     
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mails sent')
except:
    print('error sending email')