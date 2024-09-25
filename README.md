This submission includes a basic HTML/CSS web page, a Python web server, dynamic content integration, form handling, and data persistence. The implementation follows the requirements provided in five exercises:

Exercise 1: Simple Web Page Setup: Created a basic web page with a header, navigation menu, main content area, and footer.

Exercise 2: Python Web ServerFunctionality:

Serves the HTML/CSS page created in Exercise 1.

Includes appropriate routes to handle GET requests.
Routes:
/: Serves the home page.
/about: Displays information about the website.
/contact: Provides contact details.
/form: Displays a form for user input.
/submissions: Shows user submissions.

Exercise 3: Dynamic Content
Integrated current date and time into the web page using Flask templating.
The {{ time }} variable is dynamically passed to the web page when it is rendered.
Exercise 4: Form Handling
Form: Added a form to collect user details (name and email) on the web page.

Form Submission:
A Python route handles POST requests for form submissions.
After submission, the page displays the entered data.

Exercise 5: Data Persistence
Data Storage:
Form submissions are stored in a local file (submissions.txt) to ensure persistence.
A separate route displays all the stored submissions on a new page.
The /submissions page reads the data from the file and shows it in a table format.

To Run: cmd:python3 app.py

