from abc import ABC, abstractmethod

# 1. Amaliyot (Implementation) qismi - Bildirishnoma yuborish mexanizmlari
# Bu qism qanday yuborishni (SMS, Mobil Ilova) aniqlaydi.
class YuborishMexanizmi(ABC): # SenderMechanism
    @abstractmethod
    def yubor(self, xabar: str) -> str:
        """Bildirishnomani yuborish usuli."""
        pass

class SMSYuboruvchi(YuborishMexanizmi): # SMSSender
    def yubor(self, xabar: str) -> str:
        return f"[SMS] Yuborildi: '{xabar}'"

class MobilIlovaBildiruvchi(YuborishMexanizmi): # MobileAppNotifier (Push Notifications)
    def yubor(self, xabar: str) -> str:
        return f"[Mobil Ilova] Yuborildi: '{xabar}'"

# 2. Abstraktsiya (Abstraction) qismi - Turli xodimlar uchun bildirishnoma turlari
# Bu qism kimga va qanday turdagi bildirishnoma ketayotganini aniqlaydi.
class XodimBildirishnomasi(ABC): # StaffNotification
    def __init__(self, mexanizm: YuborishMexanizmi):
        """
        Xodim bildirishnomasi uchun abstrakt klass.
        U o'ziga bildirishnoma yuborish mexanizmini oladi.
        """
        self._mexanizm = mexanizm

    @abstractmethod
    def yetkaz(self, xabar_matni: str) -> str:
        """Xabarni tegishli xodimga yetkazish."""
        pass

class AdminBildirishnomasi(XodimBildirishnomasi):
    def yetkaz(self, xabar_matni: str) -> str:
        return self._mexanizm.yubor(f"Admin uchun: {xabar_matni}")

class OshpazBildirishnomasi(XodimBildirishnomasi):
    def yetkaz(self, xabar_matni: str) -> str:
        return self._mexanizm.yubor(f"Oshpaz uchun: {xabar_matni}")

class MenejerBildirishnomasi(XodimBildirishnomasi):
    def yetkaz(self, xabar_matni: str) -> str:
        return self._mexanizm.yubor(f"Menejer uchun: {xabar_matni}")


# Foydalanish qismi (Client Code) - Bog'cha tizimida
# Bu yerda biz abstraction va implementationni birlashtiramiz.
if __name__ == "__main__":
    print("--- Bog'cha tizimi xodimlari uchun bildirishnomalar ---")

    # Mavjud yuborish mexanizmlari
    sms_service = SMSYuboruvchi()
    mobile_app_service = MobilIlovaBildiruvchi()

    # Har bir rol uchun bildirishnomalar yaratamiz va ularga yuborish mexanizmlarini bog'laymiz

    # Admin
    admin_sms_notifier = AdminBildirishnomasi(sms_service)
    print(admin_sms_notifier.yetkaz("Yangi oshpaz tizimga qo'shildi. Ma'lumotlarni tekshiring."))

    admin_app_notifier = AdminBildirishnomasi(mobile_app_service)
    print(admin_app_notifier.yetkaz("Muhim tizim yangilanishi mavjud. Ilovani yangilang."))

    # Oshpaz
    oshpaz_sms_notifier = OshpazBildirishnomasi(sms_service)
    print(oshpaz_sms_notifier.yetkaz("Omborda guruch tugayapti. Buyurtma berish zarur."))

    oshpaz_app_notifier = OshpazBildirishnomasi(mobile_app_service)
    print(oshpaz_app_notifier.yetkaz("Ertangi kun menyusi tasdiqlandi. Ko'rib chiqing."))

    # Menejer
    menejer_sms_notifier = MenejerBildirishnomasi(sms_service)
    print(menejer_notifier_sms.yetkaz("Oylik moliyaviy hisobot tayyor. Kirib ko'ring."))

    menejer_app_notifier = MenejerBildirishnomasi(mobile_app_service)
    print(menejer_app_notifier.yetkaz("Yangi yig'ilish rejalashtirildi. Kalendarni tekshiring."))

    print("\n--- Kengaytirish imkoniyatlari ---")
    # Agar Telegram orqali yuborish kerak bo'lsa, yangi mexanizm qo'shish juda oson:
    class TelegramYuboruvchi(YuborishMexanizmi):
        def yubor(self, xabar: str) -> str:
            return f"[Telegram] Yuborildi: '{xabar}'"

    telegram_service = TelegramYuboruvchi()
    # Endi Admiga Telegram orqali bildirishnoma yuborishimiz mumkin
    admin_telegram_notifier = AdminBildirishnomasi(telegram_service)
    print(admin_telegram_notifier.yetkaz("Tizimda g'ayritabiiy harakatlar aniqlandi. Zudlik bilan kirish tekshiruvi lozim."))