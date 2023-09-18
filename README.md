# Vital Bio Python Coding Challenge

## The Challenge
Given a file of participants, each participant should be randomly assigned another participant to get a gift for. A participant should not be assigned to get themselves a gift, and additionally it should be possible to predefine some assignments that are not allowed. A secret gift exchange generator would probably notify the participants of their assignment by email, but for this purpose there is no need to actually send an email. In place of that you can just have a print statement that is something like "Notifying asa@vitalbio.com that he is assigned to get a gift for Leah Skerl"

## Thought process
We are told that we are working with data given in a file but we do not know the file type. For now, we are going to assume that we will be working with csv file, and we will be putting this file in the resources directory so everytime we run this script we do not 
+ ask the user for participants' info
+ hard code the info and/or change it for different test datasets

### Edge cases
1. Only 1 participant in the file. 
2. Multiple participants in the file but all the others efficiently exchanged gifts, leaving only 1 without receiving.

We will be having 2 methods doing all of our work, `assign_gifts()` and `file_reader()`

### `file_reader()` method
This method will be openining the file named `participants.csv` located in `resources` directory. This method opens the file, and saves the data in the dictionary called `info` saves it in the pair of name and email. 

### `assign_gifts()` method
This method is responsible for making sure the gifts are assigned to the person as specified in the challenge and covering the identified edge cases.
> It might seem that the line where we are removing a participant from the list is useless. However, the said list keeps decreasing every iteration so our processing time is reduced improving the efficiency. 
