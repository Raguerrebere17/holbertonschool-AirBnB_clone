<div align="center">

![AIRBnBBanner](https://github.com/Marulaska/holbertonschool-AirBnB_clone/assets/124218286/4c0cb688-95e2-4999-897d-40a19d2f5a66)

<h1> AirBnB Clone </h1>

> This repository contains all the tasks related to the "AirBnB Clone" project made by Holberton students.
>
> Throughout this project, we will learn how to create our own command interpreter, just like with the "Shell" project, but this time with a slight difference.

</div>

<div align="center">

![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png)

</div>

<br>

## Table of contents
* [About](#about)
* [Requirements](#requirements)
* [Instalation](#instalation)
* [File Structure](#project-files)
* [Usage](#usage)
* [Examples](#examples)
* [Authors](#authors)

## About
The AirBnb Clone is a project that comprises multiple interconnected stages.
You'll start by implementing The Console, which is a command interpreter designed to manage your AirBnB objects.

This serves as the initial step towards creating a comprehensive web application: the AirBnB clone. The Console is of utmost importance as it will be utilized in conjunction with all the subsequent projects, including HTML/CSS templates, database storage, APIs, front-end integration, and more.

## Requirements
```
python3
```
## Instalation
```python
$ git clone git@github.com:Marulaska/holbertonschool-AirBnB_clone.git
$./console.py
```

## Project Files
| File | File Hierarchy | Description |
| :---: | :---: | :---: |
| `console.py` | [console.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/console.py) | The main console file |
| `amenity.py` | [models/amenity.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/amenity.py) | The amenity subclass |
| `base_model.py` | [models/base_model.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/base_model.py) | The base model superclass |
| `city.py` | [models/city.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/city.py) | The city subclass | 
| `place.py` | [models/place.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/place.py) | Te place subclass |
| `review.py` | [models/review.py](https://github.com/mfcrespo/AirBnB_clone/blob/master/models/review.py) | The review subclass |
| `state.py` | [models/state.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/state.py) | The state subclass |
| `user.py` | [models/user.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/user.py) | The user subclass |
| `file_storage.py` | [models/engine/file_storage.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py) | The file storage class |

## Test Files
| File | File Hierarchy | Description |
| :---: | :---: | :---: |
| `test_amenity.py` | [tests/amenity.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_amenity.py) | The unittest module for amenity |
| `test_base_model.py` | [tests/base_model.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model.py) | The unittest module for base model |
| `test_base_model_dict.py` | [tests/base_model_dict.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model_dict.py) | The unitest module for base model|
| `test_city.py` | [tests/city.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_city.py) | The unittest module for city |
| `test_place.py` | [tests/place.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_place.py) | The unittest module for place |
| `test_review.py` | [tests/review.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_review.py) | The unittest module for review |
| `test_save_reload_user.py` | [tests/save_reload_user.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_save_reload_user.py) |The unittest for module user
| `test_state.py` | [tests/state.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_state.py) | The unittest module for state |
| `test_user.py` | [tests/user.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_user.py) | The unittest module for user |
| `test_file_storage.py` | [tests/test_models/test_engine/test_file_storage.py](https://github.com/Marulaska/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py) | The unittest module for file storage |


## Usage
### Basic usage of The Console

| Command | Usage | Example | Functionality |
| :---: | :---: | :---: | :---: |
| `help` | `help` | help | displays a list of the commands |
| `create` | `create <class>` | create BaseModel | Create a new instance |
| `show` | `show <class> <id>` | show BaseModel 787fds-fdf665-fdf843a1 | Shows a specific instance |
| `destroy` | `destroy <class> <id>` | destroy BaseModel 787fds-fdf665-fdf843a1 | Deletes a specific instance |
| `all` | `all` or `all <class>` | all BaseModel | Shows all instance or class |
| `update` | `update <class> <id> <attribute> <value>` | update BaseModel 787fds-fdf665-fdf843a1 name Betty | Update an attribute in an instance |
| `quit` | `quit` | quit | Quits the console |

### Interactive Mode

````python
$ ./console.py
(hbnb) create  <-- input 1
(hbnb) 
(hbnb) create BaseModel <-- input 2
````

### Non-interactive Mode

````python
$ echo "create BaseModel" | ./console.py
````

## Examples

### Interactive Mode

![](https://raw.githubusercontent.com/Marulaska/holbertonschool-AirBnB_clone/main/images/interac%20modef.gif)

### Non-Interactive mode

![](https://raw.githubusercontent.com/Marulaska/holbertonschool-AirBnB_clone/main/images/non-interacf.gif)




<div align="center">

## Authors
  
&ensp;[<img src="https://img.shields.io/badge/Raguerrebere17-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/Raguerrebere17)
&ensp;[<img src="https://img.shields.io/badge/Marulaska-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">](https://github.com/Marulaska)

<br>

![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png) ════════════════════ ![sea-horse](https://user-images.githubusercontent.com/110431271/229328604-b8c19c26-54e9-48d6-946f-91b0337deece.png)
