from PIL import Image

import LsbSteg

import canny_edge_detector

from CaesarCipher import CaesarCipher

if __name__ == "__main__":
        key = 5
        imageFilename = "BW-using-curves.jpg"
        newFileName = "stego_stars_background.png"

        message = "This is a hidden flower in an image"

        encMessage = CaesarCipher.encrypt(message, key)

        img = Image.open(imageFilename)
        detect = canny_edge_detector.cannyEdgeDetector(img)

        newImg = LsbSteg.encodeLSB(encMessage, imageFilename, newFileName)
        if newImg is not None:
                print("Stego image created.")

        print("Decoding...")
        rawMessage = LsbSteg.decodeLSB(newFileName)
        message = CaesarCipher.decrypt(rawMessage, key)
        print("Final message: ", message)
