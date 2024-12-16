from barcode import ITF
from barcode.writer import SVGWriter

if __name__ == '__main__':
    num = input("Podaj numer: ")
    if len(str(num)) > 16:
        raise ValueError("Max number length is 16 digits. See https://pl.wikipedia.org/wiki/Przeplatany_2_z_5 ")
    with open("code.svg", 'wb') as f:
        ITF(str(num), writer=SVGWriter()).write(f)
    print("Kod zapisany w pliku code.svg")