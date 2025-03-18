def pacet_vacation_planner(destinations, budget):
    """
    Merencanakan liburan di Pacet dengan algoritma backtracking
    
    Args:
        destinations: List of tuples (nama_tempat, biaya_masuk, biaya_transportasi, durasi_jam)
        budget: Anggaran maksimal dalam ribu rupiah
    
    Returns:
        List of valid vacation plans
    """
    result = []
    current_plan = []
    
    def backtrack(index, remaining_budget, current_plan):
        # Jika sudah memilih 3 destinasi, tambahkan ke hasil
        if len(current_plan) == 3:
            result.append(current_plan.copy())
            return
        
        # Jika sudah melihat semua destinasi atau budget habis, berhenti
        if index >= len(destinations) or remaining_budget <= 0:
            return
        
        # Pilihan 1: Pilih destinasi saat ini
        dest_name, entrance_fee, transport_cost, duration = destinations[index]
        total_cost = entrance_fee + transport_cost
        
        if total_cost <= remaining_budget:
            current_plan.append((dest_name, total_cost, duration))
            # Lanjutkan ke destinasi berikutnya
            backtrack(index + 1, remaining_budget - total_cost, current_plan)
            # Kembalikan state (backtrack)
            current_plan.pop()
        
        # Pilihan 2: Lewati destinasi saat ini
        backtrack(index + 1, remaining_budget, current_plan)
    
    # Mulai backtracking dari index 0, budget penuh
    backtrack(0, budget, current_plan)
    return result

# Data destinasi wisata di Pacet
# Format: (nama_tempat, biaya_masuk, biaya_transportasi, durasi_jam)
pacet_destinations = [
    ("Air Terjun Dlundung", 25, 35, 2),
    ("Pemandian Air Panas Padusan", 20, 30, 3),
    ("Taman Wisata Pacet Mini Park", 15, 25, 2),
    ("Kebun Strawberry Pacet", 10, 30, 1.5),
    ("Candi Jolotundo", 10, 40, 1),
    ("Wana Wisata Pacet", 15, 35, 2),
    ("Goa Lowo", 20, 45, 1.5),
    ("Bukit Jamur", 15, 50, 2.5),
]

# Cari semua rencana liburan yang valid
valid_plans = pacet_vacation_planner(pacet_destinations, 500)

# Tampilkan hasil
print(f"Ditemukan {len(valid_plans)} rencana liburan dengan budget ≤ 500 ribu:")
for i, plan in enumerate(valid_plans, 1):
    total_cost = sum(cost for _, cost, _ in plan)
    total_duration = sum(duration for _, _, duration in plan)
    print(f"\nRencana {i}:")
    print(f"Total biaya: Rp {total_cost}.000")
    print(f"Total durasi: {total_duration} jam")
    print("Destinasi:")
    for dest_name, cost, duration in plan:
        print(f"- {dest_name} (Rp {cost}.000, {duration} jam)")