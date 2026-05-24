import datetime

patient_name = input("Nhập tên bệnh nhân: ")
year_of_birth = int(input("Nhập năm sinh: "))
number_of_sick_days = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
price = float(input("Nhập chi phí khám: "))

if patient_name.strip() == "" or (year_of_birth <= 1900 and year_of_birth >= datetime.date.today().year) or number_of_sick_days < 0 or (temperature <= 30 and temperature >= 45) or price < 0:
    print("Lỗi: Dữ liệu không hợp lệ!!!")
else:
    count_patient_age = datetime.date.today().year - year_of_birth
    total_price = price + price * 0.1

    if temperature > 38 and number_of_sick_days > 3:
        health_classification = "Nguy hiểm"
    elif temperature > 38:
        health_classification = "Sốt cao"
    elif temperature > 37.5:
        health_classification = "Sốt nhẹ"
    else:
        health_classification = "Bình thường"


    if health_classification == "Nguy hiểm":
        if count_patient_age > 60:
            prioritize = "Cấp cứu"
        else:
            prioritize = "Ưu tiên cao"
    else:
        prioritize = "Bình thường"


    check_total_price = "Cao" if total_price > 500000 else "Thấp"

    print()
    print("--- KẾT QUẢ ---")
    print(f"Tên: {patient_name}")
    print(f"Tuổi: {count_patient_age}")
    print(f"Nhiệt độ: {temperature} °C")
    print(f"Số ngày bệnh: {number_of_sick_days}", end="\n\n")
    print(f"Tình trạng: {health_classification}")
    print(f"Mức độ ưu tiên: {prioritize}", end="\n\n")
    print(f"Tổng chi phí: {total_price} VND")
    print(f"Mức chi phí: {check_total_price}")
