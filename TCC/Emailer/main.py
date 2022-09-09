import smtplib, ssl
from email.mime.text import MIMEText

chuva  = 10
funcionarios_final = 0
funcionarios_normal = 600
funcionarios_chuva = 0
funcionarios_feriado = 0
feriado = 0
consta_feriado = []
feriado_final = ''

# ^ variáveis para a predição

if chuva >= 5:
    funcionarios_chuva = funcionarios_normal * 0.5
elif feriado == 1:
    funcionarios_feriado = funcionarios_chuva * 2
    consta_feriado.append('Sim')
if feriado == 0:
    consta_feriado.append('Não')

if funcionarios_chuva > 0:
    funcionarios_final = funcionarios_chuva
elif funcionarios_feriado > 0:
    funcionarios_final = funcionarios_feriado
else:
    funcionarios_final = funcionarios_normal

# ^ predição de funcionários

port = 465 # porta do servidor que envia emails
smtp_server = 'smtp.gmail.com' # conector pra enviar email
sender = 'cucomellocm@gmail.com' # email de quem vai enviar
receiver = 'gabreelzocm@gmail.com'# email de quem vai receber
password = input('Digite sua senha gerada do google: ') # input da senha do google

msg = MIMEText(f'''
    Milímetros de chuva esperados: {chuva};
    O dia é um feriado? {feriado_final.join(consta_feriado)};
    Funcionarios esperados pro dia: {funcionarios_final}. 
''') # Conteúdo do email
msg['Subject'] = 'Previsão do tempo para este dia e os dias seguintes' # Assunto do email
msg['From'] = 'cucomellocm@gmail.com'
msg['To'] = 'gabreelzocm@gmail.com'

context = ssl.create_default_context() # conexão com a biblioteca

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login('cucomellocm@gmail.com', password) # conexão com o servidor que envia emails
    server.sendmail(sender, receiver, msg.as_string()) # envio do email