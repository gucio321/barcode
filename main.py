import barcode.itf as itf

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
        itf.ITF(str(self.number))

def main():
    Barcode(123).generate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
