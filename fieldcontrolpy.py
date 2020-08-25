import requests
import json


class FieldControl:
    def __init__(self, API_KEY):
        self.key = API_KEY
        self.BASE_URL = 'https://carchost.fieldcontrol.com.br/'
        self.TASKS_URL = self.BASE_URL+'tasks/'
        self.ORDER_URL = self.BASE_URL+'orders/'
        self.CLIENT_URL = self.BASE_URL+'customers/'
        self.EMPLOYEES_URL = self.BASE_URL+'employees/'
        self.MATERIALS_URL = self.BASE_URL+'materials'
        self.EQUIPMENTS_URL = self.BASE_URL+'equipments'
        self.TICKETS_URL = self.BASE_URL+'tickets'
        self.SERVICE_ORDER_URL = self.BASE_URL+'orders'
        self.OK_STATUS_CODE = 200
        self.test_connection()
 
    def test_connection(self):
        result = requests.get(self.TASK_URL, headers={'X-Api-Key': self.key})

        if result.status_code != self.OK_STATUS_CODE:
            raise Exception("API key not valid")
#------------------------ CLIENTES ------------------------------------- 

    def get_client(self, client_id):

        request_result = self.__simple_request__(self.CLIENT_URL, id_retrieve=client_id)        
        return request_result

#---------------------------- COLABORADORES ----------------------------------

    def get_employee(self, employee_id):

        request_result = self.__simple_request__(self.EMPLOYEES_URL, id_retrieve=employee_id)
        return request_result

#----------------------------- MATERIAIS -------------------------

    def get_material(self, material_id):
    
        request_result = self.__simple_request__(self.MATERIALS_URL, id_retrieve=material_id)
        return request_result

#--------------------- --------- EQUIPAMENTOS ------------------------

    def get_equipment(self, equipment_id):
    
        request_result = self.__simple_request__(self.EQUIPMENTS_URL, id_retrieve=equipment_id)
        return request_result

#-------------------------------- SOLICITAÇÃO DE SERVIÇOS ------------------------

    def get_ticket(self, ticket_id):
        request_result = self.__simple_request__(url=self.TICKETS_URL, id_retrieve=ticket_id)
        return request_result
    
#--------------------------------ATIVIDADES-------------------------
    def get_task(self, task_id):
            request_result = self.__simple_request__(self.TASKS_URL, task_id)
            return request_result

#----------------------------- SERVICE ORDER ----------------------------

    def get_service_order(self, service_order_id):

            request_result = self.__simple_request__(self.SERVICE_ORDER_URL, service_order_id)
            return request_result

#------------------------ INNER FUNCTIONS --------------------------

    def __simple_request__(self, url, id_retrieve):

        request_result = requests.get(f'{url}{id_retrieve}',
        headers={'X-Api-Key': self.key})
        if request_result.status_code != 200:
            raise Exception("ID not valid")
        return request_result.json()
        
  
# false=False
# true=True
# null=None



# print(client)
#REQUEST QUE PEGA AS ATIVIDADES
# response_t = requests.get(TASK_URL+'?q=created_at>=:"2020-08-17"&status:"done"', headers={'X-Api-Key': API_KEY})

#REQUEST QUE PEGA O ID DO CLIENTE
# response_t = requests.get(ORDER_URL+"NDUyZjkxNWUtZjJiNy00ZDU2LTg0NGItNDA5MDM4ZmMwNjc0OjE5NTY3",
#     headers={'X-Api-Key': API_KEY})

#REQUEST COM O ID DO CLIENTE PRA

# response_t = requests.get(CLIENT_URL+"NDE2OTY2OjE5NTY3",
#     headers={'X-Api-Key': API_KEY})

# client_get = requests.get(BASE_URL+'/customers/:"MTM5ODI6MTk1Njc="',
# headers={'X-Api-Key': API_KEY})
# print(client_get.status_code)
# test = eval(client_get.text)
# print(test)
# for _ in test['items']:
#     print('--------------ITEM---------------')
#     print(_)
#-------------------------------
# response_dict = eval(response_t.text)

# # print(response_dict)
# for item in response_dict:
#     print('----------------item------------')
#     print(item)
'''
{'id': 'MDQ3ZTQ5NjUtMjg1YS00ZjgyLTllN2ItZDQ1OTYzYmFhZmQxOjE5NTY3', 'duration': 30, 'position': 100, 'status': 'scheduled', 'startedAt': None, 'completedAt': None, 'statusDescription': None, 'archived': False, 'createdAt': '2020-07-28T14:00:13Z', 'employee': {'id': 'MTM5ODI6MTk1Njc='}, 'order': {'id': 'ZDIwZDg4NjItMjBhOS00MjMyLWI5MzEtOWNmNjZjZGMwOWQzOjE5NTY3'}, 'scheduling': {'type': 'scheduled-date-and-time', 'date': '2020-08-19', 'time': '10:40:00'}, 'coords': {'latitude': -22.998759, 'longitude': -43.351201}}
'''
'''
{"items":
[
    {"id":"MDY1YzI1YTYtNDU4OC00YjJmLWEzMWMtODYyMzhhZmE1M2QxOjE5NTY3","duration":120,"position":100,"status":"scheduled","startedAt":null,"completedAt":null,"statusDescription":null,"viewedAt":null,"receivedAt":"2020-08-17T10:51:37Z","archived":false,"createdAt":"2020-08-17T10:29:56Z","employee":{"id":"MTM4MjI6MTk1Njc="},"order":{"id":"NDljYTViZmQtYmVhNC00MmRhLWIxM2EtMjc0MDg0NmZkZmZlOjE5NTY3"},"scheduling":{"type":"scheduled-date-and-time","date":"2020-08-17","time":"06:00:00"},"coords":{"latitude":-23.004394,"longitude":-43.325724}},
    {"id":"NjFmNDJhMjYtYTZjOS00ZTI1LTljNWUtYTUyYjdkNDFhMWNkOjE5NTY3","duration":120,"position":100,"status":"done","startedAt":"2020-08-17T10:00:00.000Z","completedAt":"2020-08-17T10:59:19.000Z","statusDescription":"Feito a limpeza na ETE do Barra prime. A bomba não estava ativando, por causa da grande quantidade de gordura dentro da caixa. \nA limpeza desta caixa é complicada para fazer, pois a existe um tubo no meio dela, que não conseguimos ter acesso para a  limpeza. O ideal, seríamos limpa lá, entre uma a duas vezes por mês. As duas bombas estavam encrostadas pela gordura acumulada na caixa. Retiramos quatro sacos
    com grande quantidade de gordura petrificada; foram retirados 200kg.\nSistema fluindo normalmente.\nequipe: Hugo e Severino ","viewedAt":"2020-08-17T10:51:40Z","receivedAt":"2020-08-17T10:51:37Z","archived":false,"createdAt":"2020-08-17T09:45:53Z","employee":{"id":"MTM4MjI6MTk1Njc="},"order":{"id":"NDUyZjkxNWUtZjJiNy00ZDU2LTg0NGItNDA5MDM4ZmMwNjc0OjE5NTY3"},"scheduling":{"type":"scheduled-date-and-time","date":"2020-08-17","time":"06:00:00"},"coords":{"latitude":-23.004394,"longitude":-43.325724}},
    {"id":"ZDk3MTI5ZjctODA5Yy00ODczLTg5ZDAtYTgwNTc5ZWExYzY1OjE5NTY3","duration":60,"position":100,"status":"scheduled","startedAt":null,"completedAt":null,"statusDescription":null,"viewedAt":null,"receivedAt":null,"archived":false,"createdAt":"2020-08-17T06:45:45Z","employee":{"id":"MjA1MTY6MTk1Njc="},"order":{"id":"ZGY2ZmE1ZjUtYWVhZS00Y2VlLWIwNTEtNWVmNTM5YTY5ZDBjOjE5NTY3"},"scheduling":{"type":"scheduled-date-and-time","date":"2020-09-16","time":"08:00:00"},"coords":{"latitude":-23.004394,"longitude":-43.325724}}
],
"totalCount":3}
'''