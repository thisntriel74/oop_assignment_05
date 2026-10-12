# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from decimal import Decimal

from device import Device
from device_status import DeviceStatus


class Projector(Device):
    def __init__(self, device_id, name, year_in_use, price,
                 lumen: int, lamp_hours: int,
                 status: DeviceStatus = DeviceStatus.ACTIVE):
        super().__init__(device_id, name, year_in_use, price, status)
        if lumen <= 0:
            raise ValueError("Độ sáng phải lớn hơn 0.")
        if lamp_hours < 0:
            raise ValueError("Số giờ dùng bóng đèn không được âm.")
        self.lumen = lumen
        self.lamp_hours = lamp_hours

    def calculate_maintenance_cost(self) -> Decimal:
        cost = self.price * Decimal("0.03")
        if self.lamp_hours > 3_000:
            cost += Decimal("1500000")
        return cost

    def __str__(self) -> str:
        return (f"{super().__str__()} | Projector: {self.lumen} lumen, "
                f"bóng đèn {self.lamp_hours:,} giờ")