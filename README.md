# Assignment_Intervue
## Intervue web login Automation

This project automates interactions with the InterVue website using **Selenium WebDriver**. It performs key user actions such as login, search, navigation, and logout.

---

## 🚀 Features

- Automated website navigation and interaction
- Login using predefined credentials
- Testing of the search functionality
- Profile menu navigation
- Secure logout process

---

## ✅ Prerequisites

Ensure the following are installed before running the script:

- Python 3.6 or higher
- Google Chrome browser
- ChromeDriver (must match your Chrome version)

---

## 📦 Installation

1. **Clone the repository** or download the files locally:
   ```bash
   git clone https://github.com/your-username/assignment_intervue.io.git
   cd assignment_intervue.io

## Setting Up requirements.txt

Create a file named `requirements.txt` with the following content:

```
selenium==4.10.0
webdriver-manager==3.8.6
```

You can adjust the versions as needed for your environment.

## Configuration

Before running the script, you may want to:

1. Update the login credentials in the script if needed
2. Adjust timeouts based on your internet connection speed
3. Configure ChromeDriver options as necessary for your environment

## Usage

Run the script with the following command:

```bash
python main.py
```

The script will:
1. Launch Chrome with the specified options
2. Navigate to the InterVue website
3. Interact with navigation elements
4. Log in with the provided credentials
5. Perform a search operation
6. Navigate through profile dropdown menu
7. Log out from the account

## Troubleshooting

If you encounter issues:

- Ensure ChromeDriver is compatible with your Chrome browser version
- Check that all selectors in the script match the current website structure
- Increase wait times if your internet connection is slow
- Check the console output for specific error messages




