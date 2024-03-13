import requests
import pickle
import os
import ctypes
from datetime import datetime
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()
DEFAULT_URL = 'http://192.168.1.147:5001/variables'

# Messages for error and status
INVALID_CREDENTIALS_MESSAGE = "Error of Credentials/License"
UNAVAILABLE_MESSAGE = "unavailable"

def create_directories():
    try:
        os.makedirs('C:/Tekinova/license', exist_ok=True)
        os.makedirs('C:/Tekinova/data/tmp', exist_ok=True)
        ctypes.windll.kernel32.SetFileAttributesW('C:/Tekinova', 2)
    except Exception:
        print('Not created')

create_directories()

# Function to retrieve the value of a variable through an API
def get_variable_from_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()  # Assuming the response is in JSON format
        else:
            pass
    except requests.RequestException:
        pass

# Function to load data from a pickle file
def load_data_from_pickle(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        pass
    except pickle.UnpicklingError:
        pass

# Function to save data to a pickle file
def save_data_to_pickle(data, filename):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    except Exception:
        pass

def get_server_ep():
    try:
        response = get_variable_from_api(DEFAULT_URL)
        SERVER_ENDPOINT = response['SERVER_ENDPOINT']
        save_data_to_pickle(SERVER_ENDPOINT, "c:/temp/endpoint.pickle")
        print('From WEB')          
    except Exception or requests.exceptions or ConnectionError or TimeoutError or FileNotFoundError:
        SERVER_ENDPOINT = load_data_from_pickle("c:/temp/endpoint.pickle")
        print('From PICKLE')
    if SERVER_ENDPOINT is None:
        SERVER_ENDPOINT = 'http://192.168.1.147:5001'
        print('From TXT')
    
    save_data_to_pickle(SERVER_ENDPOINT, "c:/temp/endpoint.pickle")
    return SERVER_ENDPOINT

def get_license():
    try:
        # Retrieve the value of LICENSE_FILE from the API
        response = get_variable_from_api(f"{get_server_ep()}/variables")
        LICENSE_FILE = response['LICENSE_FILE']
        if LICENSE_FILE is None:
            # Try to load the value from the pickle file if available
            LICENSE_FILE = load_data_from_pickle("c:/temp/license.pickle")
            return LICENSE_FILE
        else:
            # Save the value of LICENSE_FILE to a pickle file for future use
            save_data_to_pickle(LICENSE_FILE, "c:/temp/license.pickle")
            return LICENSE_FILE
    except Exception or requests.exceptions or ConnectionError or TimeoutError or FileNotFoundError:
        LICENSE_FILE = load_data_from_pickle("c:/temp/license.pickle")
        return LICENSE_FILE

def get_key():
    try:
        # The same process should be repeated for the KEY_FILENAME variable
        response = get_variable_from_api(f"{get_server_ep()}/variables")
        KEY_FILENAME = response['KEY_FILENAME']
        if KEY_FILENAME is None:
            # Try to load the value from the pickle file if available
            KEY_FILENAME = load_data_from_pickle("c:/temp/key.pickle")
            return KEY_FILENAME
        else:
            # Save the value of KEY_FILENAME to a pickle file for future use
            save_data_to_pickle(KEY_FILENAME, "c:/temp/key.pickle")
            return KEY_FILENAME
    except Exception or requests.exceptions or ConnectionError or TimeoutError or FileNotFoundError:
        KEY_FILENAME = load_data_from_pickle("c:/temp/key.pickle")
        return KEY_FILENAME

def license_pending():
    """
    Return status for pending license.
    """
    return "ready"

def license_used():
    """
    Return status for used license.
    """
    return "used"

def license_expired():
    """
    Return status for expired license.
    """
    return "expired"

def verification_error(status):
    """
    Return status for verification error.

    Parameters:
    status (str): The status of the verification error.

    Returns:
    str: The status of the verification error.
    """
    return status

def activation_success():
    """
    Return status for successful license activation.
    """
    return "activated"

def activation_error():
    """
    Return status for license activation error.
    """
    return "activation_error"

def invalid_credentials():
    """
    Return status for invalid credentials.
    """
    return 'unverified'

def generate_key():
    """
    Generate a new encryption key.

    Returns:
    bytes: The generated encryption key.
    """
    return Fernet.generate_key()

def save_key(key):
    """
    Save the encryption key to a file.

    Parameters:
    key (bytes): The encryption key to save.
    """
    with open(get_key(), 'wb') as f:
        f.write(key)

def load_key():
    """
    Load the encryption key from a file.

    Returns:
    bytes: The loaded encryption key.
    """
    if not os.path.exists(get_key()):
        key = generate_key()
        save_key(key)
        set_file_permissions(get_key())
    with open(get_key(), 'rb') as f:
        key = f.read()
    return key

def set_file_permissions(filename):
    """
    Set permissions for a file to read and write for the owner only.

    Parameters:
    filename (str): The name of the file.
    """
    os.chmod(filename, 0o600)

def encrypt_expiry_date(expiry_date, key):
    """
    Encrypt the expiry date using Fernet symmetric encryption.

    Parameters:
    expiry_date (str): The expiry date to encrypt.
    key (bytes): The encryption key.

    Returns:
    bytes: The encrypted expiry date.
    """
    cipher_suite = Fernet(key)
    encrypted_expiry_date = cipher_suite.encrypt(expiry_date.encode())
    return encrypted_expiry_date

def decrypt_expiry_date(encrypted_expiry_date, key):
    """
    Decrypt the expiry date using Fernet symmetric encryption.

    Parameters:
    encrypted_expiry_date (bytes): The encrypted expiry date.
    key (bytes): The encryption key.

    Returns:
    str: The decrypted expiry date.
    """
    cipher_suite = Fernet(key)
    decrypted_expiry_date = cipher_suite.decrypt(encrypted_expiry_date).decode()
    return decrypted_expiry_date

def load_license_expiry():
    """
    Load the license expiry date from the license file.

    Returns:
    str: The loaded expiry date.
    """
    try:
        with open(get_license(), 'rb') as f:
            encrypted_expiry_date = pickle.load(f)
            key = load_key()
            text = decrypt_expiry_date(encrypted_expiry_date, key)
            year = int(text[0:4])
            month = int(text[5:7].lstrip('0'))
            day = int(text[8:10].lstrip('0'))
            expiry_date = datetime(year, month, day)
            expiry_date = expiry_date.date()
            return expiry_date
    except FileNotFoundError:
        return "License file not found"
    except pickle.UnpicklingError:
        return 'License file not found'

def save_license_expiry(expiry_date):
    """
    Save the license expiry date to the license file.

    Parameters:
    expiry_date (str): The expiry date to save.
    """
    try:
        expiry_date_str = expiry_date
        key = load_key()
        encrypted_expiry_date = encrypt_expiry_date(expiry_date_str, key)
        with open(get_license(), 'wb') as f:
            pickle.dump(encrypted_expiry_date, f)
    except Exception as e:
        raise RuntimeError("Error saving license expiry:", e)

def verify_license(key, customer, customer_pass):
    """
    Verify the license with the server.

    Parameters:
    key (str): The license key to verify.
    customer (str): The customer's email.
    customer_pass (str): The customer's password.

    Returns:
    str: The status of the license verification.
    """
    try:
        url = f"{get_server_ep()}/verify"
        data = {'chave': key, 'email': customer, 'senha': customer_pass}
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            resposta = response.json()
            if resposta['status'] == 'pending':
                return license_pending()
            elif resposta['status'] == 'used':
                return license_used()
            elif resposta['status'] == 'expired':
                return license_expired()
            elif resposta['status'] == INVALID_CREDENTIALS_MESSAGE:
                return invalid_credentials()
            else:
                return resposta['status']
        else:
            return UNAVAILABLE_MESSAGE
        
    except requests.ConnectionError:
        return UNAVAILABLE_MESSAGE

def activate_license(key, customer, customer_pass):
    """
    Activate the license with the server.

    Parameters:
    key (str): The license key to activate.
    customer (str): The customer's email.
    customer_pass (str): The customer's password.

    Returns:
    str: The status of the license activation.
    """
    url = f"{get_server_ep()}/activate"
    data = {'chave': key, 'email': customer, 'senha': customer_pass}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        resposta = response.json()
        if resposta['status'] == 'Ativação bem-sucedida':
            new_expiry_date = resposta['data_validade']
            save_license_expiry(new_expiry_date)
            return activation_success()
        else:
            return activation_error()
    else:
        return UNAVAILABLE_MESSAGE

def expiry_date():
    """
    Get the license expiry date.

    Returns:
    str: The license expiry date.
    """
    try:
        expiry_date = load_license_expiry()
        return expiry_date
    except FileNotFoundError:
        return "License file not found"
    except pickle.UnpicklingError:
        return 'License file not found'

def violation_fix():
    """
    Fix the license violation by resetting the expiry date to a default value.
    """
    load_key()
    datetm = datetime(year=1800, month=1, day=1, hour=23, minute=59, second=59)
    expiry_date = datetime.date(datetm).strftime('%Y-%m-%d')
    save_license_expiry(expiry_date)

def health_monitor():
    """
    Monitor the health status of the license.

    Returns:
    str: The health status of the license.
    """
    try:
        noted = load_license_expiry()
        return noted
    except FileNotFoundError:
        return "License file not found"
    except pickle.UnpicklingError:
        return 'License file not found'

def target():
    """
    Get the current date.

    Returns:
    datetime.date: The current date.
    """
    return datetime.now().date()

def  license_valid():
    """
    Check if the license is valid.

    Returns:
    bool: True if the license is valid, False otherwise.
    """
    if expiry_date() < target():
        return False
    else:
        return True

get_server_ep()
get_license()
get_key()
