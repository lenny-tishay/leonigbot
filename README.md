

# <span style="color: #FFD700;">LeonigBot</span> 🤖

**Welcome to LeonigBot** - A terminal-controlled Instagram automation bot designed to view and like stories and posts. Built with love by `lenny-tishay` for seamless use on Termux (Android) or any simple OS!

---

## <span style="color: #00FF00;">Features</span> 🌟
- **Login:** Securely logs into your Instagram account as a linked web device.
- **Automation:** Views and likes stories from followed users and posts from your timeline.
- **Terminal Control:** Simple menu (1-4) to choose actions.
- **Smooth Start:** Run with a single command like `npm start` using `./start.sh`.
- **Dependencies:** Auto-installs required libraries with `requirements.txt`.

---

## <span style="color: #FF4500;">Files</span> 📂
| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `bot.py`        | The main bot script (Python).                   |
| `requirements.txt` | Lists Python dependencies (`instagrapi`).     |
| `start.sh`      | Bash script to install deps and run the bot.    |

---

## <span style="color: #1E90FF;">Setup Instructions</span> 🚀

### Prerequisites
- **Termux** (Android) or a simple OS with Python.
- Git installed (`pkg install git`).

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/lenny-tishay/leonigbot.git
   cd leonigbot
   ```

2. **Install Rust** (needed for `instagrapi`)
   ```bash
   pkg install rust -y
   export PATH="$HOME/.cargo/bin:$PATH"
   ```

3. **Make start.sh Executable**
   ```bash
   chmod +x start.sh
   ```

4. **Run the Bot**
   ```bash
   ./start.sh
   ```
   - Follow prompts for username, password, and 2FA (if enabled).

---

## <span style="color: #FF69B4;">Usage</span> 🎨
After running `./start.sh`, you’ll see:
```
[LeonigBot] Starting login process...
[LeonigBot] Enter your Instagram username: 
```
- Enter credentials one by one.
- Then choose:
```
[LeonigBot] Options:
1. View and like stories
2. View and like posts
3. Do both
4. Exit
```

---

## <span style="color: #9ACD32;">Troubleshooting</span> 🛠️
- **“No module named instagrapi”**
  ```bash
  pip install instagrapi
  ```
- **Login Fails**
  - Add this to `bot.py` after `cl = Client()`:
    ```python
    cl.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    ```
  - Update on GitHub, then `git pull`.
- **Rust Error**
  - Ensure Rust is installed (`rustc --version`).

---

## <span style="color: #BA55D3;">Contributing</span> 💡
Feel free to fork, tweak, and submit pull requests! Issues? Open a ticket on GitHub.

---

## <span style="color: #FFA500;">License</span> 📜
MIT License - Free to use, modify, and share!

---

**<span style="color: #00CED1;">Happy Automating!</span>**  
Created by `lenny-tishay` - 2025
```

---

---
