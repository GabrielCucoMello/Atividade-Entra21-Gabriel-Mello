from email.mime.multipart import MIMEMultipart
import smtplib, ssl
import locale
from datetime import datetime
from email.mime.text import MIMEText
from src.database_connect import chuva_hoje, chance_chuva_hoje
from src.local_settings import senha
from src.clientes import clientes_final, consta_feriado, dia_semana
from src.funcionarios import funcionarios_final

locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
data_hoje = datetime.now()
data_format = data_hoje.strftime('%d de %B de %Y')

if dia_semana == 6 or dia_semana == 7:
    final_de_semana = 'Sim'
else:
    final_de_semana = 'Não'

port = 465 # porta do servidor que envia emails
smtp_server = 'smtp.gmail.com' # conector pra enviar email
sender = 'cucomellocm@gmail.com' # email de quem vai enviar
receiver = 'gabreelzocm@gmail.com'# email de quem vai receber
password = senha # senha do google

msg = MIMEMultipart('alternative')

html = (f'''\
<html>
    <head></head>
    <body>
    <h2> Previsão de Clientes e Funcionários para o dia de hoje: {data_format} </h2>
    <p> Chance de chuva: {chance_chuva_hoje}; </p>
    <p> Milímetros de chuva esperados: {chuva_hoje}; </p>
    <p> Hoje é um final de semana? {final_de_semana}; </p>
    <p> Hoje tem algum feriado? {consta_feriado}; </p>
    <p> Clientes esperados para o dia: {clientes_final}; </p>
    <p> Funcionarios esperados para o dia {int(funcionarios_final)}. </p>
    </body>
</html>
''') # Conteúdo do email

parte1 = MIMEText(html, 'html')

msg.attach(parte1)
msg['Subject'] = 'Previsão do tempo para este dia e os dias seguintes' # Assunto do email
msg['From'] = 'cucomellocm@gmail.com'
msg['To'] = 'gabreelzocm@gmail.com'

context = ssl.create_default_context() # conexão com a biblioteca

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login('cucomellocm@gmail.com', password) # conexão com o servidor que envia emails
    server.sendmail(sender, receiver, msg.as_string()) # envio do email