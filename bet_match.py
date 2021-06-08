class BetMatch:
    def __init__(self):
        self.accuracy_k = 1 #округление процентов
        self.accuracy_p = 2 #округление коэффициентов
        self.k = [] #список кефов

    def addK(self, k):
        #добавить кеф в список
        if not self.testFloat(k):
            return False
        fk = float(k)
        if fk > 0:
            self.k.append(fk)
            return True
        else:
            return False


    def testFloat(self, x):
        try:
            x = float(x)
            return True
        except:
            return False

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
            return int(s-100) #все хорошо маржа >0
        elif s == 0:
            return 0 #нулевая маржа
        else:
            return False #отрицательной маржи не может быть
