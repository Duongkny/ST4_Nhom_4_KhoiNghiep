import heapq

def thuat_toan_a_star(ma_tran, diem_dau, diem_cuoi):
    hang_doi_uu_tien = []
    
    heapq.heappush(hang_doi_uu_tien, (0, diem_dau))
    
    duong_di = {}
    g_score = {diem_dau: 0}
    
    
    def tinh_h(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    print(f"--- Đang tìm đường tối ưu bằng A* từ {diem_dau} ---")

    while hang_doi_uu_tien:
        chi_phi_f, hien_tai = heapq.heappop(hang_doi_uu_tien)

        if hien_tai == diem_cuoi:
            print("Đã tìm thấy đường đi ngắn nhất!")
            return xay_dung_lo_trinh(duong_di, diem_cuoi)

        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            lang_gieng = (hien_tai[0] + dx, hien_tai[1] + dy)
            
            
            if 0 <= lang_gieng[0] < len(ma_tran) and 0 <= lang_gieng[1] < len(ma_tran[0]):
                if ma_tran[lang_gieng[0]][lang_gieng[1]] == 1:
                    continue
                
                chi_phi_g_moi = g_score[hien_tai] + 1
                
                if lang_gieng not in g_score or chi_phi_g_moi < g_score[lang_gieng]:
                    g_score[lang_gieng] = chi_phi_g_moi
                    f_score = chi_phi_g_moi + tinh_h(lang_gieng, diem_cuoi)
                    duong_di[lang_gieng] = hien_tai
                    heapq.heappush(hang_doi_uu_tien, (f_score, lang_gieng))
    return None

def xay_dung_lo_trinh(duong_di, hien_tai):
    ket_qua = []
    while hien_tai in duong_di:
        ket_qua.append(hien_tai)
        hien_tai = duong_di[hien_tai]
    return ket_qua[::-1]


ban_do = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

lo_trinh = thuat_toan_a_star(ban_do, (0, 0), (4, 4))
print(f"Lộ trình đề xuất: (0, 0) -> {' -> '.join(map(str, lo_trinh))}")