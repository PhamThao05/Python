# Nhập tên và năm sinh
ho_ten = input("Nhập vào họ tên: ")
nam_sinh = int(input("Nhập vào năm sinh: "))

# Tính tuổi
from datetime import datetime
nam_hien_tai = datetime.now().year
tuoi = nam_hien_tai - nam_sinh

# Hiển thị kết quả
print(f"Bạn \"{ho_ten.upper()}\" năm nay {tuoi} tuổi!")
