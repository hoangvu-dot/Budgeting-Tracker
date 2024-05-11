<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#how-to-use">How to use</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About the Project

There are many applications for financial optimization right now, but I consider them a bit complicated to use so I want to create one that is much easier to operate.

![image](https://github.com/hoangvu-dot/Budgeting-Tracker/assets/141603999/062e85da-96fd-40ef-be08-619dbab7d67a)
Above is the image of the interface when you run this project. 

### Built With
* [![Streamlit][Streamlit.io]][Streamlit-url]
* [![MySQL][mysql.com]][mysql-url]

## Getting Started

This application is run together with MySQL database, so you need to have MySQL installed on your computer.
    

### Prerequisites
You can download a MySQL database at [https://www.mysql.com/downloads/](https://www.mysql.com/downloads/)

### Installation


1. Clone the repo:
```sh
   git clone https://github.com/hoangvu-dot/Budgeting-Tracker.git
```
2. Install Packages:
```sh
pip install -r Requirements.txt
```
### How to use

It is a bugeting-trackers that can take input and display on the screen the necessary statistic for you to optimize your monthly spending.
A green box on the first column will change into RED if you spend more than 3000 in that month.

+ Steps:
1. Setting up your MySQL and changing the password based on your setting:
+ This snippet of code can be found in Database.py at the end of the package.
![image](https://github.com/hoangvu-dot/Budgeting-Tracker/assets/141603999/fcfc4e2b-6f98-4aac-805f-3665a3929a15)


* You can leave it blank "" or change to your password which is saved in MySQL
2. Run the Application.py file to open the app
```sh
python Application.py
```
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact
* Hoang Vu - vguhoangvu@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Streamlit.io]: https://camo.githubusercontent.com/a5416a5bfad3868ac588895ed44a9d3658a3b96891f229ead8ce064ff0e078a5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d616465253230776974682d53747265616d4c69742d7265643f7374796c653d666f722d7468652d6261646765266c6f676f3d53747265616d4c6974
[Streamlit-url]: https://streamlit.io/

[mysql.com]: https://www.mysql.com/common/logos/powered-by-mysql-125x64.png
[mysql-url]: https://www.mysql.com/
