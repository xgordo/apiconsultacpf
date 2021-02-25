from flask import Flask
import requests, os, time, base64, json, re
import platform

def clear():
   if platform.system() == "Windows":
      os.system("cls")
   elif platform.system() == "Linux":
      os.system("clear")
   else:
       os.system("clear")

R='\033[1;31m'; B='\033[1;34m'; C='\033[1;37m'; Y='\033[1;33m'; G='\033[1;32m'; RT='\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
a=a.encode('ascii')
a=base64.b64decode(a)
a=a.decode('ascii')
def consultar(cpf):
  try:
    h={
    'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
    'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
    'Host': "www.juventudeweb.mte.gov.br"
    }
    r=requests.post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text
    clear()
    chave1 = "{"
    chave2 = "}"

    resultado=f"""
{chave1}"CPF": "{re.search('NRCPF="(.*?)"', r).group(1)}",
"Nome": "{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}",
"Nascimento": "{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}",
"Nome da Mae": "{re.search('NOMAE="(.*?)"', r).group(1).title()}",
"Endereco": "{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}",
"Complemento": "{re.search('DSCOMPLEMENTO="(.*?)"', r).group(1).title()}",
"Bairro": "{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}",
"Cidade": "{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}",
"CEP": "{re.search('NRCEP="(.*?)"', r).group(1)}"{chave2}
"""
    #resultadojson = json.loads(resultado)
  except:
    print(f'{R}CPF inexistente{C}' + "\n")
  return resultado

app = Flask(__name__)
@app.route("/cpf/<cpf>", methods=["GET"])
def busca(cpf):
    try:
        a = consultar(cpf=cpf)
    except:
        a = "cpf erro"
    return a
app.run(host="0.0.0.0")
