from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "password" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlW9r2zAQxr9K8KsOutFm6Vr2Lg2MbWwpdOsYlGIu9sUWkSVXOq8tJd+9OtmJHOcPLQ"
    "zasr1LnntOuvuhO99HhU5R2ncXFk30sXcfKSjQ/VjR93sRlGVQWSCYSG+snMMrMLFkICEn"
    "TkFadFKKNjGiJKGVU1UlJYs6cUahsiBVSlxXGJPOkHJfyOWVk4VK8Rbt4m85i6cCZbpSp0"
    "j5bq/HdFd67YuiT97It03iRMuqUMFc3lGu1dItFLGaoUIDhHw8mYrL5+qaNhcd1ZUGS11i"
    "KyfFKVSSWu0+kkGiFfNz1VjfYMa3vO0fDo4HJ+8/DE6cxVeyVI7ndXuh9zrRExj/jOY+Dg"
    "S1w2MM3LAAIdfRjXIwm9ktEzr4XNFdfAtYz8qvgNtYosooZ2hHRzto/Rqejz4Pz/ec6w33"
    "ot0zrh/3uAn16xgjDQhLsPZGmw0PcDvFds7fAbkQAskwfS8aJY/0dNZ6nCxMIJndgEnjtY"
    "ju623e9VDRL7oKKMg8Hm6SO2g23BCNSPJNu6+J7Nx+EDz/198rWn9/3EeLS3rC6LZS/vHJ"
    "bS9BHo0nQGzsrxPg4cHBIwA611aAPrYK0N1IWM/gKsSvP87GmyG2UjogL5Rr8DIVCe33pL"
    "B09TKx7qDIXXPRhbXXsg1v7/vwd5fr6NvZqaegLWXGn+IPOH3uz8v8AcGFnHc="
)
