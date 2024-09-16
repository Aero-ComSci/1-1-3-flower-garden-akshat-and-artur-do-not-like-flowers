[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/CH30njZ-)
# 1.1.3FlowerGarden

## What is Tokenization?
Tokenization in the Code:
In this code, tokenization refers to the process of breaking down a text input (the prompt) into separate pieces (tokens) to extract relevant information. Specifically, tokenization involves:
 - Lowercasing and Removing Punctuation: The prompt is converted to lowercase and stripped of punctuation to standardize the input for easier processing.
 - Extracting Numbers and Flower Names: Using regular expressions, the code identifies and extracts numbers and associated flower names from the cleaned text.
 - Mapping Numbers to Flower Types: The extracted numbers are used to determine how many of each type of flower to draw.

## High-Level Explanation
This code creates a drawing of different flowers based on user input. It takes a prompt describing quantities and types of flowers, tokenizes the input to extract this information, and then uses the Turtle graphics library to draw the specified flowers on the screen. It supports roses, tulips, sunflowers, iris, and peonies, and adjusts their size and spacing based on the input. If no valid flowers are mentioned, it simply outputs just that.

Here is the link to a screen recording of our project: [https://drive.google.com/drive/u/0/home](https://drive.google.com/file/d/1Ti8LXe2-A7AiXB_wnaL_ia_dULorR0ou/view?usp=sharing)

Here are some results from different inputs of flowers: 

![Screenshot 2024-09-16 144049](https://github.com/user-attachments/assets/873e70d6-0559-404f-970e-1e74848459bf)

![Screenshot 2024-09-16 144109](https://github.com/user-attachments/assets/1f42d178-2bd2-438c-a5c6-d20fe13236bb)

![Screenshot 2024-09-16 144154](https://github.com/user-attachments/assets/16eafe44-ace6-4e5a-aa40-0a16b9b77b4a)
