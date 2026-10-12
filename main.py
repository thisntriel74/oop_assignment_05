# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
import sys

from computer import Computer
from device_status import DeviceStatus
from inetworkable import INetworkable
from lab_room import LabRoom
from network_printer import NetworkPrinter
from printer import Printer, PrinterType
from projector import Projector

sys.stdout.reconfigure(encoding="utf-8")   # in tiếng Việt đúng trên Windows

# 1. Tạo thiết bị
pc1 = Computer("PC01", "Dell Optiplex", 2019, 15_000_000, 16, "Intel i5", True)
pc2 = Computer("PC02", "HP ProDesk", 2024, 18_000_000, 8, "Intel i3", False)
pr1 = NetworkPrinter("PR01", "Canon LBP", 2022, 6_000_000,
                     PrinterType.INKJET, 120_000, True)
pr2 = Printer("PR02", "HP LaserJet", 2023, 5_000_000,
              PrinterType.LASER, 30_000, False)
pj1 = Projector("PJ01", "Epson EB-X", 2021, 12_000_000, 3600, 3_500,
                DeviceStatus.UNDER_MAINTENANCE)

room_a = LabRoom("A101", "Phòng Lab 1", 40)
room_b = LabRoom("B202", "Phòng Lab 2", 30)

# Thao tác 1: thêm thiết bị vào phòng
for d in (pc1, pc2, pr1):
    room_a.add_device(d)
for d in (pr2, pj1):
    room_b.add_device(d)

# Thao tác 2: thêm thiết bị trùng mã
try:
    room_a.add_device(pc1)
except ValueError as ex:
    print(f"[Lỗi mong đợi] {ex}\n")

rooms = [room_a, room_b]

for room in rooms:
    # Thao tác 3: in danh sách thiết bị
    print(f"=== {room.name} ({room.id}) ===")
    for d in room.devices:
        print(f"  {d}")

    # Thao tác 4: tổng chi phí bảo trì
    print(f"  -> Tổng chi phí bảo trì dự kiến: "
          f"{room.calculate_annual_maintenance_cost():,.0f} VND")

    # Thao tác 5: thiết bị cần bảo trì
    print("  -> Thiết bị cần bảo trì:")
    for d in room.get_devices_requiring_maintenance():
        print(f"     {d.id} - {d.name}")
    print()

# Thao tác 6 + 7: làm việc qua INetworkable, không phụ thuộc lớp cụ thể
networkables = [d for r in rooms for d in r.devices if isinstance(d, INetworkable)]

for i, n in enumerate(networkables, start=1):
    n.connect(f"192.168.1.{10 + i}")

print("=== Thiết bị mạng ===")
for n in networkables:
    print(f"  {type(n).__name__}: IP={n.ip_address}, đã kết nối={n.is_connected}")

# Kiểm tra ràng buộc: kết nối lại khi đang kết nối
try:
    networkables[0].connect("10.0.0.1")
except RuntimeError as ex:
    print(f"[Lỗi mong đợi] {ex}")

# Ngắt kết nối rồi kiểm tra
networkables[0].disconnect()
print(f"Sau disconnect: is_connected={networkables[0].is_connected}, "
      f"IP='{networkables[0].ip_address}'")