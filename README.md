# Installation

```
pytho3 -m pip requirements.txt
```

# Usage
### For Linux and Mac:

```
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

### For Windows cmd
Use set instead of export:

```
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

After that you need to initialize database:
```
flask init-db
```

And now you are ready to start app:
```
flask run
```

# Features

+ Register/Login
+ Creating, updating and deleting posts

To view specific user's profile visit: /id\<user-id\>

To view all publicated posts: /blog (debug features)
