from pydantic import BaseModel


class DetailInfo(BaseModel):
    detail: str


EMPTY_RESPONSE = {
    "model": {},
}

EMPTY_WITH_TOKENS_COOKIES = {
    "description": "Sets access and refresh tokens",
    "headers": {
        "Set-Cookie": {
            "description": "Sets access token",
            "schema": {
                "type": "string",
            },
            "example": "access=a.b.c",
        },
    },
}

DETAIL_INFO = {
    "model": DetailInfo,
}
