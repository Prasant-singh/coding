# File I/O and Processing: Write a function that takes a file path as an argument. The function should read the file, count the frequency of each word,
#  and then print the top 10 most frequent words.

# with open('file.txt', 'r') as file:
#     text= file.read()
#     word_count = {}
#     for word in text.split():
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     sorted_words=sorted(word_count.items(),reverse=True)
#     print(sorted_words[:10])


import os
import random
import cv2

path = 'C:\\Users\\s66\\Downloads\\digit recognition.v6i.yolov8\\test\\images'
images = os.listdir(path)

# Filter for actual image files if necessary (optional but good practice)
image_files = [f for f in images ]

if not image_files:
    print(f"No image files found in {path}")
else:
    # Select a random image filename
    random_image_filename = random.choice(image_files)

    # Construct the full path to the random image
    full_image_path = os.path.join(path, random_image_filename)

    # Read the image using OpenCV
    img_data = cv2.imread(full_image_path)

    if img_data is not None:
        print(f"Successfully loaded image: {full_image_path}")
        # You can now work with img_data, e.g., display it:
        cv2.imshow("Random Image", img_data)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Failed to load image: {full_image_path}. It might be corrupted or not a valid image.")