"""
Description: remove_bg.py example
Author: Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]
License: MIT
"""
from remove_bg import RemoveBg
from config import API_TOKEN

def main():
    """
    Shows the remainder of free api calls through this library.
    """
    removebg = RemoveBg(API_TOKEN)  # Initialize api wrapper
    print("Account free api calls estilimated: ", removebg.account.free_api_calls())  # Get account free calls


if __name__ == "__main__":
    main()
