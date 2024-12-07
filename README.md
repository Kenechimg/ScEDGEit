<p align="center">
  <img src="Images_SchEDGEit/SchEDGEit_logo.jpg" alt="Image Description">
</p>



# SchEDGEit  
### Scheduling Comes with an Edge📝  
🧑‍💻[Ken Luigi M. Magnaye](https://github.com/Kenechimg) <br>  
**IT-2104**
<hr style="width: 50%; height: 1px; background-color: #4CAF50; border: none; margin: 20px auto;">

<div style="border: 1px solid #4CAF50; border-radius: 8px; padding: 10px; background-color: #E8F5E9; margin: 20px 0;">
<details>
<summary><strong> Table of Contents📚 </strong></summary>  

I. Project Overview  
II. Application of Python Concepts and Libraries  
III. Integration with SDG  
IV. Instructions for Running the program 

</details>

 <hr style="width: 50%; height: 1px; background-color: #4CAF50; border: none; margin: 20px auto;">

<div style="border: 1px solid #4CAF50; border-radius: 8px; padding: 10px; background-color: #E8F5E9; margin: 20px 0;">  

### I. Project Overview👁️‍🗨️
**SchEDGEit** is a program designed to help students organize their schedules effectively. Users can create tasks with specific deadlines, assign priority levels, and view them sorted by either due date or priority, ensuring that essential tasks are handled first.  

**The program allows users to:**  
•	Add tasks with due dates and different priority level.  
•	View tasks sorted by its priority level or date.  
•	Mark the tasks that are completed.  
•	Delete the finished or unwanted tasks from the list.  
All added tasks are saved using JSON, ensuring that the users to-do list is always there when they return.

<hr style="width: 50%; height: 1px; background-color: #4CAF50; border: none; margin: 20px auto;">

<div style="border: 1px solid #4CAF50; border-radius: 8px; padding: 10px; background-color: #E8F5E9; margin: 20px 0;">  
  
### II. Application of Python Concepts and Libraries📖  

This project demonstrates the application of several key Python concepts and libraries:  

**1.	Object-Oriented Programming (OOP):**  

-this allows the code to be modular, reusable, and easier to maintain. The classes Task and ToDoList implement OOP principles:  

•	 **Encapsulation:** Task-related attributes (such as ``description``, ``date``, ``priority``) and behaviors (``mark_complete``, ``to_dict``) are encapsulated within the Task class. Similarly, the ToDoList class encapsulates all logic related to managing multiple tasks.  

•	**Static Methods:** The ``from_dict()`` method in the Task class demonstrates encapsulated functionality for creating instances from JSON data.  

**2.	File Handling with JSON:**  

- Using JSON ensures tasks are stored persistently between sessions in a lightweight and human-readable format. The json library simplifies serialization and deserialization of data. It is found within:  

o	``ToDoList.save_tasks()`` where it writes tasks to a file in JSON format.   

o	``ToDoList.load_tasks()`` where it reads the JSON file to populate the tasks list.  

The datetime module is used in ``ToDoList.view_tasks()`` to sort tasks by date  

**3.	Error Handling:**  

This ensures the application doesn’t crash when encountering issues with the tasks.json file. Instead, the program recovers gracefully. It is found within:  

o	``ToDoList.load_tasks()`` where exceptions are handled for cases where the file is missing or contains invalid JSON data:  

**4.	Datetime Management:**  

This sorts tasks by due date ensures that users can prioritize tasks with approaching deadlines. It is found within:  

o	the datetime module and is used in ``ToDoList.view_tasks()`` to sort tasks by date  

**5.	Command-line Interaction:**  

This design provides a simple and user-friendly way to interact with the program in a terminal or command-line environment. It is found within:  

o	the ``main()`` function where it provides an interactive menu using ``input()`` to let users add, view, complete, or delete tasks

<hr style="width: 50%; height: 1px; background-color: #4CAF50; border: none; margin: 20px auto;">

<div style="border: 1px solid #4CAF50; border-radius: 8px; padding: 10px; background-color: #E8F5E9; margin: 20px 0;">  

**III. Integration with SDG🌍**  

**Sustainable Development Goal (SDG) 4:** Quality Education seeks to ensure inclusive and equitable quality education and promote lifelong learning opportunities for all. This goal emphasizes improving access to education, enhancing educational outcomes, and fostering a culture of continuous learning and skill development for individuals of all ages. SchEDGEit supports this goal by providing a structured system that helps individuals and communities organize their tasks, manage deadlines, and prioritize goals, fostering better time management and productivity.  

This project contributes to SDG 4 in three significant ways. First, it helps learners and educators manage their time effectively by organizing academic tasks, assignments, and learning objectives. By sorting tasks by priority or due date, it ensures that critical deadlines are met, promoting better academic outcomes and reducing stress. Second, it supports lifelong learning by encouraging users to set personal development goals, such as learning a new skill or completing educational milestones and tracking their progress. The ability to mark tasks as completed fosters a sense of achievement and motivates users to continue learning. Lastly, the system builds essential planning and organizational skills by integrating features like task prioritization, deadline management, and progress tracking. These skills are crucial for individuals to succeed academically and professionally, contributing to their long-term personal and educational growth.   

<hr style="width: 50%; height: 1px; background-color: #4CAF50; border: none; margin: 20px auto;">

<div style="border: 1px solid #4CAF50; border-radius: 8px; padding: 10px; background-color: #E8F5E9; margin: 20px 0;">

**IV. Instructions for Running the program🖥️🖱️**  

**1. Interacting with the Application:**  

o	Upon starting the program, you’ll see a menu with options to add, view, complete, or delete tasks.  
o	Follow the prompts to interact with your to-do list.  

**2. JSON-based Persistence:**  

o	Tasks are saved in the tasks.json file in the project directory.  
o	You can edit the JSON file manually if needed.  

**Example Usage**  

**Adding a Task:** 

Choose an option: 1  
Enter task name/description: Project in ACP  
Enter task due date (YYYY-MM-DD): 2024-11-26  
Enter task priority (1 for high, 3 for low): 1  

**Viewing Tasks:**  

Choose an option: 2  
Sort tasks by 'priority' or 'date': priority  
Current Tasks:  
Project in ACP (Due: 2024-11-26, Priority: 1) - Pending  

**Marking a Task as Complete:** 

Choose an option: 3  
Enter task name/description to mark as complete: Project in ACP  
Task 'Project in ACP' marked as complete.  

**Deleting a Task:**  

Choose an option: 4  
Enter task name/description to delete: Project in ACP  
Task 'Project in ACP' deleted.  

**Exiting the Program**
Choose an option: 5  
Exiting the program.  


