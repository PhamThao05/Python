# Đoạn văn
doan_van = """Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 - 1969)"""

# Yêu cầu 1: Đếm số ký tự trong đoạn văn
so_ky_tu = len(doan_van)

# Yêu cầu 2: Kiểm tra sự tồn tại của các cụm từ (không phân biệt hoa thường)
cum_tu_1 = "Hồ Chí Minh".lower() in doan_van.lower()
cum_tu_2 = "non sông".lower() in doan_van.lower()

# Yêu cầu 3: Tách đoạn văn thành các câu
cau = doan_van.split('.')

# Yêu cầu 4: Kiểm tra xem đoạn văn có chứa ký tự khác chữ và số
co_ky_tu_khac = any(not (c.isalnum() or c.isspace()) for c in doan_van)

# Yêu cầu 5: Thay thế từ "Việt Nam" bằng "VIỆTNAM"
doan_van_thay_the = doan_van.replace("Việt Nam", "VIỆT NAM")

# Hiển thị kết quả
print(f"Số ký tự trong đoạn văn: {so_ky_tu}")
print(f"Có chứa cụm từ 'hồ chí minh': {cum_tu_1}")
print(f"Có chứa cụm từ 'non sông': {cum_tu_2}")
print(f"Các câu trong đoạn văn: {cau}")
print(f"Có chứa ký tự khác chữ và số: {co_ky_tu_khac}")
print(f"Đoạn văn sau khi thay thế: {doan_van_thay_the}")
