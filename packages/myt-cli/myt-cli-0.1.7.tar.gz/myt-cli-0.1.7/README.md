# myt-cli
My Tasks - A personal task manager

### What is it
A simple command line task manager written in python. It is inspired from taskwarrior but with no where near as much functionality. 

### What can it do
You can add tasks with descriptions, due dates and notes. You can groups tasks together and can add tags to them. Tasks can be modified. Tasks can also be set to indicate they are currently being worked on. There is functionality to set recurring tasks

### Screenshots
1. The default view
![TaskView](https://github.com/nsmathew/myt-cli/blob/master/images/TaskAdd.png?raw=true)
&nbsp;
2. Information displyed after adding a task
![TaskView](https://github.com/nsmathew/myt-cli/blob/master/images/TaskView.png?raw=true)
### Examples
1. Add a simple task
`myt add -de "Buy gifts" -du 2021-06-25 -gr PERS.SHOPPING -tg birthday,occassions`
&nbsp;
1. Add a recurring task
`myt add -de "Pay the rent" -re M -du 2021-06-25 -hi -5 -gr PERS.FINANCES -tg bills`
This task is scheduled for the 25th of every month. Using the 'hide' option tt will be hidden until 5 days from the due date for every occurence in the tasks default view 
&nbsp;
1. Add a recurring task with an end date
`myt add -de "Project weekly catch ups" -re WD1,2,5 -du +0 -en +30 -gr WORK.PROJECTS`
This adds a recurring task for every Monday, Tuesday and Friday and ending in 30 days from today

Other functionality in the app can be explored using the app's help 

### Installation
Install using pip: `pip install myt-cli`

### Technology
* Python 3
* Sqlite3

### Links
- Github - https://github.com/nsmathew/myt-cli
- PyPi - https://test.pypi.org/project/myt-cli

### Contact
Nitin Mathew, nitn_mathew2000@hotmail.com
