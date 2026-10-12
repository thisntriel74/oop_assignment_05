# Phân tích yêu cầu nghiệp vụ

## 1. Bài toán

Xây dựng chương trình quản lý các thiết bị trong phòng thực hành. Mỗi thiết bị có thông tin chung gồm mã, tên, năm đưa vào sử dụng, giá mua, trạng thái. Hệ thống quản lý ba loại thiết bị máy tính, máy in, máy chiếu, mỗi loại có khả năng kết nối mạng khác nhau. Sử dụng các kiến thức về oop để thực hành.

## 2. Các đối tượng chính

| Đối tượng      | Loại                                             | Thuộc tính chính                                                    |
| -------------- | ------------------------------------------------ | ------------------------------------------------------------------- |
| Device         | Lớp trừu tượng                                   | Mã, tên, năm sử dụng, giá mua, trạng thái                           |
| Computer       | Lớp con (Kế thừa Device, thực thi INetworkable)  | RAM, loại bộ xử lý, có GPU rời không                                |
| Printer        | Lớp con (Kế thừa Device)                         | Loại (laser or phun), số trang, có in màu không (boolean)           |
| NetworkPrinter | Lớp con (Kế thừa Printer, thực thi INetworkable) | Kế thừa các thuộc tính của Printer và thực thi các hàm kết nối mạng |
| Projector      | Lớp con (Kế thừa Device)                         | Độ sáng (tính bằng lumen), số giờ đã sử dụng bóng đèn               |
| Labroom        | Lớp chứa                                         | Mã phòng, tên, sức chứa, danh sách thiết bị                         |
| INetworkable   | Interface                                        | IpAddress, Connect(), Disconnect(), IsConnected                     |

**Ghi chú về dữ liệu kết nối mạng** (áp dụng cho `Computer` và `NetworkPrinter`):

- Địa chỉ IP hiện tại: có giá trị khi đang kết nối, `None` khi chưa kết nối hoặc đã ngắt.
- Trạng thái kết nối: cần để kiểm tra điều kiện "không kết nối lại khi đang kết nối".
- (Chưa chắc chắn) Có thể chỉ lưu IP rồi suy ra trạng thái (có

## 3. Chức năng ( phương thức )

**Thiết bị**

- Hiển thị thông tin thiết bị dưới dạng chuỗi (`__str__`).
- Tính chi phí bảo trì dự kiến 1 năm (mỗi loại tính khác nhau, thể hiện bằng đa hình).
- Tính tuổi sử dụng = năm hiện tại − năm sử dụng.

**Kết nối mạng** (`Computer`, `NetworkPrinter`)

- Kết nối với một địa chỉ IP, ngắt kết nối, kiểm tra trạng thái kết nối.

**Phòng thực hành**

- Thêm thiết bị, xóa thiết bị theo mã, tìm thiết bị theo mã.
- Tính tổng chi phí bảo trì dự kiến hằng năm của phòng.
- Liệt kê thiết bị cần bảo trì: đang `UnderMaintenance` hoặc dùng trên 5 năm.

**Công thức chi phí bảo trì**

| Loại                         | Công thức                                                               |
| ---------------------------- | ----------------------------------------------------------------------- |
| `Computer`                   | 5% giá + 2% giá (nếu có GPU rời) + 1% giá (nếu dùng > 5 năm)            |
| `Printer` / `NetworkPrinter` | 4% giá + 500.000 đồng (nếu > 100.000 trang) + 300.000 đồng (nếu in màu) |
| `Projector`                  | 3% giá + 1.500.000 đồng (nếu đèn > 3.000 giờ)                           |

> `NetworkPrinter` kế thừa cách tính của `Printer`, không cần viết lại.
> Mọi điều kiện đều là "lớn hơn hẳn" (`>`), nên giá trị đúng bằng mốc (5 năm, 100.000 trang, 3.000 giờ) **không** bị cộng phụ phí.

## 4. Ràng buộc dữ liệu

**Thiết bị**

- Mã thiết bị không rỗng; chỉ gán khi khởi tạo, không sửa được sau đó.
- Giá mua > 0.
- Năm sử dụng ≤ năm hiện tại.
- Không tạo trực tiếp đối tượng `Device`.
- (Bổ sung, đề không nêu rõ) Tên thiết bị không rỗng.

**Thuộc tính của lớp con** _(bổ sung hợp lý, chưa chắc đề yêu cầu)_

- RAM > 0; độ sáng máy chiếu > 0.
- Số trang đã in ≥ 0; số giờ dùng bóng đèn ≥ 0.

**Kết nối mạng** (`Computer`, `NetworkPrinter`)

- Địa chỉ IP không rỗng khi kết nối.
- Đang kết nối thì không cho kết nối lại.
- Sau khi ngắt: `IsConnected` = `False` và không còn địa chỉ IP đang hoạt động.

**Phòng thực hành**

- Không thêm hai thiết bị cùng mã vào một phòng.
- Không chấp nhận thiết bị `None`.
- Tính tổng chi phí phải dùng **đa hình**, không kiểm tra loại thiết bị bằng `if`/`isinstance`.
- (Bổ sung) Sức chứa > 0; mã phòng không rỗng.

## 5. Quan hệ giữa các lớp

| Quan hệ                                        | Loại                               | Lý do                                                      |
| ---------------------------------------------- | ---------------------------------- | ---------------------------------------------------------- |
| `Computer`, `Printer`, `Projector` -> `Device` | Kế thừa ("là một")                 | Dùng chung thuộc tính chung, khác nhau ở cách tính bảo trì |
| `NetworkPrinter` -> `Printer`                  | Kế thừa ("là một")                 | Máy in có mạng vẫn là máy in, chỉ bổ sung khả năng mạng    |
| `Computer` -> `INetworkable`                   | Thực thi interface ("có khả năng") | Mạng là năng lực, độc lập với cây kế thừa                  |
| `NetworkPrinter` -> `INetworkable`             | Thực thi interface                 | Chỉ những máy in có mạng mới có năng lực này               |
| `LabRoom` <- `Device`                          | Kết tập                            | Thiết bị tồn tại độc lập, không bị hủy khi phòng bị hủy    |

## 6. Giải thích thiết kế

### 6.1. Vì sao chọn `NetworkPrinter` (trade-off) _(nháp, cần tự viết lại theo ý mình)_

Tôi chọn tách `NetworkPrinter` kế thừa `Printer` và thực thi `INetworkable`, vì đề nêu rõ chỉ một số máy in có mạng, nên không thể cho mọi `Printer` thực thi interface này. Ưu điểm là máy in thường không bị gắn hành vi mạng vô nghĩa, và có thể duyệt thiết bị mạng bằng kiểu `INetworkable` mà không cần biết lớp cụ thể. Nhược điểm là phải thêm một lớp, và một máy in thường muốn nâng cấp có mạng thì phải tạo đối tượng mới. Ngoài ra, mã quản lý kết nối ở `NetworkPrinter` và `Computer` có thể bị lặp lại. Phương án dùng thành phần mạng riêng kết tập vào thiết bị linh hoạt hơn nhưng phức tạp hơn so với mức bài yêu cầu.

### 6.2. Vì sao thêm thuộc tính "in màu" cho `Printer`

Đề chỉ nêu loại máy in là laser hoặc phun, nhưng phụ phí bảo trì lại tính cho máy in màu. Hai tiêu chí này không trùng nhau (có máy laser màu, máy phun đen trắng), nên cần thêm thuộc tính boolean riêng để tính đúng chi phí.

### 6.3. `LabRoom` và `Device`: kết tập hay hợp thành?

Là **kết tập**. Thiết bị vẫn tồn tại khi chưa được phân bổ vào phòng nào, và khi phòng bị hủy thì thiết bị không bị hủy theo (có thể chuyển sang phòng khác). Nghĩa là vòng đời của thiết bị độc lập với vòng đời của phòng. Nếu là hợp thành thì thiết bị phải bị hủy cùng phòng.
