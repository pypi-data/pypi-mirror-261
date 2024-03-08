from pydantic_settings import BaseSettings


class RabbitMQSettings(BaseSettings):
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    QUEUE_CONSUME: str
    QUEUE_PUBLISH: str
    VIRTUAL: str

    class Config:
        env_prefix = "RABBITMQ_"


class LDAPSettings(BaseSettings):
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    SCHEME: str
    BASE: str

    class Config:
        env_prefix = "LDAP_"


class ElasticSearchSettings(BaseSettings):
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    SCHEME: str
    INDEX: str
    INDEX_1: str
    INDEX_2: str
    INDEX_3: str
    INDEX_4: str
    INDEX_5: str
    INDEX_6: str

    class Config:
        env_prefix = "ES_"


class ProxySettings(BaseSettings):
    HOST: str = ""
    PORT: str = ""

    class Config:
        env_prefix = "PROXY_"


try:
    rabbitmq_settings = RabbitMQSettings()
except Exception:
    rabbitmq_settings = None

try:
    ldap_settings = LDAPSettings()
except Exception:
    ldap_settings = None

try:
    es_settings = ElasticSearchSettings()
except Exception:
    es_settings = None

try:
    proxy_settings = ProxySettings()
except Exception:
    proxy_settings = None
