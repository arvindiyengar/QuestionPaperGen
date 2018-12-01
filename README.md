Script accepts the Subject and Topic. Once the user has fed the above information , it then prompts for distribution of difficulty levels stored in DB ( bank.py )

Currently: Math / Add Topic has full set of questions. To test happy path use the below config

Subject : math
Topic : Add
Hard: 40
Medium : 40
easy: 20

The application also checks if there are insufficient questions . It would spit out an custom error "InsufficientErrors"
