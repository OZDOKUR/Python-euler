import time

def pomodoro_timer(duration):
    """
    Pomodoro tekniği için zamanlayıcı işlevi
    """
    start_time = time.time()
    end_time = start_time + duration * 60  # Dakika cinsinden süre

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        print(f"Kalan süre: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Pomodoro tamamlandı!")

# Örnek kullanım
pomodoro_timer(25)  # 25 dakikalık bir pomodoro çalışması
