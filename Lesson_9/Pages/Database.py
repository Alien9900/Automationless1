from sqlalchemy import create_engine, text

class DataBase:
    query = {
        'create_company': text('insert into company (name, description) values (:name, :description)'),
        'max_company_id': text('select MAX(id) from company'),
        'delete_company': text('delete from company where id = :company_id'),
        'list_SELECT': text('select * from employee where company_id = :id'),
        'item_SELECT': text('select * from employee where company_id = :c_id and id = :e_id'),
        'maxID_SELECT': text('select MAX(id) from employee where company_id = :c_id'),
        'item_DELETE': text('delete from employee where id = :id_delete'),
        'item_UPDATE': text('update employee set first_name = :new_name where id = :employer_id'),
        'item_INSERT': text('insert into employee(company_id, first_name, last_name, phone) values(:id, :name, :surname, :phone_num)')
    }

    def __init__(self, engine) -> None:
        self.db = create_engine(engine)

    def create_company(self, company_name: str, description: str):
        with self.db.connect() as connection:
            connection.execute(
            self.query['create_company'],
            parameters=dict(name=company_name, description=description)
        )
        connection.commit()
        connection.close()
        print("[INFO] Company created successfully")

    def delete(self, company_id: int):
        with self.db.connect() as connection:
           connection.execute(self.query['delete_company'], parameters=dict(company_id=company_id))
           connection.commit()
           connection.close()
        print("[INFO] DB connection closed")

    def last_company_id(self):
        with self.db.connect() as connection:
            connection.execute(self.query['max_company_id']).fetchall()[0][0]
            connection.commit()
            connection.close()
        print("[INFO] DB connection closed")

    def get_list_employer(self, company_id: int):
        with self.db.connect() as connection:
            connection.execute(self.query['list_SELECT'], parameters=dict(id=company_id))
            connection.commit()
            connection.close()
        print("[INFO] DB connection closed")

    def create_employer(self, company_id: int, first_name: str, last_name: str, phone: str):
        with self.db.connect() as connection:
            connection.execute(self.query['item_INSERT'], parameters=dict(id=company_id, name=first_name, surname=last_name, phone_num=phone))
            connection.commit()
            connection.close()       
        print("[INFO] DB connection closed")

    def get_employer_id(self, company_id: int):
        with self.db.connect() as connection:
            connection.execute(self.query['maxID_SELECT'], parameters=dict(c_id=company_id))[0]
            connection.commit()
            connection.close()
        print("[INFO] DB connection closed")    


    def update_employer_info(self, new_name: str, id: int):
        with self.db.connect() as connection:
            connection.execute(self.query['item_UPDATE'], parameters=dict(new_name=new_name, employer_id=id))
            connection.commit()
            connection.close()
        print("[INFO] DB connection closed")

    def delete_employer(self, id: int):
        with self.db.connect() as connection:
            connection.execute(self.query['item_DELETE'], parameters=dict(id_delete=id))
            connection.commit()
            connection.close()
        print("[INFO] DB connection closed")

        
            

