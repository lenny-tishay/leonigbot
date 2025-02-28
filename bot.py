import os
import sys
import time
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, TwoFactorRequired
import getpass

# Initialize Instagram client
cl = Client()
cl.delay_range = [2, 6]  # Adjusted delays to avoid bans
SESSION_FILE = "session.json"

def log(message):
    """Log messages to terminal."""
    print(f"[LeonigBot] {message}")

def load_session():
    """Load session if available."""
    if os.path.exists(SESSION_FILE):
        try:
            cl.load_settings(SESSION_FILE)
            log("Session loaded successfully")
            return True
        except Exception as e:
            log(f"Session load failed: {e}")
    return False

def save_session():
    """Save session to file."""
    try:
        cl.dump_settings(SESSION_FILE)
        log("Session saved successfully")
    except Exception as e:
        log(f"Session save failed: {e}")

def login():
    """Handle login with step-by-step credential input."""
    log("Starting login process...")
    username = input("[LeonigBot] Enter your Instagram username: ")
    time.sleep(1)  # Small delay for smoothness
    password = getpass.getpass("[LeonigBot] Enter your Instagram password: ")
    try:
        if not load_session():
            log("No valid session found. Logging in...")
            cl.login(username, password)
            save_session()
        log("Login successful")
    except TwoFactorRequired:
        time.sleep(1)
        code = input("[LeonigBot] Enter your 2FA code: ")
        cl.login(username, password, verification_code=code)
        save_session()
        log("Logged in with 2FA")
    except Exception as e:
        log(f"Login failed: {e}")
        sys.exit(1)

def view_and_like_stories():
    """View and like stories from followed users."""
    log("Fetching followed users...")
    try:
        following = cl.user_following(cl.user_id, amount=30)  # Limit to 30 users
        user_ids = list(following.keys())
        log(f"Found {len(user_ids)} users to process")
    except Exception as e:
        log(f"Error fetching following: {e}")
        return

    for user_id in user_ids:
        try:
            stories = cl.user_stories(user_id)
            if stories:
                for story in stories:
                    cl.story_view(story.pk)
                    log(f"Viewed story {story.pk} from user {user_id}")
                    cl.story_like(story.pk)
                    log(f"Liked story {story.pk} from user {user_id}")
                    time.sleep(3)
            else:
                log(f"No stories for user {user_id}")
            time.sleep(2)
        except Exception as e:
            log(f"Error with user {user_id} stories: {e}")
            time.sleep(10)

def view_and_like_posts():
    """View and like posts from timeline."""
    log("Fetching timeline posts...")
    try:
        posts = cl.get_timeline_feed()['feed_items'][:10]  # Limit to 10 posts
        log(f"Found {len(posts)} posts to process")
    except Exception as e:
        log(f"Error fetching timeline: {e}")
        return

    for item in posts:
        if 'media_or_ad' not in item:
            continue
        post = item['media_or_ad']
        try:
            media_id = post['pk']
            cl.media_view(media_id)
            log(f"Viewed post {media_id}")
            cl.media_like(media_id)
            log(f"Liked post {media_id}")
            time.sleep(3)
        except Exception as e:
            log(f"Error with post {media_id}: {e}")
            time.sleep(10)

def main():
    log("Welcome to LeonigBot")
    if not load_session():
        login()
    else:
        try:
            cl.get_timeline_feed()
            log("Session is valid")
        except LoginRequired:
            log("Session expired. Re-login required")
            login()

    while True:
        print("\n[LeonigBot] Options:")
        print("1. View and like stories")
        print("2. View and like posts")
        print("3. Do both")
        print("4. Exit")
        choice = input("[LeonigBot] Enter your choice (1-4): ")

        if choice == "1":
            view_and_like_stories()
        elif choice == "2":
            view_and_like_posts()
        elif choice == "3":
            view_and_like_stories()
            view_and_like_posts()
        elif choice == "4":
            log("Exiting bot. Goodbye!")
            break
        else:
            log("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
