# Jeopardygame
## Capital One Winter 2020 Software Engineering Summit

Link to depolyed website: https://jtriviasearch.herokuapp.com/

Link to GitHub repository: https://github.com/ensardogrusoz/jeopardygame-project

## Prompt

To build a web app to find trivia questions by category, time, and difficulty

To complete this challenge, build a web application that:
* has a search function that displays results in an intuitive, responsive, mobile friendly, easy to navigate interface.
* gives users the ability to refine search results by:
  * date or timeframe aired (you can search by a day,  a week, a month)
  * trivia category
  * level of difficulty of the question
  * any other smart searching criteria you see fit

Optional: You may want to include these bonus features:

* Game board simulation with the categories and questions in the proper place (as it would be organized in the game with easier questions on top)
* Marking or saving questions into a "favorites" collection

## Tech Stack

### Front-End

* HTML/CSS
* Bootstrap

### Back-End

* Python/Django

### APIs

* JService API for trivia information
* Requests to parse JSON data

## Implemented Features

Time spent: **15** hours spent in total

The following **required** functionality is completed:

- [X] Searching page with search function displayed search results page
- [X] Ability to search with filters (category, airdate, difficulty)

The following **bonus** stretch features are implemented:


- [X] Sample random trivia categories on homepage
- [X] Specific trivia questions by category, airdate, and difficulty
- [X] UI Design (Flipping Cards) / Click to flip card for answers
- [X] new categories and random question button

## Future Features

Make website more dynamic in other platforms (mobile and web)
Improve searching algorithm for faster results

## Searching Algorithm:

* Python and the web framework, Django to organize the project, redirect between pages, send requests with the JService endpoint, filter trivia questions by category, airdate, and level of difficulty

* HTML & CSS to display web pages with Bootstrap designs and allows user interactions

## Challenges

* Parsing API data from JService
* Passing data from one page to another using Django forms

