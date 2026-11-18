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
