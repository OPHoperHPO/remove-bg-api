"""
Description: remove_bg_api example
Author: Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]
License: MIT
"""
from remove_bg_api import RemoveBg
from config import API_TOKEN


def main():
    """
    It opens the imgs/a.jpg file
    and sends it for processing to remove.bg,
    and then saves it under the name a.png.
    """
    removebg = RemoveBg(API_TOKEN)  # Initialize api wrapper
    image = open("imgs/a.jpg", "rb").read()  # Open image
    image = removebg.remove_bg_bytes(input_bytes=image, out_path="./a.png", size="preview",
                                     raw=False)  # Send and save the finished image

    print("Image was saved along the path: {}".format(image))


if __name__ == "__main__":
    main()
