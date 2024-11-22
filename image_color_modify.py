import cv2
import numpy as np

# Load the image
image = cv2.imread("download.png")  # Replace with your image path

# Resize the image to 400x400 while maintaining color sensitivity
resized_image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)

# Increase pixel intensity uniformly across all channels
intensity_increase = 50
brightened_image = cv2.add(resized_image, np.array([intensity_increase, intensity_increase, intensity_increase], dtype=np.uint8))

# Display the original, resized, and brightened images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Brightened Image", brightened_image)

# Save the resized and brightened image
cv2.imwrite("/mnt/data/resized_brightened_image.png", brightened_image)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
