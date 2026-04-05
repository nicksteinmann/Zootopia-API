# Zootopia API 🦊🌍

## Description

Zootopia API is a Python-based project that generates a simple HTML website displaying information about animals.
Instead of using static JSON data, this version fetches live data from the **API Ninjas Animals API**.

The project demonstrates how to:

* Work with external APIs
* Handle JSON responses
* Generate dynamic HTML content
* Structure a Python project into multiple files

---

## Features

* 🔍 Search for any animal via user input
* 🌐 Fetch real-time data from an API
* 🧾 Automatically generate an HTML page
* ⚠️ Handle cases where no animal is found
* 🧩 Modular architecture (data fetcher + generator)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nicksteinmann/Zootopia-API.git
cd Zootopia-API
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the root directory:

```text
API_KEY=your_api_key_here
```

⚠️ Make sure your `.env` file is not pushed to GitHub.

---

## Usage

Run the script:

```bash
python animals_web_generator.py
```

Then enter an animal name when prompted:

```text
Enter a name of an animal: Fox
```

The program will generate:

```text
animals.html
```

Open this file in your browser to see the results.

---

## Example

Input:

```text
Monkey
```

Output:

* A generated HTML page with information about monkeys

If no results are found:

```html
<h2>The animal "xyz" doesn't exist.</h2>
```

---

## Technologies Used

* Python 🐍
* Requests
* Python-dotenv
* HTML & CSS

---

## Notes

* This project is part of a learning exercise focused on APIs and project structure
* API data is provided by API Ninjas

---

## Author

Nick 🚀
