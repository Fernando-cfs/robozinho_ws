from selenium import webdriver # importa o selenium
from selenium.webdriver import Keys #  import teclas       forma errada from selenium.webdriver import Keys
from selenium.webdriver.common.by import By # importando o By
from selenium.webdriver.chrome.service import Service  # biblioteca pra atualizar o webdriver todas vez que roda o codigo sem precisar baixar a versao nova do chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # importa Opitions para colocar o argumento Headless 
from datetime import datetime
from time import sleep
import pandas as pd

def coletar_dados():
    options = Options() # pra minha variavel options a importacao Options
    options.add_argument('--headless')  # Headless é uma opção para executar seus testes sem a necessidade de abrir o browser em um ambiente gráfico


    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), #instala aoutomatico a versao do chrome toda vez que ocodigo rodar
        options=options
    )



    driver.get('https://economia.uol.com.br/') 

    empresas = ['petrobras on', 'magazine luiza', 'oi on']
    valores = list()
    data_hora = list()


    for empresa in empresas:
        sleep(5)
        input_busca = driver.find_element(By.ID, 'filled-normal') 
        
        input_busca.send_keys(empresa) 
        sleep(2)
    


        input_busca.send_keys(Keys.ENTER)
        sleep(4)

        span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
        cotacao_valor = span_val.text

        valores.append(cotacao_valor)
        data_hora.append(datetime.now().strftime('%d/%m/%y %H:%M:%S')) 
        print(f'Empresas:{empresa}') # pra ver que ta rodando o codigo ja que nao vai ver o site

    dados = {
        'empresas': empresas,
        'valor': valores,
        'data_hora': data_hora,

    }
    return dados
    # print(dados)
def criar_execel(dados, file_name):
    df_empresas = pd.DataFrame(dados)
    df_empresas.to_excel(file_name, index=False)     

dados = coletar_dados()
criar_execel(dados, './empresas_acoes.xlsx')