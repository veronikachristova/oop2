# class MojaKalkulacka:
#     @staticmethod
#     def sucet(a, b):
#         return a + b
#
#     def sucin(a, b):
#         return a * b
#
# calculator = MojaKalkulacka()
#
# print(calculator.sucet(2, 3))
# print(calculator.sucin(a, 4))


class Zviera:
    def hlas(self):
        raise NotImplementedError("potrieda musi implementovat metodu")

    def pocet_noh(self):
        raise NotImplementedError("potrieda musi implementovat metodu")

class Pes(Zviera):
    def hlas(self):
        return "Haf"
    def nohy(self):
        return "4"

class Kohut(Zviera):
    def hlas(self):
        return "kikiriki"
    def nohy(self):
        return "2"

class Macka(Zviera):
    def hlas(self):
        return "Miau"
    def nohy(self):
        return "4"

def vydaj_zvuk(zviera):
    return zviera.hlas()

def udaj_pocet_noh(zviera):
    return zviera.nohy()

pes  = Pes()
kohut = Kohut()
macka = Macka()

for zviera in [pes, kohut, macka]:
    print(vydaj_zvuk(zviera))

for zviera in [pes, kohut, macka]:
    print(udaj_pocet_noh(zviera))

