# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from decimal import Decimal

from device import Device
from device_status import DeviceStatus
from inetworkable import INetworkable
from network_connection import NetworkConnection


class Computer(Device, INetworkable):
    def __init__(self, device_id, name, year_in_use, price,
                 ram_gb: int, cpu: str, has_dedicated_gpu: bool,
                 status: DeviceStatus = DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_in_use, price, status)
        if ram_gb <= 0:
            raise ValueError("RAM phải lớn hơn 0.")
        if not cpu or not cpu.strip():
            raise ValueError("Loại CPU không được rỗng.")
        self.ram_gb = ram_gb
        self.cpu = cpu
        self.has_dedicated_gpu = has_dedicated_gpu
        self._net = NetworkConnection()

    def calculate_maintenance_cost(self) -> Decimal:
        cost = self.price * Decimal("0.05")
        if self.has_dedicated_gpu:
            cost += self.price * Decimal("0.02")
        if self.age > 5:
            cost += self.price * Decimal("0.01")
        return cost

    # ---- INetworkable ----
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
        gpu = "có" if self.has_dedicated_gpu else "không"
        return f"{super().__str__()} | Computer: {self.ram_gb}GB, {self.cpu}, GPU rời: {gpu}"