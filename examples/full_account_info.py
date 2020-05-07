"""
Description: remove_bg_api example
Author: Anodev (OPHoperHPO)[https://github.com/OPHoperHPO]
License: MIT
"""
from remove_bg_api import RemoveBg
from config import API_TOKEN

def main():
    """
    Shows full account information.
    """
    removebg = RemoveBg(API_TOKEN)  # Initialize api wrapper
    info = removebg.account.get_all_info()  # Get account information
    balance = info["data"]["attributes"]["credits"]
    apis = info["data"]["attributes"]["api"]
    print("Account information: ")
    print("----------------------------------------------")
    print("Balance: ", )  # Parse balance dict
    print("----------------------------------------------")
    print("Subscription credits: ",  balance["subscription"])
    print("Pay-you-go credits: ",  balance["payg"])
    print("Enterprise credits: ",  balance["enterprise"])
    print("----------------------------------------------")
    print("Total credits: ",  balance["total"])
    print("----------------------------------------------")
    print("Account APIs:")
    print("----------------------------------------------")
    print("Api free calls: ", apis["free_calls"])
    if "sizes" in apis.keys():
        print("Api sizes (DEPRECATED): ", apis["sizes"])


if __name__ == "__main__":
    main()
