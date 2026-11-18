# Time Modifier
Đây là một tool (nói cho sang mồm thế thôi chứ nó chỉ là một file Python) có chức năng tự động thay đổi thời gian sửa đổi (modification time) của tất cả các file và folder nằm bên trong thư mục chứa tệp Python này.

Cụ thể, mã sẽ thực hiện các công việc sau:
- Quét toàn bộ thư mục: Duyệt qua tất cả các thư mục con và tệp tin xuất phát từ vị trí đặt tệp script.   
- Thay đổi mốc thời gian giả lập: Đặt lại mốc thời gian thành ngày 07/11/2026 vào khoảng 11:00 sáng, cộng thêm một khoảng thời gian ngẫu nhiên từ 0 đến 1800 giây (30 phút) cho mỗi tệp và thư mục.   
- Loại trừ chính nó: Bỏ qua việc tự sửa đổi thời gian của chính tệp script Python đang chạy.   
- Hiển thị kết quả: In ra màn hình số lượng tệp và thư mục đã được cập nhật thành công, sau đó tạm dừng để người dùng bấm Enter mới thoát. 

Ứng dụng của tool này: dùng để "đánh lừa" hệ thống hoặc đồng bộ hóa thời gian tạo/sửa đổi của một loạt tệp dữ liệu về cùng một mốc thời điểm cụ thể.

# Cách dùng
### Bước 0: Chuẩn bị môi trường
Kiểm tra xem Python đã được cài hay chưa bằng cách mở Command Prompt trên Windows hoặc Terminal trên Mac/Linux và gõ:
```
python --version
```
Nếu output không hiện ra version (ví dụ Python 3.10.11) thì cần tải và cài đặt Python từ trang chủ python.org
### Bước 1: Kéo tool về máy
Vào nơi mà bạn định tải, click chuột phải chọn "Open in Terminal" rồi gõ:
```
git clone https://github.com/nphphuc/time-modifier.git
```
> Lưu ý: máy chưa có git thì phải tải nó về
### Bước 2: Đặt file tm.py vào folder cần đổi thời gian
Hãy di chuyển file tm.py này vào folder chứa các file và sub-folder mà bạn muốn thay đổi mốc thời gian. Lý do cho hành động này là vì tool được thiết kế để tự động quét toàn bộ các file nằm cùng folder với nó.
### Bước 3: Triển thôi!
Trên Windows:

- Mở folder chứa file Python, giữ phím `Shift` và click chuột phải vào khoảng trống trong folder, chọn "Open PowerShell window here" hoặc "Open command window here".
- Gõ lệnh sau và nhấn `Enter`:
```
python tm.py
```
Trên Mac / Linux:

- Mở Terminal, trỏ đến folder chứa tệp bằng lệnh `cd folder_path`.

- Gõ lệnh:
```
python3 tm.py
```

Và sau đó chương trình sẽ chạy và hiển thị quá trình cập nhật cho từng tệp/thư mục.

Khi hoàn thành, màn hình sẽ hiện dòng chữ Nhấn Enter để thoát..., bạn chỉ cần bấm phím Enter trên bàn phím để đóng cửa sổ là xong.
# Tùy chỉnh thời gian mong muốn
Để cấu hình thời gian mong muốn thì cần sửa lại code Python của mình.

Trong file code, thời gian được thiết lập ở dòng chứa hàm datetime(...). Cụ thể, bạn hãy tìm đoạn code sau:
```
new_time = datetime(2026, 11, 7, 11, 0, 0).timestamp() + random_seconds
```
Ý nghĩa các con số bên trong ngoặc datetime(Năm, Tháng, Ngày, Giờ, Phút, Giây) lần lượt là:
- 2026: Năm
- 11: Tháng (Tháng 11)
- 7: Ngày (Ngày 7)
- 11: Giờ (11 giờ sáng - định dạng 24h, ví dụ 3 giờ chiều là 15)
- 0: Phút
- 0: Giây

### Cách tùy chỉnh theo ý muốn 
- Mở file tm.py bằng một trình soạn thảo văn bản bất kỳ (như Notepad, VS Code, v.v.).
- Tìm đến 2 dòng có chứa lệnh datetime(...) (thường nằm ở hàm xử lý file và thư mục).
- Thay đổi các con số bên trong thành thời gian bạn muốn.

Ví dụ: Nếu bạn muốn đổi thời gian thành ngày 25 tháng 12 năm 2025, lúc 08:30 sáng, hãy sửa lại đoạn code đó thành:
```
new_time = datetime(2025, 12, 25, 8, 30, 0).timestamp() + random_seconds
```
> Lưu ý: Đoạn mã này có cộng thêm một khoảng thời gian ngẫu nhiên từ 0 đến 1800 giây ~ 30 phút để các file không bị trùng hoàn toàn từng giây với nhau. Nếu bạn muốn tất cả các file có chính xác một mốc thời gian cố định không cộng thêm giây ngẫu nhiên nào, bạn có thể xóa đoạn + random_seconds đi.