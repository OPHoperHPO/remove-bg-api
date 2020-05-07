"""
Description: removebg.py example
Author: Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]
License: MIT
"""
from removebg import RemoveBg
from config import API_TOKEN

def main():
    """
    It opens the imgs/a.jpg file
    and sends it for processing to remove.bg,
    and then saves it under the name a.png.
    """
    removebg = RemoveBg(API_TOKEN)  # Initialize api wrapper
    image = removebg.remove_bg_file(input_path="imgs/a.jpg", out_path="./a.png", size="preview",
                                    raw=False)  # Send and save the finished image

    print("Image was saved along the path: {}".format(image))


if __name__ == "__main__":
    main()
