# Nhập số kẹo và số học sinh
n = int(input("Nhập số kẹo của cô (N): "))
m = int(input("Nhập số học sinh trong lớp (M): "))

# Tính số kẹo mỗi học sinh nhận được và số kẹo còn lại
if m == 0:
    print("Không thể chia kẹo vì không có học sinh nào.")
else:
    so_keo_moi_hs = n // m
    keo_con_lai = n % m

    # Hiển thị kết quả
    print(f"Mỗi học sinh được nhận: {so_keo_moi_hs} cái kẹo.")
    print(f"Cô còn lại: {keo_con_lai} cái kẹo.")
