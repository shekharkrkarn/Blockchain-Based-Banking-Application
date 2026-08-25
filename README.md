Blockchain-Based Banking Application

A web-based academic project that demonstrates how blockchain concepts
can be used to record and manage banking transactions in a secure,
transparent, and tamper-evident manner.

Overview

The Blockchain-Based Banking Application is developed using Python and
Flask for the backend, with HTML, CSS, and JavaScript for the user
interface.

The application represents banking transactions as blocks in a
blockchain-style ledger. Each block contains transaction-related
information, a timestamp, a cryptographic hash, and the hash of the
previous block. This linking mechanism helps maintain the integrity of
the blockchain and makes unauthorized modification of recorded data
detectable.

Objectives

Demonstrate the basic working principles of blockchain technology.

Store banking transactions in the form of linked blocks.

Implement cryptographic hashing using SHA-256.

Demonstrate block creation and Proof of Work based mining.

Validate and process banking transaction information.

Provide a simple web interface for entering transaction details.

Display blockchain records through the web application.

Build practical understanding of Python, Flask, cryptography, and
web development.

Key Features

Blockchain-based transaction storage

Block creation and linking

SHA-256 cryptographic hashing

Previous-hash verification

Proof of Work based mining

Transaction validation

Web-based transaction interface

Real-time addition of new blocks

Blockchain ledger display

Simple and user-friendly interface

Technology Stack

Backend

Python

Flask

Frontend

HTML

CSS

JavaScript

Blockchain & Security Concepts

Blockchain

SHA-256 Cryptographic Hashing

Proof of Work

Block Linking

Transaction Verification

Project Structure

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

How It Works

The user enters banking transaction details through the web
interface.

The application receives and processes the transaction through the
Flask backend.

The transaction is validated before being added to the blockchain.

A new block is created containing the transaction information.

The block is linked to the previous block using its previous hash.

SHA-256 hashing is used to generate the block hash.

Proof of Work is performed during the mining process.

The newly mined block is added to the blockchain.

The updated blockchain ledger is displayed through the application
interface.

Installation

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Blockchain-Based-Banking-Application

2. Create and activate a virtual environment

python -m venv .venv

Windows:

.venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python BankingApplication.py

Then open the local Flask URL shown in the terminal in your web browser.

Requirements

The project uses Python and Flask. Required Python packages are listed
in requirements.txt.

Project Category

Web-Based Application

Blockchain Application

FinTech / Banking Technology

Software Development Project

Decentralized Ledger Demonstration

Future Enhancements

The project can be extended with additional features such as:

User authentication and authorization

Database connectivity

Smart contract integration

More advanced transaction management

Additional security mechanisms

Improved scalability and deployment support

Academic Project

This project was developed as an academic project to gain practical
experience in blockchain technology, Python programming, Flask web
development, cryptographic hashing, and transaction processing.

Author

Shekhar Kumar

Computer Science & Engineering
Pemiya Rishikesh Institute of Technology, Dhanbad