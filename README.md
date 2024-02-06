<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Console - An AirBnB Project</title>
</head>
<body>
    <h1>The Console - An AirBnB Project</h1>
    <br>
    <h2>A custom implementation of the console for AirBnB</h2>
    <h3>Created by Allyson Ugarte and Savanna Davis</h3>
    <p>This command line interpreter is designed to offer an extensible environment for executing commands, managing tasks, and performing various operations seamlessly. Built using Python, it provides a powerful yet straightforward interface that can be easily customized and extended for specific use cases.</p>
    <h2>So, what's in here?</h2>
    <details><summary>Classes</summary>
        <br>
        <details><summary><em>BaseModel</em></summary>
            <ul>
            <li>def __init__(self, *args, **kwargs): <em>Instantaion method.</em></li>
            <li>def __str__(self): <em>Object as string representation method.</em></li>
            <li>def save(self): <em>Saves an instance with the current date and time.</em></li>
            <li>def to_dict(self): <em>Returns a dictionary of all created instances.</em></li>
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
</body>