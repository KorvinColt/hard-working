class Животное:
    def __init__(self, имя, вид, команды, дата_рождения):
        self.__имя = имя
        self.__вид = вид
        self.__команды = команды
        self.__дата_рождения = дата_рождения

    def get_имя(self):
        return self.__имя

    def set_имя(self, имя):
        self.__имя = имя