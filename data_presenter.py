# Open cupcake file 
open_file = open("CupcakeInvoices.csv")

# Loop through data and print each row
for line in open_file:
    print(line)

# Loop and print type of cupcakes
open_file.seek(0)
for line in open_file:
    line = line.strip()
    type = line.split(',')
    print(type[2])

# Print total of each invoice
open_file.seek(0)
for line in open_file:
    line = line.strip()
    data = line.split(',')
    total = int(data[3]) * float (data[4])
    print(total)

# Print out total for all invoice combined
open_file.seek(0)
for line in open_file:
    data = line.split(',')
    total = total + (int(data[3]) * float(data[4]))
print(total)

open_file.close()