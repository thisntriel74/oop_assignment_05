# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal

from device_status import DeviceStatus


class Device(ABC):
    """Lớp trừu tượng: đặc điểm chung của mọi thiết bị."""

    def __init__(self, device_id: str, name: str, year_in_use: int,
                 price, status: DeviceStatus = DeviceStatus.ACTIVE):
        if device_id is None or not str(device_id).strip():
            raise ValueError("Mã thiết bị không được rỗng.")
        self.__id = device_id          # chỉ gán ở đây, không có setter
        # Gán qua property để tái sử dụng logic kiểm tra hợp lệ
        self.name = name
        self.year_in_use = year_in_use
        self.price = price
        self.status = status

    # ---- Mã thiết bị: chỉ đọc ----
    @property
    def id(self) -> str:
        return self.__id

    # ---- Tên ----
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value is None or not str(value).strip():
            raise ValueError("Tên thiết bị không được rỗng.")
        self.__name = value

    # ---- Năm đưa vào sử dụng ----
    @property
    def year_in_use(self) -> int:
        return self.__year_in_use

    @year_in_use.setter
    def year_in_use(self, value: int) -> None:
        if value > datetime.now().year:
            raise ValueError("Năm sử dụng không được lớn hơn năm hiện tại.")
        self.__year_in_use = value

    # ---- Giá mua ----
    @property
    def price(self) -> Decimal:
        return self.__price

    @price.setter
    def price(self, value) -> None:
        value = Decimal(str(value))
        if value <= 0:
            raise ValueError("Giá mua phải lớn hơn 0.")
        self.__price = value

    # ---- Trạng thái ----
    @property
    def status(self) -> DeviceStatus:
        return self.__status

    @status.setter
    def status(self, value: DeviceStatus) -> None:
        if not isinstance(value, DeviceStatus):
            raise TypeError("Trạng thái phải là DeviceStatus.")
        self.__status = value

    @property
    def age(self) -> int:
        """Số năm đã sử dụng."""
        return datetime.now().year - self.year_in_use

    @abstractmethod
    def calculate_maintenance_cost(self) -> Decimal:
        """Chi phí bảo trì dự kiến trong một năm (mỗi loại tự cài đặt)."""

    def __str__(self) -> str:
        return (f"[{self.id}] {self.name} | Năm: {self.year_in_use} | "
                f"Giá: {self.price:,.0f} | {self.status.value}")