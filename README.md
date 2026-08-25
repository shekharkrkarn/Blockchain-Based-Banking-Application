# ⛓️ Blockchain-Based Banking Application

<p align="center">
  <strong>A Web-Based Academic Project Demonstrating Blockchain Concepts for Banking Transactions</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask" alt="Flask">
  <img src="https://img.shields.io/badge/Blockchain-SHA--256-purple?style=for-the-badge" alt="Blockchain">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-orange?style=for-the-badge" alt="Frontend">
</p>

---

## 📌 Overview

The **Blockchain-Based Banking Application** is a web-based academic project
that demonstrates how blockchain concepts can be used to record and manage
banking transactions in a secure, transparent, and tamper-evident manner.

The application is developed using **Python and Flask** for the backend, with
**HTML, CSS, and JavaScript** for the user interface.

The application represents banking transactions as blocks in a
blockchain-style ledger. Each block contains transaction-related information,
a timestamp, a cryptographic hash, and the hash of the previous block.

This linking mechanism helps maintain the integrity of the blockchain and makes
unauthorized modification of recorded data detectable.

---

## 🎯 Objectives

The main objectives of this project are:

- 🔗 Demonstrate the basic working principles of blockchain technology.
- 💳 Store banking transactions in the form of linked blocks.
- 🔐 Implement cryptographic hashing using SHA-256.
- ⛏️ Demonstrate block creation and Proof of Work based mining.
- ✅ Validate and process banking transaction information.
- 🌐 Provide a simple web interface for entering transaction details.
- 📋 Display blockchain records through the web application.
- 🧠 Build practical understanding of Python, Flask, cryptography, and web development.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| ⛓️ Blockchain Transaction Storage | Stores banking transactions as linked blocks |
| 🧱 Block Creation | Creates a new block for processed transactions |
| 🔐 SHA-256 Hashing | Generates cryptographic hashes for blocks |
| 🔗 Previous Hash Verification | Links each block with the previous block |
| ⛏️ Proof of Work | Demonstrates blockchain mining |
| ✅ Transaction Validation | Processes and validates transaction information |
| 🌐 Web Interface | Provides a simple interface for entering transactions |
| ⚡ Real-Time Block Addition | Adds newly mined blocks to the blockchain |
| 📋 Blockchain Ledger | Displays blockchain records through the application |
| 🎨 User-Friendly Interface | Provides a simple and easy-to-use interface |

---

## 🛠️ Technology Stack

### Backend

- 🐍 **Python**
- 🌶️ **Flask**

### Frontend

- 🌐 **HTML**
- 🎨 **CSS**
- ⚡ **JavaScript**

### Blockchain & Security Concepts

- ⛓️ Blockchain
- 🔐 SHA-256 Cryptographic Hashing
- ⛏️ Proof of Work
- 🔗 Block Linking
- ✅ Transaction Verification

---

## 🧠 Blockchain Concepts Used

### 🔐 SHA-256 Cryptographic Hashing

SHA-256 is used to generate a cryptographic hash for each block.

The block hash is generated using information such as:

- Block index
- Timestamp
- Transaction data
- Previous block hash
- Nonce

This allows changes to block information to become detectable.

---

### 🔗 Block Linking

Each block stores the hash of the previous block.

```text
┌──────────────┐
│   Block 0    │
│ Genesis Block│
└──────┬───────┘
       │ Previous Hash
       ▼
┌──────────────┐
│   Block 1    │
│ Transaction  │
└──────┬───────┘
       │ Previous Hash
       ▼
┌──────────────┐
│   Block 2    │
│ Transaction  │
└──────┬───────┘
       │ Previous Hash
       ▼
┌──────────────┐
│   Block 3    │
│ Transaction  │
└──────────────┘

⛏️ Proof of Work

During the mining process, the application changes the block's nonce until
the generated hash satisfies the configured difficulty condition.

This demonstrates the basic concept of Proof of Work based mining.

🔄 How It Works
The application follows the following transaction workflow:
        
        👤 User
           │
           ▼
   🌐 Web Interface
           │
           ▼
    🌶️ Flask Backend
           │
           ▼
  ✅ Transaction Validation
           │
           ▼
      🧱 New Block
           │
           ▼
    🔐 SHA-256 Hashing
           │
           ▼
     ⛏️ Proof of Work
           │
           ▼
    🔗 Link Previous Hash
           │
           ▼
   ⛓️ Add Block to Chain
           │
           ▼
    📋 Display Blockchain

🔄 Step-by-Step Process

1. The user enters banking transaction details through the web interface.
2. The application receives and processes the transaction through the Flask backend.
3. The transaction is validated before being added to the blockchain.
4. A new block is created containing the transaction information.
5. The block is linked to the previous block using its previous hash.
6. SHA-256 hashing is used to generate the block hash.
7. Proof of Work is performed during the mining process.
8. The newly mined block is added to the blockchain.
9. The updated blockchain ledger is displayed through the application interface.

📂 Project Structure
Blockchain-Based-Banking-Application/
│
├── templates/
│   ├── __init__.py
│   └── BankingApplication.html
│
├── BankingApplication.py
├── README.md
├── requirements.txt
└── .gitignore

⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/shekharkrkarn/Blockchain-Based-Banking-Application.git

Then move into the project directory:

cd Blockchain-Based-Banking-Application
2️⃣ Create a Virtual Environment
python -m venv .venv
Windows

Activate the virtual environment:

.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python BankingApplication.py

Then open the local Flask URL shown in the terminal in your web browser.

📦 Requirements

The project uses Python and Flask.

Required Python packages are listed in:

requirements.txt

🖥️ Application Interface

The application provides a web-based interface where users can enter banking
transaction details and interact with the blockchain-based transaction system.

📸 Project screenshots can be added here to demonstrate the application interface.

📊 Project Category
🌐 Web-Based Application
⛓️ Blockchain Application
🏦 FinTech / Banking Technology
💻 Software Development Project
📚 Decentralized Ledger Demonstration
🚀 Future Enhancements

The project can be extended with additional features such as:

👤 User authentication and authorization
💾 Database connectivity
📜 Smart contract integration
💳 More advanced transaction management
🛡️ Additional security mechanisms
📈 Improved scalability
☁️ Deployment support
🌐 Distributed blockchain/network support
⚠️ Academic Project

This project was developed as an academic project to gain practical
experience in:

Blockchain technology
Python programming
Flask web development
Cryptographic hashing
Transaction processing
Web application development

The implementation demonstrates fundamental blockchain concepts for
educational purposes.

👨‍💻 Author
Shekhar Kumar

Computer Science & Engineering
Pemiya Rishikesh Institute of Technology, Dhanbad

Areas of Interest
🐍 Python
💻 Software Development
🌐 Web Development
⛓️ Blockchain Technology
🔐 Cryptography