''' Analyse barcodes '''

# Get the barcode
# ask in a loop to force the user to enter a correct one
get_barcode = True
while get_barcode == True:
    barcode = input("Enter a 13 digit barcode: ")
    if len(barcode) == 13:
        get_barcode = False
    else:
        print("Barcode must be 13 digits long")

print(f"Country code: {barcode[0:2]}")
print(f"Manufacturer code: {barcode[2:7]}")
print(f"Product code: {barcode[7:12]}")
print(f"Check digit: {barcode[12]}")
