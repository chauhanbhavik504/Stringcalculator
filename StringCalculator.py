class StringCalculator:
    def __init__(self):
        self.summ=0
        self.small=0
        self.cap=0
        self.counter=0
    def add(self,s):
        s = s.split(",")
        a = []
        for i in s:
            if i.lstrip("-").isdigit():
                if i.isdigit():
                    pass
                else:
                    a.append(i)
                    self.counter+=1
        if self.counter>1:
            raise TypeError(f"Negatives not Allowed {a}")
        for i in s:
            if i.isdigit():
                if int(i) >=1000:
                    continue
            if i.lstrip("-").isdigit():
                if i.isdigit():
                    print("")
                else:
                    print("Negative")
            if i.isdigit():
                self.summ=self.summ+int(i)
            if i.isalpha():
                if i.islower():
                    self.small = ord(i) - 96
                    self.summ+=self.small
            if i.isalpha():
                if i.isupper():
                    self.cap = ord(i) - 64
                    self.summ+=self.cap
        return self.summ

a = StringCalculator()
s=input("Enter the string: ")
print(a.add(s))
