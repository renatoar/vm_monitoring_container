import time
import requests
from pymongo import MongoClient
from datetime import datetime
database = MongoClient('localhost:17017')['vm_monitoring']['metricas']

mins = 0
#URL base
base = "http://192.168.50.10:9090/api/v1/query?query="
#query CPU Usage
URL_cpu = '(1-avg(irate(node_cpu_seconds_total{mode="idle"}[10m]))by(instance))*100'
URL_mem = '(node_memory_MemTotal_bytes-node_memory_MemAvailable_bytes)*100'
URL_tx = 'sum(node_network_receive_bytes_total)by(instance)'
URL_rx = 'sum(node_network_transmit_bytes_total)by(instance)'
while mins != 10:
    r = requests.get(url = base + URL_cpu)
    j = requests.get(url = base + URL_mem)
    p = requests.get(url = base + URL_tx)
    q = requests.get(url = base + URL_rx)
    dados_cpu = r.json()
    dados_mem = j.json()
    dados_nettx = p.json()
    dados_netrx = q.json()
    qtd_nodes = len(dados_mem["data"]["result"])
    for x in range(0, qtd_nodes) :
        timestamp = datetime.fromtimestamp(dados_cpu["data"]["result"][x]["value"][0])
        timestampStr = timestamp.strftime("%d-%b-%Y - %H:%M:%S")
        name_node = dados_cpu["data"]["result"][x]["metric"]["instance"]
        cpu_usage = format(float(dados_cpu["data"]["result"][x]["value"][1]), '.2f') + " %"
        mem_usage = format(float(dados_mem["data"]["result"][x]["value"][1]), '.2f') + " MB"
        byte_tx = dados_nettx["data"]["result"][x]["value"][1] + " Bs"
        byte_rx = dados_netrx["data"]["result"][x]["value"][1] + " Bs"
        
        resposta = client[timestampStr].insert_one({'timestap': timestampStr, 'name_node': name_node, 'cpu_usage': cpu_usage, 'mem_usage' : mem_usage, 'byte_tx': byte_tx, 'byte_rx': byte_rx})
        print(resposta)

    time.sleep(15)
    mins += 1