# task 1
# Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC)
# с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является номерным знаком.
# Если является номерным знаком - возвращает саму строку.
import re


def main():
    def find_license(string):
        pattern = r'^\w{1,2}.\d{3}.\w{1,4}$'
        regexp = re.compile(pattern)
        if re.search(regexp, string):
            return string

    print(find_license('AA1234BB'))
    print(find_license('12 123-45AB'))
    print(find_license('a12345BC'))


if __name__ == '__main__':
    main()


# task 2
# * Напишите класс, который выбирает из произвольного текста номерные знаки и возвращает их в
# виде пронумерованного списка с помощью регулярных выражений.

class License:
    _reg = None

    def __init__(self, pattern=r'\w{1,2}.\d{3}.\w{1,4}'):
        self.pattern = pattern

    @property
    def pattern(self):
        return self._reg

    @pattern.setter
    def pattern(self, value):
        if not isinstance(value, str):
            raise Exception
        self._reg = re.compile(value)

    def find_licenses(self, text):
        items = re.findall(self._reg, text)
        if not items:
            print("This text does not contain any license plates")
        else:
            return items

    @staticmethod
    def show_license_plates(licenses):
        counter = 1
        result = ''
        for item in licenses:
            result += f"{int(counter)}. {item}\n"
            counter += 1
        print(result)


def main():
    l = License()

    licenses = l.find_licenses('A RegEx, AA1234BB, or Regular Expression, 12 123-45AB, is a sequence 12 123-45AB of \
    characters that forms a search pattern a12345BC')

    l.show_license_plates(licenses)


if __name__ == '__main__':
    main()
