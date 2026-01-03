import sys
import logging
from PIL import Image, ImageOps


def main():
    # setting up the log
    logging.basicConfig(
        filename="shirt.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    # implement a program that expects exactly two command-line arguments
    if len(sys.argv) != 3:
        logging.error("Not the right number of command line argument")
        sys.exit()

    input_name = sys.argv[1]
    output_name = sys.argv[2]
    suffix = (".JPG", ".JPEG", ".PNG")

    if not input_name.upper().endswith(suffix):
        logging.error("reading file extension is not right")
        sys.exit()

    if not output_name.upper().endswith(suffix):
        logging.error("writing file extension is not right")
        sys.exit()

    if input_name.split(".")[-1].lower() != output_name.split(".")[-1].lower():
        logging.error("Input and output have different extensions")
        sys.exit()
    try:
        with Image.open(input_name) as rimg, Image.open("shirt.png") as shirt:
            logging.info("images are opened and ready to be used")
            wimg = ImageOps.fit(rimg, shirt.size)
            logging.info("the photo match the shirt's dimensions")

            wimg.paste(shirt, shirt)
            logging.info("The input photo is resized and cropped correctly")

            wimg.save(output_name)
            logging.info("A new image is produced, the program end")

    except FileNotFoundError:
        logging.error("Input file does not exist")
        sys.exit()

if __name__ == "__main__":
    main()
