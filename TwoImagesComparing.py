import cv2
import numpy as np

def compare_and_show(image1_path, image2_path):
    # Load both images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Check if both images were loaded correctly
    if img1 is None:
        print(f"Error: Could not load image at {image1_path}")
        return
    if img2 is None:
        print(f"Error: Could not load image at {image2_path}")
        return

    # Resize both images to the same size
    img1 = cv2.resize(img1, (200, 200))
    img2 = cv2.resize(img2, (200, 200))

    # Compare the images
    difference = cv2.subtract(img1, img2)
    
    # If difference is all zeros, images are the same
    if np.count_nonzero(difference) == 0:
        print(f"The images '{image1_path}' and '{image2_path}' are the same.")
        # Draw a circle on the matched image
        center_coordinates = (100, 100)  # Center of the circle (200x200 image)
        radius = 80  # Radius of the circle
        color = (0, 255, 0)  # Circle color (Green in BGR format)
        thickness = 2  # Thickness of the circle outline

        # Draw the circle on the second image
        cv2.circle(img2, center_coordinates, radius, color, thickness)

    else:
        print(f"The images '{image1_path}' and '{image2_path}' are different.")

    # Display both images
    cv2.imshow('Image 1', img1)
    cv2.imshow('Image 2', img2)

    # Wait until a key is pressed and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Compare and show images
compare_and_show('apple2.jpg', 'apple2.jpg')  # Same images
compare_and_show('apple2.jpg', 'apple1.png')   # Different images
