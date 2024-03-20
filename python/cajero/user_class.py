
class User:
    '''
    Clase usuario
    '''
    def __init__(self, atm_manager, id_user, name, last_name, email, password, balance=0):
        self.atm_manager = atm_manager
        self.id_user = id_user
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.balance = balance

    def __str__(self):
        return f"User(id_user={self.id_user}, name={self.name}, last_name={self.last_name}, email={self.email}, balance={self.balance})"

    def get_data_base_balance(self):
        from db_atm import AtmManager
        db_manager = AtmManager()
        data = db_manager.select_user_by_id(
            self.id_user).get("balance").values[0]
        db_manager.close_connection()
        return data

    def get_data_base_password(self):
        from db_atm import AtmManager
        db_manager = AtmManager()
        data = db_manager.select_user_by_id(
            self.id_user).get("password").values[0]
        db_manager.close_connection()
        return data

    def set_balance(self, balance: float):
        self.balance = balance

    def set_password(self, password: int):
        self.password = password

    def do_deposit(self, value: float, text: str):
        from db_atm import AtmManager
        db_manager = AtmManager()

        deposit = 'deposit'
        save = db_manager.read_data_transactions(
            id_user=self.id_user, details=text, amount=value, type_transaction=deposit)
        if save:
            db_manager.update_balance_user(self.id_user, value)
            new_balance = self.get_data_base_balance()
            self.set_balance(new_balance)
            db_manager.close_connection()
            return True

    def consult_deposits(self):
        from db_atm import AtmManager
        db_manager = AtmManager()

        data = db_manager.select_all_transactions_from_user(self.id_user)

        table_data = [
            [
                data['type_transaction'].values[i],
                data['details'].values[i],
                data['amount'].values[i],
                data['date'].values[i]
            ] for i in range(len(data))
        ]
        db_manager.close_connection()
        return table_data

    def do_withdraw(self, value: float, text: str):
        from db_atm import AtmManager
        db_manager = AtmManager()

        withdraw = 'withdraw'
        save = db_manager.read_data_transactions(
            id_user=self.id_user, details=text, amount=value, type_transaction=withdraw)
        if save:
            db_manager.update_balance_user(
                self.id_user, value, to_withdraw=True)
            new_balance = self.get_data_base_balance()
            self.set_balance(new_balance)
            db_manager.close_connection()
            return True

    def change_password(self, password: int):
        from db_atm import AtmManager
        db_manager = AtmManager()
        db_manager.update_password_user(self.id_user, password)
        new_password = self.get_data_base_password()
        self.set_password(new_password)
        db_manager.close_connection()
        return True
