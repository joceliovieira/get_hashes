from vars import *
from pprint import pprint
import json
import requests
import pandas as pd
import numpy as np
import hashlib
import urllib
import datetime

def get_hash(url_input):
  response = urllib.request.urlopen(url_input)
  hash_md5 = hashlib.md5()
  hash_md5.update(response.read())
  return hash_md5.hexdigest()

def get_hashes(sigla_input):
  while True:
    params = {
      'siglaTipo': [],
      'dataApresentacaoInicio': [datetime.date.today() - datetime.timedelta(3)]
    }
    var_error = []
    var_ok = []
    cont = 0
    siglaTipo = str(sigla_input)
    siglas = [item.strip() for item in siglaTipo.split(sep=',')]
    try:
      for i in siglas:
        cont+=1
        if i not in ['PEC', 'PLP', 'PL']:
          var_error.append(i)
        else:
          var_ok.append(i)
        if (cont==len(siglas)):
          if(len(var_error)>0):
            raise ValueError
          else:
            pass
          params['siglaTipo'].append(var_ok)
          
    except ValueError:
      if (len(var_error)==1):
        return {
          'data': "O tipo da seguinte proposicao nao e adequado: " + str(var_error[0]),
          'status_code': 400
        }
      else:
        print(f"Os tipos das seguintes proposições não são adequados: %s " % str(var_error))
        print("Insira os tipos novamente.")
      break
    
    print(f"Coletando informações sobre as proposições do tipo %s apresentadas nos últimos 3 dias." % var_ok)
    response = requests.get(url, params)
    id_serie = pd.json_normalize(response.json()['dados'])[['id','siglaTipo']]
    requests_list = [url + str(i) for i in id_serie['id']]
    dados_iniciais = [(j['id'], j['siglaTipo'], j['urlInteiroTeor']) for j in [requests.get(i).json()['dados'] for i in requests_list]]
    df_01 = pd.DataFrame(dados_iniciais, columns=['id', 'siglaTipo', 'urlInteiroTeor'])
    lista_hashes = [(df_01.iloc[i]['id'], get_hash(df_01.iloc[i]['urlInteiroTeor'])) for i in range(0,len(df_01))]
    df_02 = pd.DataFrame(lista_hashes, columns=['id', 'hashmd5'])
    df_final = df_02.merge(df_01, on='id')
    ld_final = json.loads(df_final.drop(columns=['urlInteiroTeor']).to_json(orient='records'))
    lista_final_hashes = [i['hashmd5'] for i in ld_final]    
    return {
      'data': ld_final,
      'status_code': 200
      }
