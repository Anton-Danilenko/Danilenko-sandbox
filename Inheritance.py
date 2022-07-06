class qa:
    def can_test(self):
        print("Могу тестировать")

class anton(qa):
    def can_fly(self):
        print("Могу летать")
y = qa()
x = anton()
x.can_test()
x.can_fly()
