"""
Description: remove_bg_api example
Author: Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]
License: MIT
"""
from remove_bg_api import RemoveBg
from config import API_TOKEN


def main():
    """
    Shows account balance.
    """
    removebg = RemoveBg(API_TOKEN)  # Initialize api wrapper
    balance = removebg.account.get_balance_dict()  # Get balance
    print("Account balance: ", )  # Parse balance dict
    print("----------------------------------------------")
    print("Subscription credits: ",  balance["subscription"])
    print("Pay-you-go credits: ",  balance["payg"])
    print("Enterprise credits: ",  balance["enterprise"])
    print("----------------------------------------------")
    print("Total credits: ",  balance["total"])


if __name__ == "__main__":
    main()
