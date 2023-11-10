from datetime import datetime, timedelta

# Class to hold information about parked vehicles
class ParkedVehicle:
    def __init__(self, plate_number, floor, place, entry_time):
        self.plate_number = plate_number
        self.floor = floor
        self.place = place
        self.entry_time = entry_time

# Function to calculate parking duration and fee
def calculate_parking_fee(entry_time, exit_time):
    park_duration = exit_time - entry_time

    if park_duration <= timedelta(minutes=30):
        return 0  # Ücretsiz
    elif timedelta(hours=0.5) < park_duration <= timedelta(hours=1):
        return 20  # 20 TL
    elif timedelta(hours=1) < park_duration <= timedelta(hours=2):
        return 40  # 40 TL
    elif timedelta(hours=2) < park_duration <= timedelta(hours=5):
        return 80  # 100 TL
    elif timedelta(hours=5) < park_duration <= timedelta(hours=11):
        return 150  # 150 TL

# Function to display parking space status for each floor
def display_parking_status(floor, available_spaces):
    print(f"Kat {floor} durumu:")
    for i, status in enumerate(available_spaces, start=1):
        if status == 1:
            print(f"Park Yeri {i}: Boş")
        else:
            print(f"Park Yeri {i}: Dolu")

# Function for vehicle entry
def vehicle_entry(parked_vehicles, available_spaces):
    floor = int(input("Lütfen kat numarasını giriniz: "))
    
    if floor < 1 or floor > KAT_SAYISI:
        print("Geçersiz kat numarası!")
        return
    
    if 1 in available_spaces[floor - 1]:  # Check if at least one space is available
        print(f"Boş park yerleri (Kat {floor}):")
        for i, status in enumerate(available_spaces[floor - 1], start=1):
            if status == 1:
                print(f"Park Yeri {i}")

        place = int(input("Lütfen aracınızı park etmek istediğiniz yeri seçiniz: "))
        if 1 <= place <= 10 and available_spaces[floor - 1][place - 1] == 1:
            available_spaces[floor - 1][place - 1] = 0
            plate_number = input("Lütfen aracınızın plaka numarasını giriniz: ")
            entry_time = datetime.now()
            parked_vehicle = ParkedVehicle(plate_number, floor, place, entry_time)
            parked_vehicles.append(parked_vehicle)
            print(f"Araç başarıyla park edildi! Plaka Numarası: {plate_number} - Kat: {floor} - Park Yeri: {place}")

            # Display entry time
            print(f"Giriş Saati: {entry_time.strftime('%H:%M:%S')}")
        else:
            print("Geçersiz park yeri numarası!")
    else:
        print(f"Seçilen katta boş park yeri bulunmamaktadır.")

# Function for vehicle exit
def vehicle_exit(parked_vehicles, available_spaces):
    floor = int(input("Lütfen kat numarasını giriniz: "))

    if floor < 1 or floor > KAT_SAYISI:
        print("Geçersiz kat numarası!")
        return

    if 0 in available_spaces[floor - 1]:
        print(f"Dolu park yerleri (Kat {floor}):")
        for i, status in enumerate(available_spaces[floor - 1], start=1):
            if status == 0:
                print(f"Park Yeri {i} - Araç Plakası: {parked_vehicles[i - 1].plate_number}")

        place = int(input("Lütfen aracınızı çıkarmak istediğiniz yeri seçiniz: "))
        if 1 <= place <= 10 and available_spaces[floor - 1][place - 1] == 0:
            available_spaces[floor - 1][place - 1] = 1
            exit_time = datetime.now()
            parked_vehicle = parked_vehicles.pop(place - 1)
            print(f"Araç başarıyla çıkartıldı! Plaka Numarası: {parked_vehicle.plate_number} - Kat: {floor} - Park Yeri: {place}")

            # Display exit time and calculate parking fee
            print(f"Çıkış Saati: {exit_time.strftime('%H:%M:%S')}")
            print(f"Park Süresi: {exit_time - parked_vehicle.entry_time}")
            
            fee = calculate_parking_fee(parked_vehicle.entry_time, exit_time)
            print(f"Ücret: {fee} TL")
        else:
            print("Geçersiz park yeri numarası!")
    else:
        print(f"Seçilen katta dolu park yeri bulunmamaktadır.")

# Global variables for parking status
KAT_SAYISI = 5
müsait_park_yeri = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Vector to hold parked vehicles
parked_vehicles = []

# Main program
# Kullanıcı girişi
kullanici_adi = input("Kullanıcı adı: ")
sifre = input("Şifre: ")

# Kullanıcı adı ve şifrenin doğrulanması
if kullanici_adi == "Mall" and sifre == "Autopark":
    # Kullanıcı girişi başarılı
    print(f"Hoşgeldiniz Sn. {kullanici_adi} {sifre}")

    while True:
        # Ana menü
        print("Uygulama Aşamaları:")
        print("1 - Park Yeri Durumu")
        print("2 - Araç Girişi")
        print("3 - Araç Çıkışı")
        print("4 - Program Sonlandırma")

        secim = int(input("Lütfen yapmak istediğiniz işlemi seçiniz: "))

        if secim == 1:
            for i in range(1, KAT_SAYISI + 1):
                display_parking_status(i, müsait_park_yeri[i - 1])
        elif secim == 2:
            vehicle_entry(parked_vehicles, müsait_park_yeri)
        elif secim == 3:
            vehicle_exit(parked_vehicles, müsait_park_yeri)
        elif secim == 4:
            break
        else:
            print("Hatalı seçim!")
else:
    # Kullanıcı girişi başarısız
    print("Kullanıcı adı veya şifre hatalı!")