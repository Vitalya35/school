# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding,
# который будет задавать целочисленный атрибут этажности self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию


class Buiding:
    def __init__(self, numberOfFloors: int, buildingType: str):
        if not isinstance(numberOfFloors, int):
            raise TypeError('numberOfFloors должен быть целым числом')
        if not isinstance(buildingType, str):
            raise TypeError('buildingType должен быть строкой')
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

    def __gt__(self, other):
        return self.numberOfFloors > other.numberOfFloors and self.buildingType > other.buildingType

skyscraper = Buiding(50, 'skyscraper')
residential_building = Buiding(10, 'residential building')
print(skyscraper == residential_building)
print(skyscraper > residential_building)



