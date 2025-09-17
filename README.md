DotCrypt - Advanced Text Encryption System
A Python-based text encryption tool that converts messages into unique dot patterns using randomized substitution mapping with compressed key storage.

🔐 Features
Multi-Character Support: Encrypts 100+ characters including:

Letters (a-z, A-Z)

Numbers (0-9)

Punctuation (.,!?;:'"etc.)

Mathematical symbols (+-*/=<>%^&)

Special characters (@#$~`|_§)

International characters (áéíóú, àèìòù, ñüöäß)

Emojis (😀😃😄😊😍🤔👍❤🔥💯)

Unique Dot Pattern Encryption: Each character gets mapped to a randomized sequence of dots and spaces

Compressed Key Storage: Uses Base62 encoding to reduce key file size by ~60%

Clipboard Integration: Automatically copies encrypted output for easy sharing

Bidirectional: Full encryption and decryption support

Interactive CLI: User-friendly menu system

🚀 How It Works
Encryption: Each character is mapped to a unique pattern of dots (.) and spaces

Randomization: Uses random number generation to create unique mappings each time

Key Storage: Mapping data is compressed using Base62 encoding and saved to bokachokabeho.ab

Output: Encrypted text appears as sequences like: .. .. ....... .... ...... .. ..

📋 Prerequisites
bash
pip install pyperclip
💡 Usage
bash
python dotcrypt.py
Menu Options:

Encryption - Enter text to encrypt

Decryption - Enter encrypted message to decrypt

Exit - Close program

🔧 Technical Details
Algorithm: Substitution cipher with randomized dot pattern mapping

Key Compression: Base62 encoding (0-9, A-Z, a-z)

File Format: Binary key storage with UTF-8 encoding

Pattern Generation: 10 randomized segments per character (3-500 dots each)

⚠️ Important Notes
Educational Purpose: This is a learning project, not cryptographically secure

Key Dependency: Keep the generated .ab key file to decrypt messages

Platform: Requires xclip/xsel on Linux for clipboard functionality

🎯 Example
Input: Hello World!
Encrypted: .. .. ....... .... ...... .. .. .... ... ...... .. .. ........... .......

🔄 Base62 Optimization
Token compression reduces key file size:

Before: 16000 38 729 496 715 180 140 3704 1188 2960

After: 4A4 c Bl 80 BX 2u 2G xk JA lk

Built as a Python learning project exploring encryption concepts, file I/O, and data compression techniques.
