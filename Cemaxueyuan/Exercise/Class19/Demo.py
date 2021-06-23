import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
 
mail_host="smtp.163.com"
mail_user="gaoxiang1103@163.com"
mail_pass="LATOAUHKRZXJOHRO"
sender = 'gaoxiang1103@163.com'
receivers = '2314986036@qq.com'
body_content = """ 测试文本  """
 
message = MIMEText(body_content, 'plain', 'utf-8')
message['From'] = "gaoxiang<gaoxiang1103@163.com>"
message['To'] = "gaoxiang<2314986036@qq.com>"
subject = """
项目异常测试邮件
"""
message['Subject'] = Header(subject, 'utf-8')
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)  
smtpObj.set_debuglevel(1)
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
smtpObj.quit()