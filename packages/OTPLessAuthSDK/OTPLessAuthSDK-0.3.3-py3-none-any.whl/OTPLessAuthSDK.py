import base64
import copy
from urllib.parse import urlencode

import jwt
import requests
import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

OTPLESS_KEY_API = 'https://otpless.com/.well-known/openid-configuration'
OIDC_USERINFO_TOKEN_API = 'https://oidc.otpless.app/auth/userInfo'
MAGIC_LINK_URL = 'https://auth.otpless.app/auth/v1/authorize'
OTP_BASE_URL = 'https://user-auth.otpless.app/auth/otp'


class DotDict(dict):
    """A custom dictionary that allows dot notation access and provides a default value for missing keys."""

    def __getattr__(self, attr):
        return self.get(attr, None)  # Return None or any other default value you prefer

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __deepcopy__(self, memo):
        return DotDict(copy.deepcopy(dict(self), memo=memo))


class OTP:

    @staticmethod
    def send_otp(phoneNumber, email, channel,hash, orderId, expiry, otpLength,client_id,client_secret):
        return send_otp(phoneNumber,email,channel,hash,orderId,expiry,otpLength,client_id,client_secret,"")

    @staticmethod
    def resend_otp(orderId, client_id, client_secret):
        try:
            url = OTP_BASE_URL + '/v1/resend'
            headers = {
                'clientId': client_id,
                'clientSecret': client_secret,
                'Content-Type': 'application/json'
            }
            data = {
                'orderId': orderId
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
            return response.json()
        except Exception as error:
            raise Exception(f"Something went wrong, please try again. Error: {error}")

    @staticmethod
    def veriy_otp(orderId, otp, email, phoneNumber, client_id, client_secret):
        try:
            url = OTP_BASE_URL + '/v1/verify'
            headers = {
                'clientId': client_id,
                'clientSecret': client_secret,
                'Content-Type': 'application/json'
            }
            data = {
                'orderId': orderId,
                'otp': otp,
                'email': email,
                'phoneNumber': phoneNumber
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
            return response.json()
        except Exception as error:
            raise Exception(f"Something went wrong, please try again. Error: {error}")

def send_otp(phoneNumber,email,channel,hash,orderId,expiry,otpLength,client_id,client_secret,templateId):
    try:
        url = OTP_BASE_URL + '/v1/send'
        headers = {
            'clientId': client_id,
            'clientSecret': client_secret,
            'Content-Type': 'application/json'
        }
        data = {
            'phoneNumber': phoneNumber,
            'email': email,
            'channel': channel,
            'hash': hash,
            'orderId': orderId,
            'expiry': expiry,
            'otpLength': otpLength,
            'templateId':templateId
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
        return response.json()
    except Exception as error:
        raise Exception(f"Something went wrong, please try again. Error: {error}")
        
class UserDetail:

    @staticmethod
    def decode_id_token(id_token, client_id, client_secret, audience=None):
        try:
            oidc_config = get_config()
            public_key = get_public_key(oidc_config['jwks_uri'])
            decoded = decode_jwt(id_token, public_key['n'], public_key['e'], oidc_config['issuer'], audience)

            # Construct the user_detail dictionary from the decoded JWT            
            user_detail = DotDict({
                'success': True,
                'auth_time': int(decoded.get('auth_time', 0)),  # Provide a default value if 'auth_time' is not present
                'phone_number': decoded.get('phone_number'),     # Defaults to None if 'phone_number' is not present
                'email': decoded.get('email'),                   # Defaults to None if 'email' is not present
                'name': decoded.get('name'),                     # Defaults to None if 'name' is not present
                'country_code': decoded.get('country_code'),     # Defaults to None if 'country_code' is not present
                'national_phone_number': decoded.get('national_phone_number')  # Defaults to None
            })

            return user_detail
        except Exception as error:
            raise Exception(f"Something went wrong, please try again. Error: {error}")

    @staticmethod
    def verify_code(code, client_id, client_secret, audience=None):
        try:
            oidc_config = get_config()
            form_data = {
                'code': code,
                'client_id': client_id,
                'client_secret': client_secret,
            }
            response = requests.post(oidc_config['token_endpoint'], data=form_data)

            if response.status_code == 200:
                return UserDetail.decode_id_token(response.json()['id_token'], client_id, client_secret, client_id)
            else:
                raise Exception(
                    f"Request failed with status code {response.status_code}, message: {response.json()['message']}, full response: {response.text}")
        except Exception as error:
            raise Exception(f"Something went wrong, please try again. Error: {error}")

    @staticmethod
    def verify_token(token, client_id, client_secret):
        try:

            form_data = {
                'token': token,
                'client_id': client_id,
                'client_secret': client_secret
            }

            response = requests.post(OIDC_USERINFO_TOKEN_API, data=form_data)

            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

            resp_data = response.json()

            user_detail = DotDict({
                'success': True,
                'auth_time': int(resp_data['auth_time']),
                'phone_number': resp_data['phone_number'],
                'email': resp_data['email'],
                'name': resp_data['name'],
                'country_code': resp_data['country_code'],
                'national_phone_number': resp_data['national_phone_number']
            })

            return user_detail
        except Exception as error:
            raise Exception(f"Something went wrong, please try again. Error: {error}")

    @staticmethod
    def generate_magic_link(mobile_number, email, client_id, client_secret, redirect_uri, channel):
        try:
            query_params = {
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': redirect_uri
            }

            if mobile_number:
                query_params['mobile_number'] = mobile_number

            if email:
                query_params['email'] = email

            if channel:
                query_params['channel'] = channel

            encoded_params = urlencode(query_params)
            full_url = f"{MAGIC_LINK_URL}?{encoded_params}"

            response = requests.get(full_url)

            if response.status_code != 200:
                raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

            resp_data = response.json()

            user_detail = DotDict()
            for req_id in resp_data['requestIds']:
                if req_id['type'] == 'MOBILE':
                    user_detail.mobile_request_id = req_id['value']
                elif req_id['type'] == 'EMAIL':
                    user_detail.email_request_id = req_id['value']
                if 'destinationUri' in req_id:
                    user_detail.destination_uri = req_id['destinationUri']

            user_detail.success = True
            return user_detail
        except Exception as error:
            raise Exception(f"Something went wrong, please try again. Error: {error}")


def decode_jwt(jwt_token, modulus, exponent, issuer, audience=None):
    public_key = create_rsa_public_key(modulus, exponent)
    verify_options = {
        'algorithms': ['RS256'],
        'issuer': issuer,
    }
    if audience:
        verify_options['audience'] = audience

    try:
        decoded = jwt.decode(jwt_token, public_key, **verify_options)
        return decoded
    except jwt.InvalidAudienceError:
        raise Exception("Invalid audience")
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except Exception as error:
        raise Exception(f'JWT verification failed: {str(error)}')


def create_rsa_public_key(modulus_b64, exponent_b64):
    try:
        modulus_bytes = base64.urlsafe_b64decode(modulus_b64 + '=' * (4 - len(modulus_b64) % 4))
        exponent_bytes = base64.urlsafe_b64decode(exponent_b64 + '=' * (4 - len(exponent_b64) % 4))
    except Exception as e:
        raise Exception(f"Error during base64 decoding: {str(e)}")

    try:
        modulus = int.from_bytes(modulus_bytes, byteorder="big")
        exponent = int.from_bytes(exponent_bytes, byteorder="big")
    except Exception as e:
        raise Exception(f"Error during byte conversion: {str(e)}")

    try:
        public_numbers = rsa.RSAPublicNumbers(exponent, modulus)
        public_key = public_numbers.public_key(backend=default_backend())
    except Exception as e:
        raise Exception(f"Error during public key creation: {str(e)}")

    try:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    except Exception as e:
        raise Exception(f"Error during PEM serialization: {str(e)}")

    try:
        return serialization.load_pem_public_key(pem, backend=default_backend())
    except Exception as e:
        raise Exception(f"Error during PEM public key loading: {str(e)}")


def get_config():
    response = requests.get(OTPLESS_KEY_API, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    if response.json():
        return response.json()
    raise Exception('Unable to fetch OIDC config')


def get_public_key(url):
    response = requests.get(url, headers={'Content-Type': 'application/x-www-form-urlencoded'})

    if response.json() and 'keys' in response.json() and response.json()['keys'][0]:
        return response.json()['keys'][0]
    raise Exception('Unable to fetch public key')
