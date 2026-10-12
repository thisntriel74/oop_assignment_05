# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from decimal import Decimal
from enum import Enum

from device import Device
from device_status import DeviceStatus


class PrinterType(Enum):
    LASER = "Laser"
    INKJET = "Phun"


class Printer(Device):
    def __init__(self, device_id, name, year_in_use, price,
                 printer_type: PrinterType, pages_printed: int, is_color: bool,
                 status: DeviceStatus = DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_in_use, price, status)
        if pages_printed < 0:
            raise ValueError("Số trang đã in không được âm.")
        self.printer_type = printer_type
        self.pages_printed = pages_printed
        # Bổ sung: đề tính phụ phí theo "máy in màu" nhưng không có thuộc tính biểu diễn
        self.is_color = is_color

    def calculate_maintenance_cost(self) -> Decimal:
        cost = self.price * Decimal("0.04")
        if self.pages_printed > 100_000:
            cost += Decimal("500000")
        if self.is_color:
            cost += Decimal("300000")
        return cost

    def __str__(self) -> str:
        color = "màu" if self.is_color else "đen trắng"
        return (f"{super().__str__()} | Printer: {self.printer_type.value}, "
                f"{self.pages_printed:,} trang, {color}")