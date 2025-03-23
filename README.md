# System Ticketing

System Ticketing is a Django-based web application designed to manage tickets for users and administrators. Users can create, view, edit, and delete tickets, while administrators have additional privileges to manage all tickets in the system.

## Features

- **User Authentication**: Users can register, log in, and log out.
- **Ticket Management**:
  - Users can create, view, edit, and delete their tickets.
  - Administrators can manage all tickets in the system.
- **Ticket Status**:
  - Tickets can have statuses such as `open`, `complete`, `done`, or `abandoned`.
  - Administrators can mark tickets as complete or done.
- **Admin Comments**: Administrators can add comments to tickets when marking them as done.
- **Responsive Design**: The application is styled with a simple and responsive layout.

## Project Structure
system_ticketing/ ├── db.sqlite3 ├── manage.py ├── README.md ├── system_ticketing/ │ ├── __init__.py │ ├── asgi.py │ ├── settings.py │ ├── urls.py │ ├── wsgi.py ├── templates/ │ ├── main.html │ ├── navbar.html ├── tickets/ │ ├── __init__.py │ ├── admin.py │ ├── apps.py │ ├── forms.py │ ├── models.py │ ├── tests.py │ ├── urls.py │ ├── views.py │ ├── migrations/ │ ├── templates/ │ ├── tickets/ │ ├── close_ticket.html │ ├── craete_tickets.html │ ├── delete_ticket.html │ ├── home.html │ ├── login.html │ ├── view_ticket.html

## Open Application 
Open the application in your browser at http://127.0.0.1:8000.

## Usage
- Register: Create a new user account.
- Login: Log in with your credentials.
- Create Tickets: Navigate to "Create Ticket" to submit a new ticket.
- View Tickets: View your tickets on the home page.
- Edit/Delete Tickets: Modify or remove your tickets.
- Admin Privileges: Administrators can manage all tickets and add comments.

## Requirements
- Python 3.10+
- Django 5.1.7

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details. ```