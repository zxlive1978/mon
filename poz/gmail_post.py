#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def post(message,topic):
	msg = MIMEMultipart()
	msg['From'] = 's.sedyshev@agg.gazpromgeofizika.ru'
	msg['To'] = 's.sedyshev@agg.gazpromgeofizika.ru'
	msg['Subject'] = unicode(topic,"utf-8")
	#message = 'here is the email'
	msg.attach(MIMEText(message.encode('utf-8'), 'plain', 'UTF-8'))

	mailserver = smtplib.SMTP('smtp.gmail.com',587)
	mailserver.ehlo()
	mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('djarastafarabg@gmail.com', 'Greatwall1978')
	#mailserver.sendmail('s.sedyshev@agg.gazpromgeofizika.ru','djarastafarabg@gmail.com',msg.as_string())
	#mailserver.sendmail('s.sedyshev@agg.gazpromgeofizika.ru','s.sedyshev@agg.gazpromgeofizika.ru',msg.as_string())
	mailserver.sendmail('zxlive@yandex.ru','zxlive@yandex.ru',msg.as_string())
	mailserver.quit()

#post("Отвалился Мегафон")


	
#Read more: http://plutonit.ru/view_post.php?id=704#ixzz51tiYknsb
