from PIL import Image

import LsbSteg

import canny_edge_detector


message = "This is a hidden flower in an image"

imageFilename = "BW-using-curves.jpg"
img = Image.open(imageFilename)
detect = canny_edge_detector.cannyEdgeDetector(img)

newImageFilename = "stego_stars_background"

newImg = LsbSteg.encodeLSB(message, imageFilename, newImageFilename)
if not newImg is None:
        print("Stego image created.")

print("Decoding...")
message = LsbSteg.decodeLSB("stego_stars_background.png")
print("Final message: ", message)
