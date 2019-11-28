#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program prints a mailing address in proper format


def mailing_address(name, address, city,
                    province, postal_code, apartment=None):
    # This function makes a mailing address in proper format

    # Process
    if apartment is not None:
        post_address = name + "\n" + apartment + "-" + address + "\n" + \
                       city + " " + province + "  " + postal_code
    else:
        post_address = name + "\n" + address + "\n" + city + \
                       " " + province + "  " + postal_code

    return post_address


def main():
    # This function collects mailing details then outputs a mailing address

    # Variables
    user_apartment_number = None

    # Input
    user_recipient_name = input("Enter the recipient's full name: ")
    user_address = input(
                   "Enter the recipient's address (road & street number): ")
    question = input("Does the recipient live in an apartment (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        user_apartment_number = input(
                                "Enter the recipient's apartment number: ")
    user_municipality = input("Enter the recipient's municipality: ")
    user_province = input(
                    "Enter the recipient's province/territory (abbreviate): ")
    user_postal_code = input("Enter the recipient's postal code: ")

    # Process
    if user_apartment_number is not None:
        post = mailing_address(user_recipient_name, user_address,
                               user_municipality, user_province,
                               user_postal_code, user_apartment_number)
    else:
        post = mailing_address(user_recipient_name, user_address,
                               user_municipality, user_province,
                               user_postal_code)

    # Output
    print("")
    print(post)


if __name__ == "__main__":
    main()
