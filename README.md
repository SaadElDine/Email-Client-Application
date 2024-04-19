# Email Client Project

![image](https://github.com/SaadElDine/Email-Client-Application/assets/113860522/da55f139-2bea-45dd-bf86-fda4d5ec3b0a)


## Objective
The objective of this project is to develop a Python-based email client application that can send and receive emails using the smtplib and imaplib libraries respectively. The application should be able to establish a TCP connection with a mail server, dialogue with the mail server using the SMTP and IMAP protocols, send an e-mail message to a recipient via the mail server, fetch the latest email from the mailbox, and finally close the TCP connection with the mail server.

## Project Structure
The project is organized into the following files:

- `send_email.py`: Contains the `send_email` function for sending emails using the SMTP protocol.
- `receive_email.py`: Contains the `receive_email` function for receiving emails using the IMAP protocol.
- `gui.py`: Contains the graphical user interface code using tkinter for the email client application.

## Implemented Features

### 1. Sending Emails
- The application allows users to send emails using the SMTP protocol.
- Users can specify the sender's email, password, recipient's email, subject, and body of the email.
- The `send_email` function in `send_email.py` handles the email sending process.

### 2. Receiving Emails
- Users can receive emails using the IMAP protocol.
- The application fetches the latest email from the mailbox and displays its body.
- The `receive_email` function in `receive_email.py` is responsible for fetching and displaying emails.

### 3. Graphical User Interface (GUI)
- The GUI for the email client application is developed using the tkinter library.
- Users can input their email, password, recipient's email, subject, and body in the GUI.
- Buttons are provided in the GUI to send and receive emails.

### 4. Error Handling
- The application includes error handling mechanisms to manage errors during the sending or receiving process.
- Appropriate error messages are displayed to the user in case of errors.

### 5. Push Notifications
- A push notification system using Plyer is implemented to alert the user when a new email arrives in the mailbox.
- Notifications are displayed to the user on the desktop.

### 6. Mail Server
- For testing purposes and to maintain privacy, the application uses mail.tm or an alternative mail server.

### 7. Code Structure
- The code is well-structured, properly indented, and includes comments where necessary.
- Each functionality is implemented in separate files (`send_email.py`, `receive_email.py`, `gui.py`) to maintain code organization.

By implementing these features, the email client application provides a comprehensive solution for sending and receiving emails with a user-friendly interface and error handling capabilities.

## How to Run
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the `gui.py` file to start the email client application.

## Testing
- Tested sending emails to different user accounts and servers.

![image](https://github.com/SaadElDine/Email-Client-Application/assets/113860522/b3d962c1-1239-4016-a935-20791799dacc)

  
- Tested receiving emails from different email accounts.

  ![image](https://github.com/SaadElDine/Email-Client-Application/assets/113860522/77a87103-b067-46bb-89e8-ffd336526483)


## Future Improvements
- Implement email threading for faster processing.
- Add support for attachments.
- Improve error handling and user feedback.

## Conclusion
The email client application provides a simple and intuitive way to send and receive emails using Python. It can be further enhanced and customized to meet specific requirements and preferences.
