# 🔐 Secure Coding Review Using Python

## 📌 About This Project

As part of my cybersecurity learning journey, I completed a practical task on **Secure Coding Review** using Python.

In this project, I reviewed a simple Python-based login authentication system, identified potential security vulnerabilities, and explored secure coding techniques to improve application security.

## 🎯 Objectives

* Understand the importance of secure coding.
* Identify common security vulnerabilities.
* Perform manual code inspection.
* Learn to use static analysis tools.
* Implement secure coding practices.
* Recommend solutions to prevent security attacks.

## 🛠️ Technologies and Tools

* Python
* SQLite
* Bandit
* Pylint
* Bcrypt

## 🔍 Vulnerabilities Identified

During the code review, I studied the following vulnerabilities:

1. SQL Injection
2. Plaintext Password Storage
3. Hardcoded Credentials
4. Improper Error Handling
5. Lack of Input Validation

## 🛡️ Security Improvements

I explored the following security practices:

* Used parameterized SQL queries to prevent SQL injection.
* Implemented bcrypt password hashing.
* Avoided hardcoded credentials.
* Improved exception handling.
* Recommended input validation.
* Learned about static code analysis using Bandit.

## 🔧 Security Testing

I explored Bandit, a Python security analysis tool.

Command used:

```bash
pip install bandit
bandit -r .
```

Bandit helps identify potential security issues in Python applications.

## 📚 Key Learnings

Through this task, I learned:

* How SQL injection vulnerabilities occur.
* Why password hashing is important.
* How to identify security weaknesses in source code.
* How static analysis tools help developers.
* How secure coding practices improve application security.

## 🚀 Conclusion

This project helped me understand the importance of secure coding and basic application security auditing.

I gained practical knowledge of identifying vulnerabilities and recommending remediation techniques to build safer applications.

**This project is part of my continuous cybersecurity learning journey.**

---

⭐ Learning something new every day and improving my cybersecurity skills!
