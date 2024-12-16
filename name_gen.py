from faker import Faker
from random import choice


faker_in = Faker(locale='en_IN')
faker_us = Faker(locale='en_US')

def generate_names():
    data_path = "names_mixed.txt"
    out = []
    for i in range(32_500):
        if choice([0, 1]):
            out.append(f'{faker_in.first_name().lower()}\n')
        else:
            out.append(f'{faker_us.first_name().lower()}\n')
    out[-1] = out[-1].replace("\n","")
    with open(data_path, 'w+') as file:
        file.writelines(out)

def main():
    generate_names()


if __name__ == "__main__":
    main()
