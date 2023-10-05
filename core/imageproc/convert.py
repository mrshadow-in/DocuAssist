import os
import pytesseract
from PIL import Image, ImageFile
import fitz  # PyMuPDF for PDF handling
import io  # Import the io module

# Initialize PIL and PyMuPDF
ImageFile.LOAD_TRUNCATED_IMAGES = True


def convert_to_text(input_file):
    try:
        # Check the file extension to determine the type
        file_extension = os.path.splitext(input_file)[1].lower()

        if file_extension in ['.png', '.jpg', '.jpeg']:
            image = Image.open(input_file)
            text = pytesseract.image_to_string(image)
        elif file_extension == '.pdf':
            pdf_document = fitz.open(input_file)
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)

                # Extract images from the page
                images = page.get_images(full=True)
                for img_index, img in enumerate(images):
                    xref = img[0]
                    base_image = pdf_document.extract_image(xref)
                    image_data = base_image["image"]

                    # Create a PIL Image from the image data
                    image = Image.open(io.BytesIO(image_data))

                    # Perform OCR on the image
                    image_text = pytesseract.image_to_string(image)
                    text += image_text

        else:
            return "Unsupported file format."

        # Save the extracted text to temp.txt
        with open('temp.txt', 'w', encoding='utf-8') as temp_file:
            temp_file.write(text)

        return "Text extracted and saved to temp.txt"
    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == '__main__':
    input_file = 'medrepot.pdf'  # Replace with the actual file path
    result = convert_to_text(input_file)
    print(result)

    # Read and print the contents of temp.txt
    with open('temp.txt', 'r', encoding='utf-8') as temp_file:
        extracted_text = temp_file.read()
        print("Extracted Text:")
        print(extracted_text)
