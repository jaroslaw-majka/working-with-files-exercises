def csv_reader():
    with open('csv_file_for_reading.csv', 'r') as csv_file:
        csv_data_list = csv_file.readlines()

    print(csv_data_list)


if __name__ == '__main__':
    csv_reader()
