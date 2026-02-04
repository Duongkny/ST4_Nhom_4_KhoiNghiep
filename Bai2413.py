from collections import deque

def tim_luong_nguoi_dung_ngan_nhat(so_do_app, bat_dau, ket_thuc):
    
    hang_doi = deque([(bat_dau, [bat_dau])])
    da_tham = {bat_dau}

    print(f"--- Đang tìm luồng từ '{bat_dau}' đến '{ket_thuc}' ---")

    while hang_doi:
        (nut_hien_tai, duong_di) = hang_doi.popleft()

        
        if nut_hien_tai == ket_thuc:
            return duong_di

        
        for trang_ke in so_do_app.get(nut_hien_tai, []):
            if trang_ke not in da_tham:
                da_tham.add(trang_ke)
                hang_doi.append((trang_ke, duong_di + [trang_ke]))
    
    return None


so_do_app = {
    'Trang chủ': ['Tìm kiếm', 'Danh mục', 'Khuyến mãi'],
    'Tìm kiếm': ['Chi tiết sản phẩm'],
    'Danh mục': ['Chi tiết sản phẩm', 'Giỏ hàng'],
    'Khuyến mãi': ['Chi tiết sản phẩm'],
    'Chi tiết sản phẩm': ['Giỏ hàng'],
    'Giỏ hàng': ['Thanh toán'],
    'Thanh toán': []
}


ket_qua = tim_luong_nguoi_dung_ngan_nhat(so_do_app, 'Trang chủ', 'Thanh toán')

if ket_qua:
    print("KẾT QUẢ TỐI ƯU:")
    print(" -> ".join(ket_qua))
    print(f"Số bước tối thiểu: {len(ket_qua) - 1}")
else:
    print("Không tìm thấy đường đi!")