import socket
from re import match
from geolocalizer.constants import WWW_REGEXP


def validate_ipv4(address: str) -> bool:
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return True
    except socket.error:
        return False
    return True


def validate_ipv6(address: str) -> bool:
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:
        return False
    return True


def validate_www(address: str) -> bool:
    return match(WWW_REGEXP, address)


def validate_address(address: str) -> bool:
    return any([
        validate_ipv4(address),
        validate_ipv6(address),
        validate_www(address),
    ])
