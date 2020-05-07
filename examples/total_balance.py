"""
Description: remove_bg.py example
Author: Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]
License: MIT
"""
from remove_bg import RemoveBg
from config import API_TOKEN

def main():
    """
    Shows total account balance.
    """
    removebg = RemoveBg(API_TOKEN)  # Initialize api wrapper
    print("Account total balance: ", removebg.account.balance())  # Show account balance

if __name__ == "__main__":
    main()
