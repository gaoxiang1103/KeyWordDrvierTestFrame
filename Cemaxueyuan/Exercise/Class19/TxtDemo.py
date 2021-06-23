# 使用Python发送文本邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 创建邮箱服务器
con = smtplib.SMTP_SSL('smtp.163.com','465')
# con = smtplib.SMTP()
# con.connect('smtp.163.com',25)
# con.set_debuglevel(0)
# 使用用户名、密码登录邮箱，密码其实是授权密码
con.login('gaoxiang1103@163.com','LATOAUHKRZXJOHRO')
# print(con)

#发送者账号
sender = 'gaoxiang1103@163.com'
# 接收者账号
recevier = ['2314986036@qq.com','xgao4@amarsoft.com']

# 文本邮件内容
txt = '这是文本邮件正文'
message = MIMEText(txt,'plain','utf-8')
subject = '这是文本文件的标题'
message['Subject'] =Header(subject,'utf-8')
message['Form'] =('gaoxiang<gaoxiang1103@163.com>')
message['To'] =('gaoxiang<2314986036@qq.com>,gaoxiang<xgao4@amarsoft.com>')

try:
    con.sendmail(sender,recevier,message.as_string())
    print('邮件发送成功！')
except Exception as e:
    print('邮件发送失败，抛出了异常，异常信息为%s'%e)


