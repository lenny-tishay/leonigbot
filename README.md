```markdown
# 🤖 LeonigBot: Your Terminal-Controlled Instagram Automation Buddy! 🌈✨

[![Made with Rust and Python](https://img.shields.io/badge/Made%20with-Rust%20%26%20Python-blueviolet?style=for-the-badge)](https://www.rust-lang.org/ "Rust") [![Instagrapi Powered](https://img.shields.io/badge/Powered%20by-Instagrapi-brightgreen?style=for-the-badge)](https://instagrapi.readthedocs.io/en/latest/ "Instagrapi")

Welcome to **LeonigBot**, a terminal-based Instagram automation tool designed for simple OS environments like Termux! 🚀 This bot allows you to effortlessly view and like stories and posts, just like a linked web device. Get ready to supercharge your Instagram experience! 🌟

## 🌟 Features

* **Terminal-Controlled:** Manage your Instagram account directly from your terminal. 💻
* **Automation:** Automatically view and like stories and posts. 👍👀
* **Simple OS Compatibility:** Perfect for Termux and similar environments. 📱
* **Easy Installation:** Step-by-step guide to get you up and running quickly. 🛠️
* **Colorful Output:** Enjoy a visually appealing terminal experience. 🎨
* **Animated Messages:** Fun animations to enhance your interaction. 🎉

## 🎬 Demo (Imagine this with terminal animations!)

```
[LeonigBot] ✨ Starting login process... ✨
[LeonigBot] 👤 Enter your Instagram username: your_username
[LeonigBot] 🔑 Enter your Instagram password: *********
[LeonigBot] 🔐 Enter 2FA code (if enabled): 123456
[LeonigBot] 🚀 Login successful! 🚀
[LeonigBot] 1. View Stories 📖
[LeonigBot] 2. Like Posts ❤️
[LeonigBot] 3. View and Like Both 🤩
[LeonigBot] 4. Exit 🚪
```

## 🛠️ Installation Guide

Follow these steps to get LeonigBot running on your Termux environment.

**Step 1: Install Rust in Termux**

To resolve potential dependency issues, install the Rust compiler in Termux:

```bash
pkg update && pkg upgrade -y
pkg install rust -y
rustc --version
export PATH="$HOME/.cargo/bin:$PATH"
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Step 2: Retry Installing `instagrapi`**

Now that Rust is installed, try installing `instagrapi` again:

```bash
pip install instagrapi
```

**Step 3: Verify Your Setup**

Once `instagrapi` installs:

```bash
pip show instagrapi
cd ~/leonigbot
./start.sh
```

**Step 4: If You Still Have Issues**

If Rust installation or `pip install instagrapi` still fails, we can try a workaround by pinning older versions of dependencies.

1.  **Update `requirements.txt` on GitHub:**
    * Go to [https://github.com/lenny-tishay/leonigbot](https://github.com/lenny-tishay/leonigbot).
    * Click `requirements.txt`.
    * Click the pencil icon to edit.
    * Replace its contents with:

    ```text
    instagrapi==1.16.35
    pydantic==1.10.13
    ```

    * Commit with a message like "Update requirements.txt with older versions."

2.  **Pull changes in Termux:**

    ```bash
    cd ~/leonigbot
    git pull origin main
    ```

3.  **Install again:**

    ```bash
    pip install -r requirements.txt
    ```

**Step 5: Run the Bot Smoothly**

Assuming `instagrapi` installs successfully:

```bash
./start.sh
```

**What Happens:**

It runs the bot, prompting:

```text
[LeonigBot] Starting login process...
[LeonigBot] Enter your Instagram username:
```

Enter your username, then password, then 2FA (if needed), one by one.

Choose options 1-4 to view/like stories/posts.

## 📝 Usage

1.  Run `./start.sh` in your Termux terminal.
2.  Follow the prompts to log in and select your desired actions.
3.  Enjoy automated Instagram interactions! 🎉

## ⚠️ Disclaimer

* Use this bot responsibly and ethically.
* Automating Instagram actions may violate Instagram's terms of service.
* The developer is not responsible for any issues arising from the use of this bot.

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues.

## 📜 License

This project is licensed under the MIT License.

## 💖 Support

If you find this project helpful, consider starring it! ⭐

---

**Happy automating!** 🤖✨
```
