class Person:
    species = "Human"  # 클래스 변수, 모든 객체가 공유

    def __init__(self, name):
        self.name = name  # 인스턴스 속성

p1 = Person("winiee")
p2 = Person("Minam")

