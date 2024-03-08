from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

import secrets
from typing import Dict, Any, Union

from jwt import DecodeError, ExpiredSignatureError, InvalidKeyError
from flet_easy.extras import Msg
from flet_easy.datasy import Datasy
from flet_easy.extras_jwt import _decode_payload_async, _decode_payload
from asyncio import run


class EasyKey:
    def __init__(self):
        self.__private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048
        )
        self.__public_key = self.__private_key.public_key()

    def private(self) -> str:
        return self.__private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ).decode("utf-8")

    def public(self) -> str:
        return self.__public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")

    def secret_key(self) -> str:
        return secrets.token_bytes(64).hex()


# ----------------------------------------------------------------


async def _handle_decode_errors(
    data: Datasy, key_login: str, algorithms: str, is_async: bool = False
) -> Union[Dict[str, Any], bool]:
    print(data.auto_logout)
    try:
        if is_async:
            if data.auto_logout:
                await data.page.pubsub.send_others_on_topic_async(
                    data.page.client_ip, Msg("updateLogin", value=data._login_done)
                )

            decode = await _decode_payload_async(
                page=data.page,
                key_login=key_login,
                secret_key=data.secret_key.secret
                if data.secret_key.secret is not None
                else data.secret_key.pem_key.public,
                algorithms=algorithms,
            )

        else:
            if data.auto_logout:
                data.page.pubsub.send_others_on_topic(
                    data.page.client_ip, Msg("updateLogin", value=data._login_done)
                )
            decode = _decode_payload(
                page=data.page,
                key_login=key_login,
                secret_key=data.secret_key.secret
                if data.secret_key.secret is not None
                else data.secret_key.pem_key.public,
                algorithms=algorithms,
            )

        """ It checks if there is a logout time, if there is a logout task running and finally if the user wants to create a logaut task. """
        if decode.get("exp") and not data._login_done and data.auto_logout:
            print("Creating log", data.auto_logout)
            data._create_task_login_update(decode)

        return decode

    except ExpiredSignatureError:
        if is_async:
            await data._logout_sessions_async(key_login)
        else:
            data._logout_sessions(key_login)
        print("Session has expired!")
        return False
    except InvalidKeyError:
        if is_async:
            await data._logout_sessions_async(key_login)
        else:
            data._logout_sessions(key_login)
        print("Invalid key!")
        return False
    except DecodeError:
        if is_async:
            await data._logout_sessions_async(key_login)
        else:
            data._logout_sessions(key_login)
        print(
            "Decoding error, possibly there is a double use of the 'client_storage' 'key' or Secret key invalid!"
        )
        return False
    except Exception as e:
        if is_async:
            await data._logout_sessions_async(key_login)
        else:
            data._logout_sessions(key_login)
        print("Error login:", e)
        return False


# ------------------------------------------


def decode_HS256(key_login: str, data: Datasy) -> Dict[str, Any] | bool:
    if data.page.client_storage.contains_key(key_login):
        return run(_handle_decode_errors(data, key_login, "HS256"))
    else:
        print("not value session")
        return False


async def decode_HS256_async(key_login: str, data: Datasy) -> Dict[str, Any] | bool:
    if await data.page.client_storage.contains_key_async(key_login):
        return await _handle_decode_errors(data, key_login, "HS256", True)

    else:
        print("not value session")
        return False


def decode_RS256(key_login: str, data: Datasy) -> Dict[str, Any] | bool:
    if data.page.client_storage.contains_key(key_login):
        return run(_handle_decode_errors(data, key_login, "RS256"))

    else:
        print("not value session")
        return False


async def decode_RS256_async(key_login: str, data: Datasy) -> Dict[str, Any] | bool:
    if await data.page.client_storage.contains_key_async(key_login):
        return await _handle_decode_errors(data, key_login, "RS256", True)

    else:
        print("not value session")
        return False
