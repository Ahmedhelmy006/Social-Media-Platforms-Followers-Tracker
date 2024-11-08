# LinkedIn Followers Tracker using Playwright

This project is a LinkedIn followers tracker that scrapes follower counts for LinkedIn accounts and pages using [Playwright](https://playwright.dev/) for browser automation. The follower data is submitted to a Google Form for tracking. The script is set to run every 6 hours using GitHub Actions.

## Features

- 🚀 **Automated LinkedIn Scraping**: Scrapes the number of followers from LinkedIn profiles and pages.
- 🕒 **Runs Every 6 Hours**: Uses GitHub Actions to automate the scraper on a 6-hour interval.
- 📊 **Google Form Submission**: Automatically submits the scraped data to a specified Google Form.
- 🔒 **Secure Handling of Sensitive Data**: LinkedIn cookies and other sensitive information are securely stored using GitHub Secrets.

## Installation

To run this project locally, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/linkedin-followers-tracker.git
   cd linkedin-followers-tracker
Install Dependencies: Install the required Python package

pip install -r requirements.txt
Install Playwright: Playwright needs to be installed for browser automation:

playwright install
Set Up LinkedIn Cookies:

Obtain your LinkedIn session cookies (e.g., li_at, JSESSIONID, li_rm) and store them securely.
If running locally, save them in a file named linkedin_cookies.json (this file is ignored by Git for security).


## Usage

To run the scraper locally, simply execute:
 ```python
   python main.py
```
##### The script will:

- Open LinkedIn using Playwright (headless mode).
- Scrape the follower counts for the specified accounts and pages.
- Submit the data to a pre-configured Google Form.
- Scheduling with GitHub Actions
- The scraper is set up to run automatically every 6 hours using GitHub Actions.

**Ensure you have set up your repository secrets:**


- LINKEDIN_COOKIES_JSON: Your LinkedIn cookies in JSON format.
- GitHub Actions will:
- Run the scraper every 6 hours.
- Submit the scraped data to Google Form.
- Store the logs in the Actions tab for monitoring.
- Storing Sensitive Information
- Sensitive information such as LinkedIn session cookies are securely stored using GitHub Secrets. Do not commit sensitive data like cookies or API keys to the repository.

For more details on how to set up GitHub Secrets, refer to the official GitHub documentation.

## Customization

You can customize the list of LinkedIn accounts and pages to be tracked by modifying the input files (Accounts.xlsx and Pages.xlsx).

## Contributing

Feel free to contribute by submitting a pull request or opening an issue. Contributions to improve the functionality or add features are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Example Workflow (GitHub Actions)
**Here’s a brief description of the GitHub Actions workflow used in this project:**

-Run Frequency: Every 6 hours
-Environment: Ubuntu-latest with Python 3.12 and Playwright installed.
