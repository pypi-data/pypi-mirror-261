import ipih

from pih import A
from pih.collections.service import ServiceDescription

NAME: str = "Zabbix"

HOST = A.CT_H.SERVICES

VERSION: str = "0.11"

PACKAGES: tuple[str, ...] = ("pyzabbix",)

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    description="Zabbix service",
    host=HOST.NAME,
    use_standalone=True,
    packages=PACKAGES,
    standalone_name="zabbix",
    version=VERSION,
)

ZABBIX_SERVER_HOST: str = A.CT_H.SERVICES.NAME
ZABBIX_SERVER_PORT: int = 8080
ZABBIX_SERVER_LOGIN: str = "Admin"
ZABBIX_SERVER_PASSWORD: str = "zabbix"
