# AirBnB Clone - The Console

## Description
This project is the first step towards building a full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Console Description
The console is a command line interpreter that permits management of the backend of AirBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

### How to Start It
Clone the repository and run the console.py file:

$ git clone https://github.com/[your-username]/alu-AirBnB_clone.git
$ cd alu-AirBnB_clone
$ ./console.py
```
```

### How to Use It
The console works in both interactive and non-interactive mode.

**Interactive mode:**
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$
```
```

**Non-interactive mode:**
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
```

### Available Commands
* `create` - Creates a new instance of a class
* `show` - Shows an instance based on class name and id
* `destroy` - Deletes an instance based on class name and id
* `all` - Shows all instances or all instances of a class
* `update` - Updates an instance based on class name and id
* `quit` - Exits the console
* `EOF` - Exits the console

### Examples
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
$
```
```

## Authors
See [AUTHORS](./AUTHORS) file for list of contributors to this project.
