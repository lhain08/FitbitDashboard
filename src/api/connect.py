"""Connect Module for establishing API authorization"""
import fitbit
from .get_keys import OAuth2Server

def read_id_and_secret():
    """Reads in credentials from file if exists"""
    try:
        with open('api/credentials.txt', 'r', encoding="utf-8") as creds:
            client_id = creds.readline().strip()
            client_secret = creds.readline().strip()
    except Exception as error:
        print("ERROR: credentials.txt does not exist or has invalid format")
        print("\tShould contain CLIENT_ID and CLIENT_SECRET on first and second lines respectively")
        raise Exception("Bad File") from error
    return client_id, client_secret

def read_tokens():
    """reads in tokens from file if they exist"""
    try:
        with open('api/tokens.txt', 'r', encoding="utf-8") as tokens:
            access = tokens.readline().strip()
            refresh = tokens.readline().strip()
        return access, refresh
    except:
        raise Exception("Tokens do not exist")

def write_tokens(access, refresh):
    """Caches the tokens to a file"""
    with open('api/tokens.txt', 'w', encoding="utf-8") as file:
        file.write(access + "\n" + refresh)

def get_client():
    """Establishes authorization for the Fitbit API"""
    try:
        client_id, client_secret = read_id_and_secret()
    except:
        raise Exception("Could not find or read client id and secret")

    # Try to open cached tokens
    try:
        access_token, refresh_token = read_tokens()
    except:
        # Create server and wait to run browser authorization
        try:
            server = OAuth2Server(client_id, client_secret, my_uri="http://0.0.0.0:8080", \
                                         redirect_uri="http://127.0.0.1:8080/authorize")
            server.start()
        except:
            raise Exception("Authorization Failed")
        # Get tokens and client
        access_token = str(server.fitbit.client.session.token['access_token'])
        refresh_token = str(server.fitbit.client.session.token['refresh_token'])
        write_tokens(access_token, refresh_token)

    client = fitbit.Fitbit(client_id, client_secret, oauth2=True,
                           access_token=access_token, refresh_token=refresh_token,
                           redirect_uri="http://127.0.0.1:8080/authorize")

    return client
