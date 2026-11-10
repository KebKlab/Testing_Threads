import threading, queue
import timeit, time
import random
from math import sqrt

SENTINELA_CHEF = object()
SENTINELA_ENTREGADOR = object()
TAMANHO_NUMERO = 10**14
QUANTIDADE_FORNOS = 6
MAX_PEDIDOS = 30
NUMERO_PEDIDOS = 50
NUMERO_THREADS = 16
pedidos = queue.Queue(maxsize=MAX_PEDIDOS)
pizzas_prontas = queue.Queue()
chefs_finalizaram = threading.Event()

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


class Chef:
    def __init__(self,id):
        self.id = id

    def gerar_numero(self):
        pizza = random.randrange(0,10**5) + TAMANHO_NUMERO
        return pizza

    def pegarPedido(self):
        pedido = pedidos.get()
        if pedido is not SENTINELA_CHEF:
            print(f"Chef {self.id} pegou o pedido de número {pedido.id}")
        return pedido
    
    def trabalhar(self):
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
                    primo = eh_primo(pizza)
                forno.liberar_forno(self.id)
                print(f"Chef {self.id} terminou a pizza {pizza}")
                pizzas_prontas.put(pizza)
                pedidos.task_done()

    
class Entregador:
    def __init__(self,id):
        self.id = id
        
    def entregarPizza(self):
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
        i = Pedido(i)
        pedidos.put(i)
        #print(f"Gerador de pedidos criou o pedido: {pedido.id}")
    for i in range(NUMERO_THREADS):
        pedidos.put(SENTINELA_CHEF)

chef1 = Chef(1);
chef2 = Chef(2);
chef3 = Chef(3);
chef4 = Chef(4);
chef5 = Chef(5);
chef6 = Chef(6);
chef7 = Chef(7);
chef8 = Chef(8);
chef9 = Chef(9);
chef10 = Chef(10);
chef11 = Chef(11);
chef12 = Chef(12);
chef13 = Chef(13);
chef14 = Chef(14);
chef15 = Chef(15);
chef16 = Chef(16);

entregador1 = Entregador(1);
entregador2 = Entregador(2);
entregador3 = Entregador(3);
entregador4 = Entregador(4);
entregador5 = Entregador(5);
entregador6 = Entregador(6);
entregador7 = Entregador(7);
entregador8 = Entregador(8);
entregador9 = Entregador(9);
entregador10 = Entregador(10);
entregador11 = Entregador(11);
entregador12 = Entregador(12);
entregador13 = Entregador(13);
entregador14 = Entregador(14);
entregador15 = Entregador(15);
entregador16 = Entregador(16);

forno = Forno(QUANTIDADE_FORNOS)

inicio = timeit.default_timer()

thread_gerador = threading.Thread(target=GeradorPedidos)

thread_chef1 = threading.Thread(target=chef1.trabalhar)
thread_chef2 = threading.Thread(target=chef2.trabalhar)
thread_chef3 = threading.Thread(target=chef3.trabalhar)
thread_chef4 = threading.Thread(target=chef4.trabalhar)
thread_chef5 = threading.Thread(target=chef5.trabalhar)
thread_chef6 = threading.Thread(target=chef6.trabalhar)
thread_chef7 = threading.Thread(target=chef7.trabalhar)
thread_chef8 = threading.Thread(target=chef8.trabalhar)
thread_chef9 = threading.Thread(target=chef9.trabalhar)
thread_chef10 = threading.Thread(target=chef10.trabalhar)
thread_chef11 = threading.Thread(target=chef11.trabalhar)
thread_chef12 = threading.Thread(target=chef12.trabalhar)
thread_chef13 = threading.Thread(target=chef13.trabalhar)
thread_chef14 = threading.Thread(target=chef14.trabalhar)
thread_chef15 = threading.Thread(target=chef15.trabalhar)
thread_chef16 = threading.Thread(target=chef16.trabalhar)


thread_entregador1 = threading.Thread(target=entregador1.entregarPizza)
thread_entregador2 = threading.Thread(target=entregador2.entregarPizza)
thread_entregador3 = threading.Thread(target=entregador3.entregarPizza)
thread_entregador4 = threading.Thread(target=entregador4.entregarPizza)
thread_entregador5 = threading.Thread(target=entregador5.entregarPizza)
thread_entregador6 = threading.Thread(target=entregador6.entregarPizza)
thread_entregador7 = threading.Thread(target=entregador7.entregarPizza)
thread_entregador8 = threading.Thread(target=entregador8.entregarPizza)
thread_entregador9 = threading.Thread(target=entregador9.entregarPizza)
thread_entregador10 = threading.Thread(target=entregador10.entregarPizza)
thread_entregador11 = threading.Thread(target=entregador11.entregarPizza)
thread_entregador12 = threading.Thread(target=entregador12.entregarPizza)
thread_entregador13 = threading.Thread(target=entregador13.entregarPizza)
thread_entregador14 = threading.Thread(target=entregador14.entregarPizza)
thread_entregador15 = threading.Thread(target=entregador15.entregarPizza)
thread_entregador16 = threading.Thread(target=entregador16.entregarPizza)


thread_gerador.start()

thread_chef1.start()
thread_chef2.start()
thread_chef3.start()
thread_chef4.start()
thread_chef5.start()
thread_chef6.start()
thread_chef7.start()
thread_chef8.start()
thread_chef9.start()
thread_chef10.start()
thread_chef11.start()
thread_chef12.start()
thread_chef13.start()
thread_chef14.start()
thread_chef15.start()
thread_chef16.start()


thread_entregador1.start()
thread_entregador2.start()
thread_entregador3.start()
thread_entregador4.start()
thread_entregador5.start()
thread_entregador6.start()
thread_entregador7.start()
thread_entregador8.start()
thread_entregador9.start()
thread_entregador10.start()
thread_entregador11.start()
thread_entregador12.start()
thread_entregador13.start()
thread_entregador14.start()
thread_entregador15.start()
thread_entregador16.start()

pedidos.join()

thread_chef1.join()
thread_chef2.join()
thread_chef3.join()
thread_chef4.join()
thread_chef5.join()
thread_chef6.join()
thread_chef7.join()
thread_chef8.join()
thread_chef9.join()
thread_chef10.join()
thread_chef11.join()
thread_chef12.join()
thread_chef13.join()
thread_chef14.join()
thread_chef15.join()
thread_chef16.join()

chefs_finalizaram.set()

print("Todos os pedidos foram preparados com sucesso")

for i in range(NUMERO_THREADS):
    pizzas_prontas.put(SENTINELA_ENTREGADOR)

pizzas_prontas.join()

thread_entregador1.join()
thread_entregador2.join()
thread_entregador3.join()
thread_entregador4.join()
thread_entregador5.join()
thread_entregador6.join()
thread_entregador7.join()
thread_entregador8.join()
thread_entregador9.join()
thread_entregador10.join()
thread_entregador11.join()
thread_entregador12.join()
thread_entregador13.join()
thread_entregador14.join()
thread_entregador15.join()
thread_entregador16.join()

print("Todos os pedidos foram entregues com sucesso")

fim = timeit.default_timer();

print(f"Tempo de execução: {fim - inicio}")