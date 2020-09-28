# task 1
# Напишите функцию для парсинга номерных знаков автомоблей Украины (стандарты - AА1234BB, 12 123-45AB, a12345BC)
# с помощью регулярных выражений. Функция принимает строку и возвращает None если строка не является номерным знаком.
# Если является номерным знаком - возвращает саму строку.
import re


def main():
    def find_license(string):
        patterns = [r'^[A-Z]{2}\d{4}[A-Z]{2}$', r'^\d{2}\s\d{3}\-\d{2}[A-Z]{2}$', r'^[a-z]\d{5}[A-Z]{2}$']
        for pattern in patterns:
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
    _reg = []

    def __init__(self, patterns):
        self.patterns = patterns

    @property
    def patterns(self):
        return self._reg

    @patterns.setter
    def patterns(self, value):
        if not isinstance(value, list):
            raise Exception
        for pattern in value:
            self._reg.append(re.compile(pattern))

    def find_licenses(self, text):
        result = []
        for reg in self._reg:
            items = re.findall(reg, text)
            if items:
                result.extend(items)

        if not result:
            print("This text does not contain any license plates")
        else:
            return result

    @staticmethod
    def show_license_plates(licenses):
        counter = 1
        result = ''
        for item in licenses:
            result += f"{int(counter)}. {item}\n"
            counter += 1
        print(result)


def main():

    license = License([r'[A-Z]{2}\d{4}[A-Z]{2}', r'\d{2}\s\d{3}\-\d{2}[A-Z]{2}', r'[a-z]\d{5}[A-Z]{2}'])

    licenses = license.find_licenses('A RegEx, AA1234BB, or Regular Expression, 12 123-45AB, is a sequence \
              12 123-45AB of characters that forms a search pattern a12345BC')
    if licenses is None:
        return

    license.show_license_plates(licenses)


if __name__ == '__main__':
    main()
