# 📞 Contact Book (Python + MySQL)

A simple terminal-based **Contact Book** application built with **Python** and **MySQL**. This project demonstrates basic operations (Create, Read, Update, Delete) and Python-MySQL integration using the `mysql-connector-python` library.

---

## 🚀 Features

- ✅ Add a new contact
- ✅ View all saved contacts
- ✅ Search for a contact by name
- ✅ Delete a contact by ID
- ✅ CLI menu for user interaction

---

## 🛠️ Technologies Used

- **Python 3.x**
- **MySQL**
- **mysql-connector-python**

---

## 💻 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/contact-book-python-mysql.git
cd contact-book-python-mysql
```

### 2️⃣ Install Required Package

```bash
pip install mysql-connector-python
```

### 3️⃣ Create MySQL Database & Table

Open your MySQL CLI or Workbench and run:

```sql
CREATE DATABASE contact_book;

USE contact_book;

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100)
);
```

### 4️⃣ Configure Database Connection

Update the following lines in `contact_book.py` with your own MySQL credentials:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="contact_book"
)
```

### 5️⃣ Run the Program

```bash
python contact_book.py
```


