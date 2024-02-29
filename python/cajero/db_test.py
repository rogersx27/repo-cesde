from db_atm import AtmManager

db_file = r"python/cajero/db/test.db"

db_manager = AtmManager(db_file)

data = (2, "Diana", "testDiana123", "diana@gmail.com")

db_manager.insert_data_user(data)

df = db_manager.select_all_data_user()
print(df)