import os
import sys
import time
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, TwoFactorRequired
from colorama import init, Fore, Style
import getpass

# Initialize colorama for colored terminal output
init()

# Instagram client instance
cl = Client()

# Session file to avoid repeated logins
SESSION_FILE = "session.json"

def load_session():
    """Load session if it exists to avoid re-login."""
    if os.path.exists(SESSION_FILE):
        cl.load_settings(SESSION_FILE)
        print(Fore.GREEN + "Session loaded successfully!" + Style.RESET_ALL)
        return True
    return False

def save_session():
    """Save session to file."""
    cl.dump_settings(SESSION_FILE)
    print(Fore.GREEN + "Session saved successfully!" + Style.RESET_ALL)

def login():
    """Handle Instagram login with 2FA support."""
    username = input(Fore.CYAN + "Enter your Instagram username: " + Style.RESET_ALL)
    password = getpass.getpass(Fore.CYAN + "Enter your Instagram password: " + Style.RESET_ALL)

    try:
        if not load_session():
            cl.login(username, password)
            save_session()
        print(Fore.GREEN + "Logged in successfully!" + Style.RESET_ALL)
    except TwoFactorRequired:
        code = input(Fore.YELLOW + "Enter 2FA code: " + Style.RESET_ALL)
        cl.login(username, password, verification_code=code)
        save_session()
        print(Fore.GREEN + "Logged in with 2FA successfully!" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Login failed: {str(e)}" + Style.RESET_ALL)
        sys.exit(1)

def get_following():
    """Get list of users the account is following."""
    try:
        following = cl.user_following(cl.user_id)
        return list(following.keys())
    except Exception as e:
        print(Fore.RED + f"Error fetching following: {str(e)}" + Style.RESET_ALL)
        return []

def view_and_like_stories():
    """View and like stories from followed users."""
    print(Fore.YELLOW + "Fetching users you follow..." + Style.RESET_ALL)
    user_ids = get_following()
    
    if not user_ids:
        print(Fore.RED + "No users found to process." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"Found {len(user_ids)} users. Processing stories..." + Style.RESET_ALL)
    
    for user_id in user_ids:
        try:
            # Get stories for the user
            stories = cl.user_stories(user_id)
            if stories:
                for story in stories:
                    # View the story
                    cl.story_view(story.pk)
                    print(Fore.GREEN + f"Viewed story {story.pk} from user {user_id}" + Style.RESET_ALL)
                    
                    # Like the story
                    cl.story_like(story.pk)
                    print(Fore.GREEN + f"Liked story {story.pk} from user {user_id}" + Style.RESET_ALL)
                    
                    # Delay to mimic human behavior and avoid rate limits
                    time.sleep(5)
            else:
                print(Fore.YELLOW + f"No stories found for user {user_id}" + Style.RESET_ALL)
            time.sleep(3)  # Delay between users
        except Exception as e:
            print(Fore.RED + f"Error processing user {user_id}: {str(e)}" + Style.RESET_ALL)
            time.sleep(10)  # Longer delay on error

def main():
    """Main function to control the bot via terminal."""
    print(Fore.BLUE + "=== Instagram Story Bot ===" + Style.RESET_ALL)
    
    # Login if not already logged in
    if not load_session():
        login()
    else:
        try:
            cl.get_timeline_feed()  # Test session validity
        except LoginRequired:
            print(Fore.YELLOW + "Session expired. Re-login required." + Style.RESET_ALL)
            login()

    while True:
        print(Fore.CYAN + "\nOptions:" + Style.RESET_ALL)
        print("1. View and like stories")
        print("2. Exit")
        choice = input(Fore.CYAN + "Enter your choice (1-2): " + Style.RESET_ALL)

        if choice == "1":
            view_and_like_stories()
        elif choice == "2":
            print(Fore.GREEN + "Exiting bot. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Try again." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
