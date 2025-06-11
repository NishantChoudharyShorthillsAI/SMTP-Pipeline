import smtplib
import os
from email.message import EmailMessage

# Email details
recipients = ['aryan2@shorthills.ai', 'nishant.choudhary@shorthills.ai']
subject = f"CI/CD Pipeline {'✅ SUCCESS' if os.getenv('JOB_STATUS') == 'success' else '❌ FAILURE'}"
body = f"""
Hello Team,

The CI/CD pipeline has completed with status: {os.getenv('JOB_STATUS').upper()}.

Repository: {os.getenv('GITHUB_REPOSITORY')}
Workflow: {os.getenv('GITHUB_WORKFLOW')}
Run: {os.getenv('GITHUB_RUN_ID')}
URL: https://github.com/{os.getenv('GITHUB_REPOSITORY')}/actions/runs/{os.getenv('GITHUB_RUN_ID')}

Regards,
CI/CD Bot
"""

# Compose the message
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = os.getenv("SMTP_USERNAME")
msg['To'] = ', '.join(recipients)
msg.set_content(body)

# Send the email
try:
    with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as smtp:
        smtp.starttls()
        smtp.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
        smtp.send_message(msg)
    print("✅ Email sent successfully")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
