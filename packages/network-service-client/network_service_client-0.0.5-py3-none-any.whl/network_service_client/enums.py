from enum import Enum


class NetworksNames(str, Enum):
    AlastriaRedT = "Alastria Red T"
    AlastriaRedB = "Alastria Red B"
    Lacchain = "Lacchain"
    Ebsi = "Ebsi"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class ContractsNames(str, Enum):
    Eidas = "Eidas"
    AlastriaServiceProvider = "AlastriaServiceProvider"
    AlastriaIdentityIssuer = "AlastriaIdentityIssuer"
    AlastriaCredentialRegistry = "AlastriaCredentialRegistry"
    AlastriaPresentationRegistry = "AlastriaPresentationRegistry"
    AlastriaPublicKeyRegistry = "AlastriaPublicKeyRegistry"
    AlastriaIdentityManager = "AlastriaIdentityManager"
    LacchainDIDRegistry = "LacchainDIDRegistry"
    LacchainCredentialRegistry = "LacchainCredentialRegistry"
    LacchainClaimsVerifier = "LacchainClaimsVerifier"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
