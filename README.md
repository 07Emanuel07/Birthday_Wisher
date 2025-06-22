# Birthday Wisher

I created a **Birthday Wisher** program to automate the process of sending birthday wishes via email.
This project leverages data from a CSV file containing birthday information and utilizes email services to deliver personalized messages.

## Key Features

- **Data Handling**: Utilizes the `pandas` library to read and manipulate birthday data from a CSV file.

- **Randomized Messaging**: Selects a birthday message template at random from a set of predefined templates, ensuring a unique experience for each recipient.

- **Email Automation**: Uses the `smtplib` library to send birthday wishes via email.

- **Date Management**: Employs the `datetime` module to check for upcoming birthdays.
