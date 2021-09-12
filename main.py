def csv_reader(header=False, separator=','):
    csv_data_list = []
    with open('csv_file_for_reading.csv', 'r') as csv_file:
        for line in csv_file:
            csv_data_list.append(line.split(separator))
    header = csv_data_list[0]



if __name__ == '__main__':
    first_line_as_header = True
    separate = ','
    csv_reader(first_line_as_header, separate)
