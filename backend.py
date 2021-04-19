import ipaddress
import re


class IpCalculator:

    def __init__(self):
        self._ip_address = None
        self._mask = None

    @property
    def mask(self) -> str:
        return self._mask

    @mask.setter
    def mask(self, mask: str):
        if self.validate_mask(mask):
            self._mask = mask
        else:
            raise NameError("Niepoprawny format maski")

    @property
    def ip_address(self) -> str:
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address: str):
        if self.validate_ip_address(ip_address):
            self._ip_address = ip_address
        else:
            raise NameError("Niepoprawny format adresu IP")

    @staticmethod
    def validate_ip_address(ip_address: str) -> bool:
        is_match = re.match(r'^((25[0-5]|(2[0-4]|1[0-9]|[1-9]|)[0-9])(\.(?!$)|$)){4}$', ip_address)
        return is_match is not None

    @staticmethod
    def validate_mask(mask: str) -> bool:
        is_match = re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
                            mask)
        return is_match is not None

    def get_addresses(self):
        try:
            host = ipaddress.ip_network(f"{self._ip_address}/{self._mask}")
            return host
        except Exception as e:
            raise NameError(e)

    def get_broadcast(self):
        try:
            net = ipaddress.IPv4Network(f"{self._ip_address}/{self._mask}", False)
            return net.broadcast_address
        except Exception as e:
            raise NameError(e)
