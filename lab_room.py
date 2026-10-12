# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from decimal import Decimal

from device import Device
from device_status import DeviceStatus


class LabRoom:
    def __init__(self, room_id: str, name: str, capacity: int):
        if not room_id or not room_id.strip():
            raise ValueError("Mã phòng không được rỗng.")
        if not name or not name.strip():
            raise ValueError("Tên phòng không được rỗng.")
        if capacity <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")
        self.id = room_id
        self.name = name
        self.capacity = capacity
        self.__devices: list[Device] = []

    @property
    def devices(self) -> tuple[Device, ...]:
        """Trả về bản sao chỉ đọc để bên ngoài không sửa trực tiếp danh sách."""
        return tuple(self.__devices)

    def add_device(self, device: Device) -> None:
        if device is None:
            raise ValueError("Thiết bị không được là None.")
        if self.find_device(device.id) is not None:
            raise ValueError(f"Thiết bị mã '{device.id}' đã có trong phòng {self.id}.")
        self.__devices.append(device)

    def remove_device(self, device_id: str) -> bool:
        device = self.find_device(device_id)
        if device is None:
            return False
        self.__devices.remove(device)
        return True

    def find_device(self, device_id: str) -> Device | None:
        for d in self.__devices:
            if d.id.lower() == str(device_id).lower():
                return d
        return None

    def calculate_annual_maintenance_cost(self) -> Decimal:
        """Đa hình: gọi qua kiểu Device, không dùng if/isinstance."""
        return sum((d.calculate_maintenance_cost() for d in self.__devices), Decimal("0"))

    def get_devices_requiring_maintenance(self) -> list[Device]:
        return [d for d in self.__devices
                if d.status == DeviceStatus.UNDER_MAINTENANCE or d.age > 5]