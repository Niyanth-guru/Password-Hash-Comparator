# Password Hash Comparator

Hey everyone! 
This project is a personal initiative to build a password hash comparator using Python. Currently, it's a rudimentary build that supports comparison against a select few hashing algorithms like MD5 and SHA variants. The goal is to lay the foundation for a more advanced tool in the future — one that can handle a broader range of algorithms and deliver deeper insights for password security analysis. Stay tuned as this project evolves!

🧩 Features
Supports the following hash algorithms:
* MD5<br>
* SHA-1<br>
* SHA-224<br>
* SHA-256<br>
* SHA-384<br>
* SHA-512<br>

* Accepts user input for:
  * Hash value to compare<br>
  * Hashing algorithm used<br>
* Reads from a user-provided wordlist
* Returns the matching plaintext password (if found)<br>

# 🚀 Getting Started
## 🔧 Prerequisites
* Python 3.x installed

## 📥 Installation
Clone the repo or download the script:
```bash
git clone https://github.com/yourusername/hash-compare-tool.git
cd hash-compare-tool
```

## ▶️ Usage:
You will be prompted to enter:
```bash
python hashed_passwords_checker.py
```
* The hash to compare
* The hashing algorithm used
* The path to your wordlist file

# 📂 Example
![alt text](https://github.com/Niyanth-guru/Password-Hash-Comparator/blob/main/Example%20Image.png)

# ⚠️ Disclaimer
This tool is intended for educational and ethical research purposes only. Do not use it on systems or data you do not own or have explicit permission to test.

# 📚 License
MIT License – feel free to use, modify, and share!
