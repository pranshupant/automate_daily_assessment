# Automate Daily Self-Assessment
Automates the daily COVID-19 self-assessment submission required by CMU

After getting repeatedly flagged for not submitting daily self-assessment of my health (for COVID), I decided to automate the daily form submission process.

### I implemented the following:

  * Created a cronjob which submits the form daily at 8AM.
  
  * Automated the form completion and submission using Selenium.
  
  * On successful completion of form a notification is sent to my Slack using a webhook.
