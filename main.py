import calendar

def top_dushanba_kunlar(yil):
    dushanba_kunlar = []
    for oy in range(1, 13):
        kalendariy = calendar.monthcalendar(yil, oy)
        for hafta in kalendariy:
            if hafta[0] != 0 and calendar.weekday(yil, oy, hafta[0]) == 1:
                dushanba_kunlar.append(f"{yil}-{oy}-{hafta[0]}")
    return dushanba_kunlar

yil = 2026
print(top_dushanba_kunlar(yil))
