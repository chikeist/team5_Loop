while True:
    bit = input("Nhập 8 bit (hoặc nhấn Enter để thoát): ")
    if not bit:
        break
    if len(bit) != 8 or not bit.isdigit() or not set(bit).issubset({'0', '1'}):
        print("Đầu vào không hợp lệ. Vui lòng nhập 8 bit (0 hoặc 1).")
    else:
        soluong = bit.count('1')
        chan_le = 0  if soluong % 2 == 0 else 1
        print("Bit kiểm tra chẵn nên là 0") if chan_le ==0 else print("Bit kiểm tra chẵn nên là 1 ")            
print("Thoát chương trình")