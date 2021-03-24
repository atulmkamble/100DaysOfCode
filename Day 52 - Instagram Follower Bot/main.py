"""
This program follows the followers of an intended Instagram account
"""

# Import required class
from insta_follower import InstaFollower

# Initialize global variables
target_account = '' # TODO: Intended target account. e.g., shraddhakapoor
USERNAME = '' # TODO: Your instagram username
PASSWORD = '' # TODO: Your instagram password


def main():
    insta_follower = InstaFollower()
    insta_follower.login(USERNAME, PASSWORD)
    insta_follower.find_followers(target_account)
    insta_follower.follow()
    print('Done')


if __name__ == '__main__':
    main()
