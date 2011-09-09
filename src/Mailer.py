# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Gmail Mailer!! Use you gmail account to send emails through the command line.

Usage:
    Mailer.py [-smf] [Email Addresses]
    Mailer.py [-sm] "mail@mail.com" "another@mail.com" ...
    Mailer.py -s "Hey whats up man" -m "How's it going...." "mail@mail.com"
    
Options:
    -s    --subject=    enter subject of mail
    -m    --message=    enter message of mail
    -f    --files=      absolute paths of files no directories!!
                        use comma to separate between files 
    
You need a gmail account to activate this.
Just change the variables "gmail_user" and "gmail_pwd\""""
    
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os,sys,getopt,re
from datetime import datetime

gmail_user = "YOUR_ACCOUNT@GMAIL.COM"
gmail_pwd = "YOUR_GMAIL_PASSWORD"
defMessage = { "message": u"משהו זז בבית %s " % str(datetime.now()), 
              "subject":u"תזוזה אותרה"}


def mail(to, subject, text , attach):
    msg = MIMEMultipart()
    
    msg['From'] = gmail_user
    msg['To'] = ', '.join(to)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(text, 'plain', 'UTF-8'))
    if attach:
        for atc in attach:
            try:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(atc, 'rb').read())
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition',
                        'attachment; filename="%s"' % os.path.basename(atc))
                msg.attach(part)
            except IOError:
                print "File %s wasn't found" % atc 
    try:
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()
    except smtplib.SMTPException as (errno, strerror):
        print "SMTP Error({0}): {1}".format(errno, strerror)
        raise
    return True

def mailFilter(mail):
    pat = re.compile("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
    return bool(pat.match(mail))

def filesFilter(file_path):
    return os.path.isfile(file_path)

def main():
    args = sys.argv[1:]
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:s:f:", ["help", "message=", "subject=", "files="])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    attachments = None
    subject = defMessage['subject']
    msg = defMessage['message']
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
        if o in ("-m", "--message"):
            msg = a or msg
        if o in ("-s", "--subject"):
            subject = a or subject
        if o in ("-f", "--files"):
            attachments = a.split(',')
            attachments = filter(filesFilter, attachments)
    lst = filter(mailFilter, args)
    if lst:
        try:
            result = mail(lst, subject, msg, attachments)
            if result:
                print "Package delivered successfully"
            else:
                print "Package delivery failed"
        except smtplib.SMTPException:
            print "Package delivery failed"
    else:
        print 'No valid mail addresses where given.'
    
if __name__ == "__main__":
    main()
    