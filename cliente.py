import urllib.request, json, time
import aiohttp

#rotas dos servicos de noticias de informacao
URL_SERVICO_PRIMEIRO_SEMESTRE = "http://localhost:5001/"
PRIMEIRO_SEMESTRE_IS_ALIVE = URL_SERVICO_PRIMEIRO_SEMESTRE + "isalive/"
PRIMEIRO_SEMESTRE = URL_SERVICO_PRIMEIRO_SEMESTRE + "grade/"

URL_SERVICO_SEGUNDO_SEMESTRE = "http://localhost:5002/"
SEGUNDO_SEMESTRE_IS_ALIVE = URL_SERVICO_SEGUNDO_SEMESTRE + "isalive/"
SEGUNDO_SEMESTRE = URL_SERVICO_SEGUNDO_SEMESTRE + "grade/"

URL_SERVICO_TERCEIRO_SEMESTRE = "http://localhost:5003/"
TERCEIRO_SEMESTRE_IS_ALIVE = URL_SERVICO_TERCEIRO_SEMESTRE + "isalive/"
TERCEIRO_SEMESTRE = URL_SERVICO_TERCEIRO_SEMESTRE + "grade/"

URL_SERVICO_QUARTO_SEMESTRE = "http://localhost:5004/"
QUARTO_SEMESTRE_IS_ALIVE = URL_SERVICO_QUARTO_SEMESTRE + "isalive/"
QUARTO_SEMESTRE = URL_SERVICO_QUARTO_SEMESTRE + "grade/"

URL_SERVICO_QUINTO_SEMESTRE = "http://localhost:5005/"
QUINTO_SEMESTRE_IS_ALIVE = URL_SERVICO_QUINTO_SEMESTRE + "isalive/"
QUINTO_SEMESTRE = URL_SERVICO_QUINTO_SEMESTRE + "grade/"

URL_SERVICO_SEXTO_SEMESTRE = "http://localhost:5006/"
SEXTO_SEMESTRE_IS_ALIVE = URL_SERVICO_SEXTO_SEMESTRE + "isalive/"
SEXTO_SEMESTRE = URL_SERVICO_SEXTO_SEMESTRE + "grade/"

URL_SERVICO_SETIMO_SEMESTRE = "http://localhost:5007/"
SETIMO_SEMESTRE_IS_ALIVE = URL_SERVICO_SETIMO_SEMESTRE + "isalive/"
SETIMO_SEMESTRE = URL_SERVICO_SETIMO_SEMESTRE + "grade/"

URL_SERVICO_OITAVO_SEMESTRE = "http://localhost:5008/"
OITAVO_SEMESTRE_IS_ALIVE = URL_SERVICO_OITAVO_SEMESTRE + "isalive/"
OITAVO_SEMESTRE = URL_SERVICO_OITAVO_SEMESTRE + "grade/"


def acessar(url):
    #print("acessando a url: ", url)

    response = urllib.request.urlopen(url)
    data = response.read()

    return data.decode("utf-8")
    
##################ISALIVE VERIFIANDO SE OS SERVICOS ESTAO ATIVOS#####################
def primeiro_semestre_is_alive():
    alive = False

    if acessar(PRIMEIRO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def segundo_semestre_is_alive():
    alive = False

    if acessar(SEGUNDO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def terceiro_semestre_is_alive():
    alive = False

    if acessar(TERCEIRO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def quarto_semestre_is_alive():
    alive = False

    if acessar(QUARTO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def quinto_semestre_is_alive():
    alive = False

    if acessar(QUINTO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def sexto_semestre_is_alive():
    alive = False

    if acessar(SEXTO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def setimo_semestre_is_alive():
    alive = False

    if acessar(SETIMO_SEMESTRE_IS_ALIVE) == "yes":
        alive = True
    
    return alive

def oitavo_semestre_is_alive():
    alive = False

    if acessar(OITAVO_SEMESTRE_IS_ALIVE) == "no":
        alive = True
    
    return alive
##############################################

def get_primeiro_semestre():
    data = acessar(PRIMEIRO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_segundo_semestre():
    data = acessar(SEGUNDO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_terceiro_semestre():
    data = acessar(TERCEIRO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_quarto_semestre():
    data = acessar(QUARTO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_quinto_semestre():
    data = acessar(QUINTO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_sexto_semestre():
    data = acessar(SEXTO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_setimo_semestre():
    data = acessar(SETIMO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def get_oitavo_semestre():
    data = acessar(OITAVO_SEMESTRE)
    data = json.loads(data)

    return data["grade"]

def imprimir(tipo_noticia, noticias):
    for noticia in noticias:
        print(f"Dia: {noticia['dia']}. Materia: {noticia['materia']}. Carga Horaria {noticia['carga-horaria']}. Horario: {noticia['horario']}")

if __name__ == "__main__":
    while True:
        #print("Servico está respondendo. Acessando notícias...")
        #verifica se o servico está ativo
        if primeiro_semestre_is_alive():
            #acessar as noticias do primeiro semestre
            print("\n")
            print("#############################################################################################################################")
            print("########################## servicos do primeiro semestre disponivel. Grade sendo apresentanda  ##############################")
            print("#############################################################################################################################")
           
            noticias = get_primeiro_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  #######################################################")
            print("########################################### SERVIÇO DO PRIMEIRO SEMESTRE NÃO ESTÁ FUNCIONANDO ################################")
            print("##############################################################################################################################")

        if segundo_semestre_is_alive():
            #acessar as noticias do segundo semestre
            print("\n")
            print("#############################################################################################################################")
            print("########################## servicos do segundo semestre disponivel. Grade sendo apresentanda  ###############################")
            print("#############################################################################################################################")
           
            noticias = get_segundo_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  ########################################################")
            print("########################################## SERVIÇO DO SEGUNDO SEMESTRE NÃO ESTÁ FUNCIONANDO ##################################")
            print("##############################################################################################################################")

        if terceiro_semestre_is_alive():
            #acessar as noticias do terceiro semestre
            print("\n")
            print("#############################################################################################################################")
            print("######################### servicos do terceiro semestre disponivel. Grade sendo apresentanda  ###############################")
            print("#############################################################################################################################")
           
            noticias = get_terceiro_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  ########################################################")
            print("######################################### SERVIÇO DO TERCEIRO SEMESTRE NÃO ESTÁ FUNCIONANDO ##################################")
            print("##############################################################################################################################")

        if quarto_semestre_is_alive():
            #acessar as noticias do quarto semestre
            print("\n")
            print("#############################################################################################################################")
            print("########################## servicos do quarto semestre disponivel. Grade sendo apresentanda  ################################")
            print("#############################################################################################################################")
           
            noticias = get_quarto_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  ########################################################")
            print("########################################## SERVIÇO DO QUARTO SEMESTRE NÃO ESTÁ FUNCIONANDO ###################################")
            print("##############################################################################################################################")

        if quinto_semestre_is_alive():
            #acessar as noticias do quinto semestre
            print("\n")
            print("#############################################################################################################################")
            print("########################## servicos do quinto semestre disponivel. Grade sendo apresentanda  ################################")
            print("#############################################################################################################################")
           
            noticias = get_quinto_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  ########################################################")
            print("########################################## SERVIÇO DO QUINTO SEMESTRE NÃO ESTÁ FUNCIONANDO ###################################")
            print("##############################################################################################################################")

        if sexto_semestre_is_alive():
            #acessar as noticias do sexto semestre
            print("\n")
            print("#############################################################################################################################")
            print("############################ servicos do sexto semestre disponivel. Grade sendo apresentanda  ###############################")
            print("#############################################################################################################################")
           
            noticias = get_sexto_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  ########################################################")
            print("########################################## SERVIÇO DO SEXTO SEMESTRE NÃO ESTÁ FUNCIONANDO ####################################")
            print("##############################################################################################################################")

        if setimo_semestre_is_alive():
            #acessar as noticias do setimo semestre
            print("\n")
            print("#############################################################################################################################")
            print("########################## servicos do setimo semestre disponivel. Grade sendo apresentanda  ################################")
            print("#############################################################################################################################")
           
            noticias = get_setimo_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("############################################################  ALERTA  ########################################################")
            print("######################################### SERVIÇO DO SÉTIMO SEMESTRE NÃO ESTÁ FUNCIONANDO ####################################")
            print("##############################################################################################################################")

        if oitavo_semestre_is_alive():
            #acessar as noticias do primeiro semestre
            print("\n")
            print("#############################################################################################################################")
            print("########################## servicos do oitavo semestre disponivel. Grade sendo apresentanda  ################################")
            print("#############################################################################################################################")
            
            noticias = get_oitavo_semestre()
            imprimir(" ", noticias)
        else:
            print("\n")
            print("##########################################################  ALERTA  ##########################################################")
            print("####################################### SERVIÇO DO OITAVO SEMESTRE NÃO ESTÁ FUNCIONANDO ######################################")
            print("##############################################################################################################################")

        time.sleep(5)
        
    

