<h1>The Console - An AirBnB Project</h1>
<h2>Created by Allyson Ugarte and Savanna Davis</h2>
<h3>A custom implementation of the console for AirBnB</h3>

<h2>Introduction</h2>

<p>Placeholder text</p>

<details><summary>Classes</summary>
    <details><summary><em>BaseModel</em></summary>
        <ul>
        <li>def __init__(self, *args, **kwargs): <em>Instantaion method.</em></li>
        <li>def __str__(self): <em>Object as string representation method.</em></li>
        <li>def save(self): <em>Saves an instance with the current date and time.</em></li>
        <li>def to_dict(self): <em>Returns a dictionary of all created instances.</em></li>
        </ul>
    </details>
    <details><summary><em>User</em></summary>
        Contains a user's email, password, first name and last name. 
    </details>
    <details><summary><em>City</em></summary>
        Contains a state id and name.
    </details>
    <details><summary><em>State</em></summary>
        Contains a name.
    </details>
    <details><summary><em>Place</em></summary>
        Contains a city id, user id, latitude, longitude, max guests, number of rooms and bathrooms.
    </details>
    <details><summary><em>Review</em></summary>
        Contains a place id, user id, and text. 
    </details>
</details>

