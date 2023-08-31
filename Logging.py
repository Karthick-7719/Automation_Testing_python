import logging

logging.basicConfig(filename='app_log.log', level=logging.INFO, format='%(acstime)s - %(levelname)s - %(message)s')


def login(username, password):
    if username == 'user' and password == 'pass123':
        logging.info(f"Successful login: {username}")
        return True
    else:
        logging.info(f"Failed login: {username}")
        return False


username = "user"
password = "pass"

if login(username, password):
    print("Login successful")
else:
    print("Login Failed")
