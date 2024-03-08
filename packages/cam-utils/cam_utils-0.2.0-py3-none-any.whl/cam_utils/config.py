import os

""""
Configuração do Serviço

    rabbit = DBRabbitMQ(config['RABBITMQ_SERVER'], config['RABBITMQ_PORT'], config['RABBITMQ_USER'], config['RABBITMQ_SECRET'], config['RABBITMQ_VIRTUAL'])

    # Inicializa Consumo
    rabbit.consume(config['RABBITMQ_CONSUME'])
"""


def localconfig():
    mqServer = os.getenv("RABBITMQ_SERVER")
    mqPort = os.getenv("RABBITMQ_PORT")
    mqVirtual = os.getenv("RABBITMQ_VIRTUAL")
    mqUser = os.getenv("RABBITMQ_USER")
    mqPassword = os.getenv("RABBITMQ_SECRET")
    mqConsume = os.getenv("RABBITMQ_CONSUME")
    mqPublish = os.getenv("RABBITMQ_PUBLISH")

    ldapServer = os.getenv("LDAP_SERVER")
    ldapPort = os.getenv("LDAP_PORT")
    ldapScheme = os.getenv("LDAP_SCHEME")
    ldapUser = os.getenv("LDAP_USER")
    ldapPassword = os.getenv("LDAP_SECRET")
    ldapBase = os.getenv("LDAP_BASE")

    esServer = os.getenv("ELASTIC_SERVER")
    esPort = os.getenv("ELASTIC_PORT")
    esScheme = os.getenv("ELASTIC_SCHEME")
    esUser = os.getenv("ELASTIC_USER")
    esPassword = os.getenv("ELASTIC_SECRET")
    esIndex = os.getenv("ELASTIC_INDEX")

    if esServer is None:
        esServer = "localhost"

    if esPort is None:
        esPort = "0"

    if esScheme is None:
        esScheme = "http"

    if esUser is None:
        esUser = "user"

    if esPassword is None:
        esPassword = "password"

    if esIndex is None:
        esIndex = "rotas"

    if ldapServer is None:
        ldapServer = "localhost"

    if ldapPort is None:
        ldapPort = "389"

    if ldapScheme is None:
        ldapScheme = "ldap"

    if ldapUser is None:
        ldapUser = "cn=admin,dc=voip,dc=rnp,dc=br"

    if ldapPassword is None:
        ldapPassword = "password"

    if ldapBase is None:
        ldapBase = "dc=voip,dc=rnp,dc=br"

    if mqServer is None:
        mqServer = "localhost"

    if mqPort is None:
        mqPort = "5867"

    if mqVirtual is None:
        mqVirtual = "rnp"

    if mqUser is None:
        mqUser = "admin"

    if mqPassword is None:
        mqPassword = "password"

    if mqPublish is None:
        mqPublish = "publish"

    if mqConsume is None:
        mqConsume = "consume"

    setconfig = {
        "RABBITMQ_SERVER": mqServer,
        "RABBITMQ_PORT": mqPort,
        "RABBITMQ_USER": mqUser,
        "RABBITMQ_SECRET": mqPassword,
        "RABBITMQ_VIRTUAL": mqVirtual,
        "RABBITMQ_CONSUME": mqConsume,
        "RABBITMQ_PUBLISH": mqPublish,
        "LDAP_SERVER": ldapServer,
        "LDAP_PORT": ldapPort,
        "LDAP_SCHEME": ldapScheme,
        "LDAP_USER": ldapUser,
        "LDAP_SECRET": ldapPassword,
        "LDAP_BASE": ldapBase,
        "ELASTIC_SERVER": esServer,
        "ELASTIC_PORT": esPort,
        "ELASTIC_SCHEME": esScheme,
        "ELASTIC_USER": esUser,
        "ELASTIC_SECRET": esPassword,
        "ELASTIC_INDEX": esIndex,
    }

    return setconfig
