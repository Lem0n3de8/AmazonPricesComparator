# Amazon Price Comparator

About the project : 

> The goal of the project is to create a small local Python application that allows tracking the price evolution for Amazon products.
> As of now, there are still some uncertainties about how exactly will the frontend part be handled.

Beginner-friendly Project :

> The goal of the project is also to give people a project to work on. You don't need to know everything about Python to start working on this project.
> If you want to work on a project, your help is more than welcome!

 
---


## Table of Contents

- [About the project](#amazon-price-comparator)
- [Table of Contents](#table-of-contents)
- [Roadmap](#roadmap)
- [How to clone](#how-to-clone-the-repository)
- [How to contribute](#how-to-contribute)
- [List of Contribuitions](#list-of-contribuitions)


---


## Roadmap

In this section you'll find the list of all the important features for the project. 

|Feature name|Feature description|Status|Author|
|------------|-------------------|------|------|
|Amazon Fetcher|Create the main class to fetch product data from Amazon Website|Completed|[Lem0n3de8](https://github.com/Lem0n3de8)|
|Fetch From Txt |Implement utility class to automate the fetching of data for multiple links |Completed|[Lem0n3de8](https://github.com/Lem0n3de8)|
|SQL Database|Create a module that will allow to initialize a local sqlite database for prices storage|Completed|[Lem0n3de8](https://github.com/Lem0n3de8)|
|Testing Units| Create testing units for the existing modules|Not started||
|Data Storage|New module to store the data retrieved from amazon into the local database|Not started||


---


## How to clone the repository

Note: Python [3.13.11](https://www.python.org/downloads/release/python-31311/) or newer required

Note: SQLite [3.51.1](https://sqlite.org/releaselog/3_51_1.html) or newer required (use Homebrew on MacOs)

### 1. Clone
``` shell
git clone https://github.com/Lem0n3de8/AmazonPriceComparator
cd AmazonPriceComparator
```

### 2. Create Virtual Environment
```shell
python -m venv venv
```

### 3. Activate Virtual Environment
- On Windows:
```shell
.\venv\Scripts\activate
```
- On MacOs and Linux:
```shell
source venv/bin/activate
```

### 4. Install Dependencies
```shell
pip install -r requirements.txt
```


---


## How to contribute

Anyone is welcome to contribute to the project!

#### Steps to contribute 🤝 : 
- Fork the repository
- Clone the project 
- Make your changes and push to your fork
- Open a pull request

#### What can you work on ⚒️ ?
- Check the issues tab and see if there's something you can work on.
- Check the list of task below. You can try to implement some features. 
- If you have an idea for a new feature that's not in the issues or in the list of task, you can either submit it via the issues tab or directly work on it and create a pull request.

#### List of tasks 📋 : 
- [ ] Implement fetching for other types of file 
    - Currently only .txt supported, maybe add .csv and .json 
- [ ] Improve comments and docstrings
- [ ] Add project structure in README.md
- [ ] Add CONTRIBUITING.md to repo
- [x] Add LICENSE.md (mit) to repo


---


## List of contribuitions

Below are displayed all contribuitions:

|Feature name|Feature description|Author|
|------------|-------------------|------|
