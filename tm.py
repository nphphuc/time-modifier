import os
import random
from datetime import datetime

def fix_current_folder():
    target_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"[*] Đang xử lý thư mục hiện tại: {target_dir}\n")

    file_count = 0
    folder_count = 0

    for root, dirs, files in os.walk(target_dir, topdown=False):
        # 1. Cập nhật thời gian cho các file
        for file in files:
            file_path = os.path.join(root, file)
            if file == os.path.basename(__file__):
                continue
                
            try:
                random_seconds = random.randint(0, 1800)
                new_time = datetime(2026, 11, 7, 11, 0, 0).timestamp() + random_seconds
                os.utime(file_path, (new_time, new_time))
                file_count += 1
            except Exception as e:
                print(f"[!] Lỗi file {file}: {e}")

        # 2. Cập nhật thời gian cho các thư mục con
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                random_seconds = random.randint(0, 1800)
                new_time = datetime(2026, 11, 7, 11, 0, 0).timestamp() + random_seconds
                os.utime(dir_path, (new_time, new_time))
                folder_count += 1
            except Exception as e:
                print(f"[!] Lỗi thư mục {dir_name}: {e}")

    print(f"\n--- HOÀN TẤT ---")
    print(f"Đã cập nhật thành công cho: {file_count} file và {folder_count} thư mục.")

if __name__ == "__main__":
    fix_current_folder()
    # Dừng màn hình ở cuối để xem kết quả thay vì tắt phụt đi
    input("\nNhấn Enter để thoát...")