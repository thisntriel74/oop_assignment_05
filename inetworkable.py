# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from abc import ABC, abstractmethod


class INetworkable(ABC):
    """Interface: năng lực kết nối mạng, độc lập với cây kế thừa Device."""

    @property
    @abstractmethod
    def ip_address(self) -> str: ...

    @property
    @abstractmethod
    def is_connected(self) -> bool: ...

    @abstractmethod
    def connect(self, ip_address: str) -> None: ...

    @abstractmethod
    def disconnect(self) -> None: ...