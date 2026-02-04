def phan_cong_tham_lam():
    
    ma_tran_thoi_gian = [
        [10, 12, 19, 21, 15],
        [15, 18, 25, 10, 12],
        [20, 11, 15, 13, 20],
        [14, 15, 12, 16, 11],
        [12, 10, 18, 20, 15]
    ]
    
    so_nv = 5
    so_cv = 5
    
    nv_da_giao = [False] * so_nv
    cv_da_lam = [False] * so_cv
    tong_thoi_gian = 0
    ket_qua = []

    print("--- QUÁ TRÌNH PHÂN VIỆC THEO NGUYÊN LÝ THỨ TỰ ---")

    for _ in range(so_nv):
        thoi_gian_min = float('inf')
        chon_nv = -1
        chon_cv = -1
        
        
        for i in range(so_nv):
            if not nv_da_giao[i]:
                for j in range(so_cv):
                    if not cv_da_lam[j]:
                        if ma_tran_thoi_gian[i][j] < thoi_gian_min:
                            thoi_gian_min = ma_tran_thoi_gian[i][j]
                            chon_nv = i
                            chon_cv = j
        
       
        nv_da_giao[chon_nv] = True
        cv_da_lam[chon_cv] = True
        tong_thoi_gian += thoi_gian_min
        ket_qua.append(f"Nhân viên {chon_nv + 1} -> Công việc {chon_cv + 1} ({thoi_gian_min} giờ)")
        print(f"Đã giao: NV{chon_nv + 1} làm CV{chon_cv + 1} trong {thoi_gian_min}h")

    print("-" * 45)
    print("PHƯƠNG ÁN PHÂN CÔNG CUỐI CÙNG:")
    for kq in ket_qua:
        print(kq)
    print(f"\n=> Tổng thời gian hoàn thành của team: {tong_thoi_gian} giờ")


phan_cong_tham_lam()