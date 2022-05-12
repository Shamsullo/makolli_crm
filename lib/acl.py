from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from lib.config import Keys
from authlib.jose import jwt
import time

# test
app = FastAPI()
mkeys = Keys()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer,
                                                                self).__call__(
            request)
        if credentials:

            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication method.")
            if not self.verify_jwt(credentials.credentials, request):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str, request: Request) -> bool:
        isTokenValid: bool = False

        try:
            #endpoint_path = request.url.path
            try:
                payload = jwt.decode(jwtoken, mkeys.publickey) #decode_session_token(jwtoken, request)
            except:
                payload = jwt.decode(jwtoken, mkeys.publickeyold)
            # if rds.get(payload['user_id']) is None:
            #     payload=None
        except Exception as e:
            print("JWT verification error: {}".format(e))
            payload = None
        if payload:
            isTokenValid = True
            """for roles in payload["user_roles"]:
                if endpoint_path.find(roles) > 0 or endpoint_path.find(
                        'logout'):
                    isTokenValid = True
                else:
                    isTokenValid = False"""
        return isTokenValid


def signJWT(user: str):
    payload = {
        "user_name": user,
        "expires": time.time() + 3600
    }
    header = {'alg': 'RS256'}
    token = jwt.encode(header, payload, mkeys.privatekey)
    return token


def sign_token(login: str, user: str, roles: list):
    payload = {
        "user_id": user,
        "user_login": login,
        "user_roles": roles,
        "expires": time.time() + (3600 * 3)  # TEMP EXTENDED
    }
    header = {'alg': 'RS256'}
    token = jwt.encode(header, payload, mkeys.privatekey)
    return token


def refresh_token(login: str, user: str, roles: list):
    payload = {
        "user_id": user,
        "user_login": login,
        "user_roles": roles,
        "expires": time.time() + (3600 * 24 * 15)
    }
    header = {'alg': 'RS256'}
    token = jwt.encode(header, payload, mkeys.privatekey)
    return token

def refresh_access_token(token):
    decoded_token = decodeJWT(token)
    return sign_token(decoded_token['user_id'], decoded_token['user_login'],  decoded_token['user_roles']) #changed 1
    


def decode_session_token(token: str, request: Request) -> dict:
    try:
        user_agent = request.headers.get('user-agent')
        try:
            decoded_token = jwt.decode(credentials, mkeys.publickey)
        except:
            decoded_token = jwt.decode(credentials, mkeys.publickeyold)
        return decoded_token # return decoded token for all cases
        
    except Exception as e:
        raise HTTPException(status_code=403, detail="JWT error: {}".format(e))

# return decoded token for all cases
def decodeJWT(token: str) -> dict:
    try:
        try:
            decoded_token = jwt.decode(credentials, mkeys.publickey)
        except:
            decoded_token = jwt.decode(credentials, mkeys.publickeyold)
        return decoded_token 
    except Exception as e:
        raise HTTPException(status_code=403, detail="JWT decode error: {}".format(e))

# return decoded token with checking
def JWTpayload(credentials: str = Depends(JWTBearer())) -> dict:
    try:
        try:
            decoded_token = jwt.decode(credentials, mkeys.publickey)
        except:
            decoded_token = jwt.decode(credentials, mkeys.publickeyold)
        return decoded_token 
    except Exception as e:
        #return "JWT error: {}".format(e)
        raise HTTPException(status_code=403, detail="JWT payload error: {}".format(e))
