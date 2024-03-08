from dataclasses import dataclass
import jwt
from datetime import datetime, timezone
from typing import Dict, Any
from flet import Page


@dataclass
class Algorithm:
    HS256 = "HS256"
    RS256 = "RS256"


@dataclass
class PemKey:
    private: str
    public: str


@dataclass
class SecretKey:
    algorithm: str = "HS256"
    secret: str = None
    pem_key: PemKey = None


def _time_exp(time_expiry: timezone, payload: Dict[str, Any]) -> Dict[str, Any]:
    if time_expiry is not None:
        payload["exp"] = datetime.now(tz=timezone.utc) + time_expiry
    return payload


def encode_RS256(
    payload: Dict[str, Any], public: str, time_expiry: timezone = None
) -> str:
    payload = _time_exp(time_expiry, payload)
    return jwt.encode(
        payload=payload,
        key=public,
        algorithm="RS256",
    )


def encode_HS256(
    payload: Dict[str, Any], secret_key: str, time_expiry: timezone = None
) -> str:
    payload = _time_exp(time_expiry, payload)
    return jwt.encode(
        payload=payload,
        key=secret_key,
        algorithm="HS256",
    )


def encode_verified(secret_key: SecretKey, value: str, time_expiration) -> str | None:
    """Verify the possible encryption of the value sent."""
    assert (
        secret_key.algorithm is not None
    ), "The secret_key algorithm is not supported, only (RS256, HS256) is accepted."

    if secret_key.algorithm == "RS256":
        return encode_RS256(
            payload=value,
            time_expiry=time_expiration,
            public=secret_key.pem_key.public,
        )
    elif secret_key.algorithm == "HS256":
        return encode_HS256(
            payload=value, time_expiry=time_expiration, secret_key=secret_key.secret
        )


async def _decode_payload_async(
    page: Page, key_login: str, secret_key: str, algorithms: str
) -> Dict[str, Any]:
    return jwt.decode(
        jwt=await page.client_storage.get_async(key_login),
        key=secret_key,
        algorithms=[algorithms],
    )


def _decode_payload(
    page: Page, key_login: str, secret_key: str, algorithms: str
) -> Dict[str, Any]:
    return jwt.decode(
        jwt=page.client_storage.get(key_login), key=secret_key, algorithms=[algorithms]
    )
