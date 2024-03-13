### CLASS CAM
import datetime
import hashlib


def complete_with_char(input: str, elem: str):

    if len(elem) != 1:
        raise ValueError(f"Completar string com char inválido {elem}.")

    if input is None:
        raise ValueError(f"Completar string com INPUT inválido {input}.")

    # if (len(input) > 8):
    #   raise ValueError(f"Completar string com INPUT inválido {input}.")

    while len(input) < 8:
        input = f"{input}{elem}"

    return input


class CustomCredential:
    token: str = ""
    user: str = ""
    secret: str = ""
    auth: int = 0


class directoryUser:
    id: str = ""
    display: str = ""
    number: str = ""
    firstname: str = ""
    lastname: str = ""
    phone: str = ""
    email: str = ""
    unitName: str = ""
    unitID: str = ""
    sectorName: str = ""
    sectorID: str = ""
    tipoRamal: str = ""


"""
    INSTITUICAO
    TIPO
    DN 
    CN
    SN
    ObjectClass
    codigoPais
    codigoArea
    prefixoInicial
    prefixoFinal 
    prioridade
    destino
    protocolo
    status

('cn=55851283,ou=UNILAB,ou=fonernp,ou=rotasParticipantes,dc=voip,dc=rnp,dc=br',
     {'cn': [b'55851283']
        , 'sn': [b'55851283']
        , 'objectClass': [b'rotasParticipantes']
        , 'codigoPais': [b'55']
        , 'codigoArea': [b'85']
        , 'prefixoInicial': [b'1283']
        , 'prefixoFinal': [b'1283']
        , 'prioridade': [b'10']
        , 'destino': [b'200.129.19.17:5060']
        , 'protocolo': [b'UDP']
        , 'status': [b'1']
    }
)
"""


class es_rota:
    instituicao: str = None
    tipo: str = None
    id: str = None
    dn: str = None
    cn: str = None
    sn: str = None
    objectclass: str = None
    codigoPais: str = None
    codigoArea: str = None
    prefixoInicial: str = None
    prefixoFinal: str = None
    prioridade: str = None
    destino: str = None
    protocolo: str = None
    status: bool = None
    dtCadastro: datetime = None
    dtAtualizado: datetime = None
    bAtualizado: bool = None
    __input: object = None

    """ cn=55851283,ou=UNILAB,ou=fonernp,ou=rotasParticipantes,dc=voip,dc=rnp,dc=br
        { 'cn': [b'55851283'], 'sn': [b'55851283'], 'objectClass': [b'rotasParticipantes'], 'codigoPais': [b'55'], 'codigoArea': [b'85']
            , 'prefixoInicial': [b'1283'], 'prefixoFinal': [b'1283'], 'prioridade': [b'10'], 'destino': [b'200.129.19.17:5060'], 'protocolo': [b'UDP']
            , 'status': [b'1']} """

    def __init__(self, dn: str = None, ldapInfo=None):
        self.__input = ldapInfo
        if not self.__input:
            return None
        self.dn = dn
        orgs = dn.split(",")
        self.instituicao = orgs[1].split("=")[1]
        self.tipo = orgs[2].split("=")[1]
        self.cn = ldapInfo["cn"][0].decode("utf-8")
        self.sn = ldapInfo["sn"][0].decode("utf-8")
        self.objectclass = ldapInfo["objectClass"][0].decode("utf-8")
        self.codigoPais = ldapInfo["codigoPais"][0].decode("utf-8")
        try:
            self.codigoArea = ldapInfo["codigoArea"][0].decode("utf-8")
        except Exception:
            self.codigoArea = ""
        self.prefixoInicial = ldapInfo["prefixoInicial"][0].decode("utf-8")
        self.prefixoFinal = ldapInfo["prefixoFinal"][0].decode("utf-8")
        self.prioridade = ldapInfo["prioridade"][0].decode("utf-8")
        self.destino = ldapInfo["destino"][0].decode("utf-8")
        self.protocolo = ldapInfo["protocolo"][0].decode("utf-8")
        self.status = ldapInfo["status"][0].decode("utf-8")
        self.dtCadastro = datetime.datetime.now()
        self.dtAtualizado = datetime.datetime.now()
        self.bAtualizado = True
        self.id = hashlib.md5(dn.encode("utf-8")).hexdigest()

    def to_dict(self):
        return {
            "dn": self.dn,
            "instituicao": self.instituicao,
            "tipo": self.tipo,
            "cn": self.cn,
            "sn": self.sn,
            "objectClass": self.objectclass,
            "codigoPais": self.codigoPais,
            "codigoArea": self.codigoArea,
            "prefixoInicial": self.prefixoInicial,
            "rotaInicial": complete_with_char(self.prefixoInicial, "0"),
            "prefixoFinal": self.prefixoFinal,
            "rotaFinal": complete_with_char(self.prefixoFinal, "9"),
            "prioridade": self.prioridade,
            "destino": self.destino,
            "protocolo": self.protocolo,
            "status": self.status,
            "dtCadastro": self.dtCadastro,
            "dtAtualizado": self.dtAtualizado,
            "bAtualizado": self.bAtualizado,
            "id": self.id,
        }
