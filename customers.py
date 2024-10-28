from typing import List


class Customers:
    _customers:List[dict]

    def __init__(self,customers:List[dict]) -> None:
        super().__init__()
        self._customers = []
        self.customers = customers

    @property
    def customers(self):
        return self._customers
    
    @customers.setter
    def customers(self,new_customers):
        for new in new_customers:
            match new:
                case {'cliente_id':int(id_),'nome':str(nome),'email':str(email)} if '@' in email:
                    self._customers.append(new)
                case _:
                    raise ValueError(
                        f"""Invalid customer record: {new!r}. Expected [{{'cliente_id':int(id_),'nome':str(nome),'email':str(email)}},...]"""
                    )

    def __repr__(self) -> str:
        return f'Customers({self.customers!r})'

    def __getitem__(self,key):
        return self.customers[key]
    
    def map_ids_and_names(self):
        return {customer['cliente_id']:customer['nome'] for customer in self.customers}
    
    def add_more_info_customer(self,customer_id:int,info_map):
        for customer in self.customers:
            if customer['cliente_id'] == customer_id:
                customer |= info_map
                print(f'Customer: {customer}')
        


if __name__=='__main__':
    # Alimentando a classe com uma lista de clientes
    customers= Customers([
        {"cliente_id": 1, "nome": "Alice", "email": "alice@example.com"},
        {"cliente_id": 2, "nome": "Bob", "email": "bob@example.com"},
    ])

    # Exibindo a representação da classe
    print(customers)

    # Exibindo o novo dicionario criando usando dictcomps para mapear o id:nome
    print(customers.map_ids_and_names())

    # Atualizando o cliente de id 1 com mais informações usando o operador |=
    customers.add_more_info_customer(1,{'phone':'5565123456789'})
    
    # Exibindo a representação da classe atualizada
    print(customers)
    