import cv2
import cv2 as cv
import numpy as np

def salt_pepper_noise(image, amount=0.05):
    output = np.copy(image)
    num_salt = np.ceil(amount * image.size * 0.5)
    num_pepper = np.ceil(amount * image.size * 0.5)

    # Salt noise
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    output[coords[0], coords[1], :] = 255

    # Pepper noise
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    output[coords[0], coords[1], :] = 0

    return output

# Baca gambar
image = cv.imread('Resources/Photos/cats.jpg')

# Tambahkan salt & pepper ke gambar
noise_image = salt_pepper_noise(image)

# # menerapkan median blur (bagus)
blurred_image = cv2.medianBlur(noise_image, 5)

# # Gaussian Blur (jelek)
# blurred_image = cv.GaussianBlur(noise_image, (5,5), 0)
#
# # Average Blur (jelek)
# blurred_image = cv.blur(noise_image, (7,7))

# Gambar dalam 1 panel
panel = np.hstack((noise_image, blurred_image, image))

# Tampilkan panel
cv2.imshow('Salt & Pepper Noise vs Median blur', panel)
cv2.waitKey(0)
cv2.destroyAllWindows()