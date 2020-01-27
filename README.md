# Flask (Hashing, Sessions, and Authentication): Solution Code

This repo is to be used with the [Flask: Hashing, Sessions, and Authentication](https://git.generalassemb.ly/sei-den-instructors/base-curriculum/blob/master/unit_3/w08d02/instructor_notes/6.%20FLASK_HASHING_SESSIONS_AUTHENTICATION.md) lesson.

## Instructor Directions
1. Once the lesson is complete, fork this repo into the cohort organization.
1. Provide the forked repo to the students.

## Student Directions
1. If you only want to view the solution code, there's no need to go any further. If, however, you'd like to run this code, move on to the following steps.
2. Fork and clone this repo. (Confirm that the url you're using to clone includes your username.)
3. Once it's cloned, navigate into the `lesson-flask-hashing-sessions-and-authentication-solution-code` directory.
4. Run `virtualenv .env -p python3` and then `source .env/bin/activate` to create and activate a virtual environment.
5. To install requirements, run either `pip install -r requirements.txt` (Python 2) or `pip3 install -r requirements.txt` (Python 3). (Note: If you run into issues with installing psycopg2, you can try running `pip install psycopg2-binary`. See [documentation](http://initd.org/psycopg/docs/install.html#install-from-source).)Then run `pip freeze > requirements.txt`.
6. Open in your code editor if you'd like.
7. If you want to start the server, run `python app.py`.
