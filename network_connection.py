# ****************
# Mã sinh viên: 20237381
# Họ tên: Đỗ Đình Quân
# ****************
class NetworkConnection:
    """Thành phần dùng chung, tránh lặp logic mạng giữa Computer và NetworkPrinter."""

    def __init__(self):
        self.__ip = ""
        self.__connected = False

    @property
    def ip_address(self) -> str:
        return self.__ip

    @property
    def is_connected(self) -> bool:
        return self.__connected

    def connect(self, ip_address: str) -> None:
        if ip_address is None or not str(ip_address).strip():
            raise ValueError("Địa chỉ IP không được rỗng.")
        if self.__connected:
            raise RuntimeError("Thiết bị đang kết nối, không thể kết nối lại.")
        self.__ip = ip_address
        self.__connected = True

    def disconnect(self) -> None:
        self.__connected = False
        self.__ip = ""      # không còn IP đang hoạt động