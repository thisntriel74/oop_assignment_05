# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
from enum import Enum


class DeviceStatus(Enum):
    """Trạng thái hoạt động của thiết bị."""
    ACTIVE = "Active"
    UNDER_MAINTENANCE = "UnderMaintenance"
    RETIRED = "Retired"