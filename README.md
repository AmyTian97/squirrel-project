# Squirrel-Tracker
## Project Group 52, Section 1
## UNIs: [yt2680, yz3630]
## Link to the server: https://core-stronghold-253812.appspot.com/
[Link to the server](https://core-stronghold-253812.appspot.com/)

We built an Django project that can import the 2018 Central Park Squirrel Census data and allow our client to  view, add, edit(update and delete) and export squirrel data. 
On '/track/map', there is  a map which displays the location of the squirrel sightings on an OpenStreets map.
On '/track/sightings', there is a table listing all the data of the squirrels, with an add button and an edit button which can jump the corresponding page.
On '/track/sightings/add', there is a page for creating a new sighting.
On '/track/sightings/<unique-squirrel-id>', there is a page with the information of the squirrel with that specific id, with an update button and a delete button for this two operation.
On '/track/sightings/<unique-squirrel-id>/update', the specific sighting can be updated.
On '/track/sightings/<unique-squirrel-id>/delete', the specific sighting can be deleted.
On '/track/sightings/stats', there are some general stats about the sightngs.
