import configparser


def crud_config(path):
    config = configparser.ConfigParser()
    config.read(path)

    login = config.get("db", "login")
    password = config.get("db", "password")
    print(login, password)


crud_config("config.ini")