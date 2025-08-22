import easyocr
# import cV2
# Initialize the reader with the desired language(s)
reader = easyocr.Reader(['en', 'hi'])  # 'en' for English, 'hi' for Hindi

# Perform OCR on an image
result = reader.readtext('C:\\Users\\s66\\Desktop\\practice\\practice 2\\OIP (1).webp')

# Print the results
for detection in result:
    print(f"Text: {detection[1]}, Confidence: {detection[2]:.2f}")

