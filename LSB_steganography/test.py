from PIL import Image

import LsbSteg

import canny_edge_detector

from CaesarCipher import CaesarCipher

if __name__ == "__main__":
        key = 5

        message = "This is a hidden flower in an image"

        encMessage = CaesarCipher.encrypt(message, key)

        imageFilename = "BW-using-curves.jpg"
        img = Image.open(imageFilename)
        detect = canny_edge_detector.cannyEdgeDetector(img)

        newImageFilename = "stego_stars_background"

        newImg = LsbSteg.encodeLSB(encMessage, imageFilename, newImageFilename)
        if newImg is not None:
                print("Stego image created.")

        print("Decoding...")
        rawMessage = LsbSteg.decodeLSB("stego_stars_background.png")
        message = CaesarCipher.decrypt(rawMessage, key)
        print("Final message: ", message)
