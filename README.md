# AirBnB Clone - The Console

This project is the first step towards building a full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Project Description

The AirBnB Console is a command interpreter that allows users to manage AirBnB objects. It provides a simple interface to create, retrieve, update, and delete objects that represent the core entities of an AirBnB-like application.

### Key Features

- **Custom Command Interpreter**: Interactive shell for managing objects
- **Object-Oriented Design**: Clean class hierarchy with BaseModel as the foundation
- **File Storage System**: JSON-based persistence for data storage
- **Comprehensive Testing**: Full test suite ensuring code reliability
- **Multiple Model Classes**: User, State, City, Amenity, Place, and Review models

### Supported Classes

- **BaseModel**: The base class for all other classes
- **User**: Represents application users
- **State**: Represents geographical states
- **City**: Represents cities within states
- **Amenity**: Represents available amenities
- **Place**: Represents rental properties
- **Review**: Represents user reviews

## Command Interpreter

The command interpreter provides an interactive shell to manage AirBnB objects. It supports various commands to create, show, update, and delete objects.

### How to Start the Console

To start the command interpreter, run the following command in your terminal:

```bash
./console.py
```

or

```bash
python3 console.py
```

You should see the prompt `(hbnb) ` indicating that the console is ready to accept commands.

### How to Use the Console

The console supports the following commands:

#### Basic Commands

- **help**: Display help information
- **quit** or **EOF**: Exit the console
- **create**: Create a new instance of a class
- **show**: Display an instance based on class name and ID
- **destroy**: Delete an instance based on class name and ID
- **all**: Display all instances or all instances of a specific class
- **update**: Update an instance based on class name and ID

#### Command Syntax

```
(hbnb) <command> <class_name> [<id>] [<attribute_name> <attribute_value>]
```

### Examples

#### Starting the Console

```bash
$ ./console.py
(hbnb)
```

#### Getting Help

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
Usage: create <class>
        Create a new class instance and print its id.
```

#### Creating Objects

```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907

(hbnb) create User
2dd6ef5c-467c-4f82-9521-a772ea7d84e9

(hbnb) create State
2b74a781-d474-42fc-a837-b7b22c8b7d13
```

#### Showing Objects

```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2023, 10, 13, 10, 30, 45, 123456), 'updated_at': datetime.datetime(2023, 10, 13, 10, 30, 45, 123456)}

(hbnb) show User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
[User] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321), 'updated_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321)}
```

#### Listing All Objects

```bash
(hbnb) all
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2023, 10, 13, 10, 30, 45, 123456), 'updated_at': datetime.datetime(2023, 10, 13, 10, 30, 45, 123456)}", "[User] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321), 'updated_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321)}"]

(hbnb) all User
["[User] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321), 'updated_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321)}"]
```

#### Updating Objects

```bash
(hbnb) update User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9 first_name "John"
(hbnb) update User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9 last_name "Doe"
(hbnb) update User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9 email "john.doe@example.com"

(hbnb) show User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
[User] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2023, 10, 13, 10, 31, 15, 654321), 'updated_at': datetime.datetime(2023, 10, 13, 10, 32, 45, 987654), 'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com'}
```

#### Deleting Objects

```bash
(hbnb) destroy User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) show User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
** no instance found **
```

#### Exiting the Console

```bash
(hbnb) quit
$
```

## Project Structure

```
alu-AirBnB_clone/
├── console.py                  # Command interpreter
├── models/                     # Model classes
│   ├── __init__.py            # Initialization file
│   ├── base_model.py          # BaseModel class
│   ├── user.py                # User class
│   ├── state.py               # State class
│   ├── city.py                # City class
│   ├── amenity.py             # Amenity class
│   ├── place.py               # Place class
│   ├── review.py              # Review class
│   └── engine/                # Storage engine
│       ├── __init__.py        # Initialization file
│       └── file_storage.py    # FileStorage class
├── tests/                      # Unit tests
│   ├── test_console.py        # Console tests
│   ├── test_models/           # Model tests
│   └── ...
├── AUTHORS                     # Project contributors
└── README.md                  # Project documentation
```

## Testing

The project includes a comprehensive test suite to ensure code quality and functionality.

### Running Tests

To run all tests:

```bash
python3 -m unittest discover tests
```

To run specific test files:

```bash
python3 -m unittest tests.test_models.test_base_model
python3 -m unittest tests.test_console
```

To run tests with verbose output:

```bash
python3 -m unittest discover tests -v
```

## Requirements

- Python 3.8 or higher
- Ubuntu 20.04 LTS (recommended)
- All files should be executable
- Code should follow PEP 8 style guidelines

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MEDATTA0/alu-AirBnB_clone.git
```

2. Navigate to the project directory:

```bash
cd alu-AirBnB_clone
```

3. Make the console executable:

```bash
chmod +x console.py
```

4. Run the console:

```bash
./console.py
```

## License

This project is part of the ALU Software Engineering curriculum.

## Authors

See the [AUTHORS](AUTHORS) file for a list of contributors to this project.
