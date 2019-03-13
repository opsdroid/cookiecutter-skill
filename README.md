# cookiecutter-skill

This is a template skill for use with cookiecutter to use when creating new opsdroid skills.


## Usage

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

    pip install --user cookiecutter

Create your application from this template:

    cookiecutter https://github.com/opsdroid/cookiecutter-skill.git

All set!

    cd skill_name

Start working on your skill!


## Features

Included:

 - Minimal skill with hello world example.

 - Empty `requirements.txt` file for you to put your python dependencies in.

 - A `README` to record how to use and configure your skill.


# Contributions

... are welcome! Feel free to create a pull request to fix bugs or keep up to date.

If you think some additional feature is indispensable, feel free to create an issue or a pull request, but bare in mind
that the goal of this template is to stay a "minimal" one. If you would like to add a feature, maybe best way to do so
is to make it optional and off by default then. One can use cookiecutter's choice variables, and, ultimately, hooks,
in order to create an optional feature.
