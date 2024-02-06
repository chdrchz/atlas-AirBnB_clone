<body>
    <h1 align="center">The Console - An AirBnB Project</h1>
    <h3 align="center">A custom implementation of the console for AirBnB</h3>
    <p align="center"><em>Created by Allyson Ugarte and Savanna Davis</em></p>
    <p align="center">This command line interpreter is designed to offer an extensible environment for executing commands, managing tasks, and performing various operations seamlessly. Built using Python, it provides a powerful yet straightforward interface that can be easily customized and extended for further use.</p>
    <br>
    <h3>So, what's included?</h3>
    <details><summary><p>Classes</p></summary>
        <details><summary><em>BaseModel</em></summary>
            <ul>
            <br>
            <li><b>def __init__(self, *args, **kwargs):</b>    <em>Instantaion method.</em></li>
            <li><b>def __str__(self):</b>    <em>Object as string representation method.</em></li>
            <li><b>def save(self):</b>    <em>Saves an instance with the current date and time.</em></li>
            <li><b>def to_dict(self):</b>    <em>Returns a dictionary of all created instances.</em></li>
            </ul>
        </details>
        <details><summary><em>User</em></summary>
            <br>
            Contains a user's email, password, first name and last name. 
        </details>
        <details><summary><em>City</em></summary>
            <br>
            Contains a state id and name.
        </details>
        <details><summary><em>State</em></summary>
            <br>
            Contains a name.
        </details>
        <details><summary><em>Place</em></summary>
            <br>
            Contains a city id, user id, latitude, longitude, max guests, number of rooms and bathrooms.
        </details>
        <details><summary><em>Review</em></summary>
            <br>
            Contains a place id, user id, and text. 
        </details>
    </details>
    <details><summary><p>The Console</p></summary>
        <ul>
        <li><b>def preloop(self):</b>    <em>Method that prints if isatty(is it a terminal?) is false.</em></li>
        <li><b>def postcmd(self, stop, line):</b>    <em>Method that prints if isatty(is it a terminal?) is false.</em></li>
        <li><b>def do_quit(self, command):</b>    <em>Method to exit the HBNB console.</em></li>
        <li><b>def help_quit(self):</b>    <em>Prints the help documentation for quit method.</em></li>
        <li><b>def do_EOF(self, arg):</b>    <em>Handles the EOF (end of file) to exit the program.</em></li>
        <li><b>def help_EOF(self):</b>    <em>Prints the help documentation for EOF (end of file).</em></li>
        <li><b>def emptyline(self):</b>    <em>Overrides the emptyline method of CMD.</em></li>
        <li><b>def do_create(self, args):</b>    <em>Creates an object of any class.</em></li>
        <li><b>def help_create(self):</b>    <em>Prints the help documentation for the create method.</em></li>
        <li><b>def do_show(self, args):</b>    <em>Method to show an individual object.</em></li>
        <li><b>def help_show(self):</b>    <em>Prints the help documentation for the show method.</em></li>
        <li><b>def do_destroy(self, args):</b>    <em>Destroys a specified object.</em></li>
        <li><b>def help_destroy(self):</b>    <em>Prints the help documentation for the destroy method.</em></li>
        <li><b>def do_all(self, args):</b>    <em>Shows all objects, or all objects of a class.</em></li>
        <li><b>def help_all(self):</b>    <em>Prints the help documentation for the all command.</em></li>
        <li><b>def do_update(self, args):</b>    <em>Updates an instance based on the class name and id.</em></li>
        </ul>
    </details>
    <h3>Usage</h3>
    <p><b>To get started:</b> In the user's terminal, in the subdirectory where the user would like to install the new repository, type:<p>
    <h3>Thanks for stopping by! It was a blast making this!</h3>
</body>