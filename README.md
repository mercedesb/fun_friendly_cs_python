# Fun, Friendly Computer Science -- Python

Code samples to support my "Fun, Friendly Computer Science" talk. This is an abbreviated version of this talk. The [Ruby version](https://github.com/mercedesb/fun_friendly_cs_ruby) and [Javascript version](https://github.com/mercedesb/fun-friendly-cs-js) include samples to illustrate the 4 principles of object-oriented programming.

## Talk Abstract
Computer science concepts like Big O Notation, set theory, and data structures sound intimidating, but they don’t have to be! This talk will dive into some fundamental computer science topics and debunk the myth that only ‘real’ programmers know CS.

Whether you are a bootcamp grad, self-taught career switcher, or someone who, like me, didn't pay attention in night class, join me as we explore some computer science theory behind the code we write every day through fun illustrations and real-world examples.

## Django

All of the code samples are written in [Django](https://www.djangoproject.com/). This is a vanilla Django setup.

### Versions
This project uses Python3 and Django version 2.2.5. It assumes you already have [Django installed](https://docs.djangoproject.com/en/2.2/intro/install/).


## Project set up
```
git clone https://github.com/mercedesb/fun_friendly_cs_python.git
cd fun_friendly_cs_python
python3 manage.py runserver
```

## Running the tests
This project uses [unittest](https://docs.python.org/3/library/unittest.html) as the unit testing framework.

```
python3 manage.py test
```

## Admin user
The database in this project is seeded with a super user.

username: `admin`

password: `admin`