import csv

#column = int(input("Enter the castle number\n")) - 1
#num_soldiers = int(input("Enter the number of soldiers you want to send to that castle\n"))

data = []
with open('riddlers-castle - Sheet1.csv', encoding = 'utf-8') as f:
    read_file = csv.reader(f)
    data = list(read_file)
    del data[0]

dist_soldiers = [ 1, 3,
                  2, 3,
                  3, 3,
                  4, 3,
                  5, 3,
                  6, 10,
                  7, 30,
                  8, 35,
                  9, 7,
                  10, 3
                  ]
    
def prob(castle_num, num_soldiers):
    counter = 0
    castle_num -= 1
    for row in data:
        if num_soldiers > int(row[castle_num]):
            counter += 1
    return float(counter / 1382)

index = 0
expected_value = 0

while index < 20:
    probability = prob(dist_soldiers[index], dist_soldiers[index + 1])
    expected_value += probability * dist_soldiers[index]
    index += 2

print("The expected value of your score is " + str(expected_value))


