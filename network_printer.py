# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from inetworkable import INetworkable
from network_connection import NetworkConnection
from printer import Printer


class NetworkPrinter(Printer, INetworkable):
    """Máy in có mạng: kế thừa Printer và thực thi INetworkable."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._net = NetworkConnection()

    @property
    def ip_address(self) -> str:
        return self._net.ip_address

    @property
    def is_connected(self) -> bool:
        return self._net.is_connected

    def connect(self, ip_address: str) -> None:
        self._net.connect(ip_address)

    def disconnect(self) -> None:
        self._net.disconnect()

    def __str__(self) -> str:
        return f"{super().__str__()} | Hỗ trợ mạng"