import csv


class Xarajat:
    file = "4-dars/xarajatlar.csv"

    def __init__(self, tur, summa, sana):
        self.tur = tur
        self.summa = summa
        self.sana = sana

    def korish(self):
        print("***Xarajat haqida***")
        print(f"Turi: {self.tur}")
        print(f"Summasi: {self.summa}")
        print(f"Sana: {self.sana}")
        print("-" * 20)

    def __str__(self):
        return f"{self.sana} - {self.tur} - {self.summa}"

    @classmethod
    def qoshish(cls, tur, summa, sana):
        with open(cls.file, "a", encoding="UTF-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([tur, summa, sana])
            print("Xarajat muvaffaqiyatli qo'shildi!")

    @classmethod
    def all(cls):
        with open(cls.file, "r", encoding="UTF-8") as f:
            data = csv.DictReader(f)
            xarajatlar = []
            for x in data:
                e = Xarajat(x["tur"], float(x["summa"]), x["sana"])
                xarajatlar.append(e)
        return xarajatlar

    @classmethod
    def jami(cls):
        xarajatlar = cls.all()
        yigindi = 0
        for x in xarajatlar:
            yigindi += x.summa
        return yigindi


while True:
    print("====Menu====")
    print("1 Barcha xarajatlar")
    print("2 Xarajat qo'shish")
    print("3 Jami sarflangan pul")
    print("4 Chiqish")
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        xarajatlar = Xarajat.all()
        for x in xarajatlar:
            x.korish()

    elif tanlov == "2":
        tur = input("Xarajat turi: ")
        summa = int(input("Summa: "))
        sana = input("Sana (masalan 2026-10-30): ")
        Xarajat.qoshish(tur, summa, sana)

    elif tanlov == "3":
        print(f"Jami sarflangan: {Xarajat.jami()} so'm")

    elif tanlov == "4":
        print("Dastur tugadi")
        break