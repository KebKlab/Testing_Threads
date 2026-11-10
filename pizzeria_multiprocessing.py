from concurrent.futures import ProcessPoolExecutor
import threading, queue
import timeit, time
import random
from math import sqrt

SENTINELA_CHEF = object()
SENTINELA_ENTREGADOR = object()
TAMANHO_NUMERO = 10**14
QUANTIDADE_FORNOS = 3
MAX_PEDIDOS = 30
NUMERO_PEDIDOS = 50
NUMERO_THREADS = 16

pedidos = queue.Queue(maxsize=MAX_PEDIDOS)
pizzas_prontas = queue.Queue()
chefs_finalizaram = threading.Event()
executor = ProcessPoolExecutor(max_workers=QUANTIDADE_FORNOS)

def eh_primo(x):
    if x < 2:
        return 0
    if x == 2:
        return x
    if x % 2 == 0:
        return 0
    limit = int(sqrt(x)) + 1
    for i in range (3, limit, 2):
        if x % i == 0:
            return 0
    return x


class Chef(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id

    def gerar_numero(self):
        pizza = random.randrange(0,10**5) + TAMANHO_NUMERO
        return pizza

    def pegarPedido(self):
        pedido = pedidos.get()
        if pedido is not SENTINELA_CHEF:
            print(f"Chef {self.id} pegou o pedido de número {pedido.id}")
        return pedido
    
    def run(self):
        while True:
            pedido = self.pegarPedido()
            if pedido is SENTINELA_CHEF:
                pedidos.task_done()
                break
            else:
                primo = 0
                forno.requisitar_forno(self.id)
                while primo == 0:
                    pizza = self.gerar_numero()
                    resultado = executor.submit(eh_primo, pizza)
                    primo = resultado.result()
                forno.liberar_forno(self.id)
                print(f"Chef {self.id} terminou a pizza {pizza}")
                pizzas_prontas.put(pizza)
                pedidos.task_done()

    
class Entregador(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id
        
    def run(self):
        chefs_finalizaram.wait()
        while True:
            entrega = pizzas_prontas.get()
            if entrega is SENTINELA_ENTREGADOR:
                pizzas_prontas.task_done()
                print(f"Entregador {self.id} encerrou suas entregas")
                break
            else:
                print(f"Pizza numero {entrega} entregue com sucesso")
                pizzas_prontas.task_done()

class Forno:
    def __init__(self, QUANTIDADE_FORNOS):
        self.forno = threading.Semaphore(QUANTIDADE_FORNOS)

    def requisitar_forno(self, chef_id):
        print(f"Chef {chef_id} requisitou o forno")
        self.forno.acquire()

    def liberar_forno(self, chef_id):
        self.forno.release()
        print(f"Chef {chef_id} liberou o forno")

class Pedido:
    def __init__(self,id):
        self.id = id

def GeradorPedidos():
    for i in range(1, NUMERO_PEDIDOS + 1):
        pedido = Pedido(i)
        pedidos.put(pedido)
        #print(f"Gerador de pedidos criou o pedido: {pedido.id}")
    for i in range(NUMERO_THREADS):
        pedidos.put(SENTINELA_CHEF)

if __name__ == '__main__':
    chefs = []
    entregadores = []

    for c in range(NUMERO_THREADS):
        chef =  Chef(c + 1)
        chefs.append(chef)

    for en in range(NUMERO_THREADS):
        entregador = Entregador(en+1)
        entregadores.append(entregador)
    
    forno = Forno(QUANTIDADE_FORNOS)

    inicio = timeit.default_timer()

    thread_gerador = threading.Thread(target=GeradorPedidos)

    for chef in chefs:
        chef.start()


    for entregador in entregadores:
        entregador.start()

    thread_gerador.start()

    pedidos.join()
    for chef in chefs:
        chef.join()

    executor.shutdown(wait=True)

    chefs_finalizaram.set()

    print("Todos os pedidos foram preparados com sucesso")

    for i in range(NUMERO_THREADS):
        pizzas_prontas.put(SENTINELA_ENTREGADOR)

    pizzas_prontas.join()

    for entregador in entregadores:
        entregador.join()

    print("Todos os pedidos foram entregues com sucesso")

    fim = timeit.default_timer()

    print(f"Tempo de execução: {fim - inicio}")