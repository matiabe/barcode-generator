import barcode
from barcode.writer import ImageWriter

def generate_barcode():
    try:
        # Prompt the user for a 12-digit numeric code
        number = input("Enter a 12-digit code to generate the barcode: ")
        
        # Validate input
        if len(number) != 12 or not number.isdigit():
            raise ValueError("UPC code must be exactly 12 digits and numeric.")
        
        # Get the barcode class for UPC
        barcode_format = barcode.get_barcode_class('upc')
        
        # Generate the barcode with an image writer
        my_barcode = barcode_format(number, writer=ImageWriter())
        
        # Save the barcode as an image file
        filename = my_barcode.save("generated_barcode")
        print(f"Barcode successfully generated and saved as: {generate_barcode}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    generate_barcode()
