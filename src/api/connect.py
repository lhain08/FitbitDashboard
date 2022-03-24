from .get_keys import OAuth2Server
import fitbit

def read_id_and_secret():
    try:
        creds = open('api/credentials.txt', 'r')
        CLIENT_ID = creds.readline().strip()
        CLIENT_SECRET = creds.readline().strip()
        creds.close()
    except:
        print("ERROR: credentials.txt does not exist or has invalid format")
        print("\tShould contain CLIENT_ID and CLIENT_SECRET on first and second lines respectively")
        raise Exception("Bad File")
    return CLIENT_ID, CLIENT_SECRET

def read_tokens():
    try:
        tokens = open('api/tokens.txt', 'r')
        access = tokens.readline().strip()
        refresh = tokens.readline().strip()
        tokens.close()
        return access, refresh
    except:
        raise Exception("Tokens do not exist")

def write_tokens(access, refresh):
    f = open('api/tokens.txt', 'w')
    f.write(access + "\n" + refresh)
    f.close()

def get_client():
    # Attempt to read in id and secret
    try:
        CLIENT_ID, CLIENT_SECRET = read_id_and_secret()
    except:
        raise Exception("Could not find or read client id and secret")

    # Try to open cached tokens
    try:
        ACCESS_TOKEN, REFRESH_TOKEN = read_tokens()
    except:
        # Create server and wait to run browser authorization
        try:
            server = OAuth2Server(CLIENT_ID, CLIENT_SECRET, my_uri="http://0.0.0.0:8080", \
                                         redirect_uri="http://127.0.0.1:8080/authorize")
            server.start()
        except:
            raise Exception("Authorization Failed")
        # Get tokens and client
        ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
        write_tokens(ACCESS_TOKEN, REFRESH_TOKEN)

    CLIENT = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN,\
                       redirect_uri="http://127.0.0.1:8080/authorize")

    return CLIENT