class BetMatch:
    def __init__(self):
        self.accuracy_k = 1 #округление процентов
        self.accuracy_p = 2 #округление коэффициентов
        self.k = [] #список кефов

    def addK(self, k):
        #добавить кеф в список
        try:
            fk = float(k)
            if fk > 0:
                self.k.append(fk)
            else:
                return False
        except:
            return False
        return True

    def clearK(self):
        #очистить список кефов
        self.k = []

    def otherSide(self):
        #считаем другое плечо и округляем
        if len(self.k) != 1:
            return False
        elif self.k[0] <=0:
            return False
        p = 1 / self.k[0] * 100
        x = 1 / (100 - p) * 100
        return round(x, self.accuracy_p)

    def calcMarja(self):
        if len(self.k) <= 1:
            return False
        p = [1 / i * 100 for i in self.k] #расчитаем кефы в проценты
        s = sum(p)
        if s > 100:
            return round(s - 100, self.accuracy_p) #все хорошо маржа >0
        elif s == 0:
            return 0 #нулевая маржа
        else:
            return False #отрицательной маржи не может быть
