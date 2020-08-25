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


