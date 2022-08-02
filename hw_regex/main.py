import re
import csv
from functions import get_data, get_new_data, upload_data


def main():
    data = get_data('hw_regex/phonebook_raw.csv')
    new_data = get_new_data(data)
    upload_data(new_data)

if __name__ == '__main__':
    main()