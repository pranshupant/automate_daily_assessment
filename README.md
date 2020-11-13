# Automate Daily Self-Assessment
Automates the daily COVID-19 self-assessment submission required by my University

After getting repeatedly flagged for not submitting daily self-assessment of my health (for COVID), I decided to automate the daily form submission process.

### I implemented the following:

  * Created a cronjob which submits the form daily at 8AM by running a shell script.
  
  * Automated the form completion and submission using Selenium.
  
  * On successful submission of form a notification is sent to my Slack using a webhook.
  
  * Wrote a macro on the MacroDroid Android App to automatically accept the MFA prompts.
  
### Notes:

 * Add your authentication credentials to auth.py.
 * Modify run.sh to use your local python/conda environment.
 * Create a webdrivers/ directory with binaries for selenium drivers that you can get using the following command:

 ```bash
 curl https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip -o chromedriver_linux64.zip
 ```
 
  
### To Run

Add the contents of crontab.txt to your crontab.

```bash
crontab -e

0 8 * * * cd /---Directory-of-choice-here---/automate_daily_assessment/ && DISPLAY=:0 ./run.sh > /dev/null 2>&1

```
