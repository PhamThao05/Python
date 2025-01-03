# Khởi tạo danh sách điểm
diem_thi = ["A", "B", "C", "F", "B", "A", "F", "C", "D", "A"]

# Yêu cầu 1: Số sinh viên trong lớp
so_sinh_vien = len(diem_thi)

# Yêu cầu 2: Số sinh viên phải học lại môn này (điểm F)
so_hoc_lai = diem_thi.count("F")

# Yêu cầu 3: Số sinh viên có điểm từ B trở lên (A, B)
diem_tot = ["A", "B"]
so_diem_tot = sum(1 for diem in diem_thi if diem in diem_tot)

# Yêu cầu 4: Loại bỏ điểm của sinh viên đầu tiên và cuối cùng
diem_moi = diem_thi[1:-1]

# Hiển thị kết quả
print(f"danh sách điểm: {diem_thi}")
print(f"Số sinh viên trong lớp: {so_sinh_vien}")
print(f"Số sinh viên phải học lại môn này (điểm F): {so_hoc_lai}")
print(f"Số sinh viên có điểm từ B trở lên: {so_diem_tot}")
print(f"Danh sách điểm sau khi loại bỏ sv đầu và cuối: {diem_moi}")
