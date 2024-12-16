from barcode import ITF
from barcode.writer import SVGWriter


class Barcode:
    def __init__(self, number : int):
        """
        :param number: barcode number that will be encoded.
        """
        # validation
        if len(str(number)) > 16:
            raise ValueError("Max number length is 16 digits. See https://pl.wikipedia.org/wiki/Przeplatany_2_z_5 ")
        self.number = number

    def generate(self):
        with open("code.svg", 'wb') as f:
            ITF(str(self.number), writer=SVGWriter()).write(f)

def main():
    try:
        num = int(input("Podaj numer: "))
    except ValueError:
        print("Nieprawidłowy numer")
    Barcode(num).generate()
    print("Kod zapisany w pliku code.svg")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
