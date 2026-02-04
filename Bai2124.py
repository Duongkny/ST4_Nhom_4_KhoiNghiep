def tim_duong_logistics(do_thi, bat_dau, dich):
    hien_tai = bat_dau
    lo_trinh = [hien_tai]
    tong_km = 0
    
    print(f"--- Startup Logistics: Lộ trình đi đến {dich} ---")
    
    while hien_tai != dich:
        lua_chon = do_thi.get(hien_tai)
        if not lua_chon:
            print(f"Thất bại: Bị kẹt tại {hien_tai}!")
            break
            
        
        ke_tiep, km = min(lua_chon.items(), key=lambda x: x[1])
        
        tong_km += km
        hien_tai = ke_tiep
        lo_trinh.append(ke_tiep)
        print(f" -> Di chuyển đến {ke_tiep} (Tốn thêm {km}km)")

    if lo_trinh[-1] == dich:
        print(f"XONG! Lộ trình: {' -> '.join(lo_trinh)} | Tổng: {tong_km}km")


so_do_thuc_te = {
    'Kho Chính': {
        'Cửa hàng (4)': 2, 
        'Điểm trung chuyển (5)': 4
    },
    'Cửa hàng (4)': {
        'Điểm trung chuyển (5)': 4
    },
    'Điểm trung chuyển (5)': {}
}

tim_duong_logistics(so_do_thuc_te, 'Kho Chính', 'Điểm trung chuyển (5)')