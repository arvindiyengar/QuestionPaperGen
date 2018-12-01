import sys
from db.bank import questionBank
import random
import math
from errors.exceptions import InsufficientErrors
from libs.validation import validateLevel, validateTopics
from libs.paper import generateQuestionPaper, getCountQuestions, displayPaper

questLevelState = {

}
questLevelState['set'] = []
questLevelState['level'] = {}
questLevelState['level']["count"] = {}
questLevelState["level"]["marks"] = {}


print("Welcome to Question Paper Generator script.\n")
proceed = input("Do you wish to proceed? [yes/no]: \t")
if(proceed in ["Yes", "yes", "y", "Y", "YES"]):
    print("Enter the difficulty level and their split.")
    try:
        print("Subjects currently in DB. Please select any one\n")

        subKeys = questionBank["subjects"].keys()
        for each in subKeys:
            print(" - "+each)
        subject = input("\nEnter Subject: \t")
        if (subject not in subKeys):
            raise Exception("Subject error")

        topicKeys = questionBank["subjects"][subject]["topics"].keys()
        print("\nSelected Subject: "+subject +
              " . Topics for the selected subject\n")
        for each in topicKeys:
            print(" - "+each)
        topic = input("\ntopic: \t")
        validateTopics(topicKeys, topic)
        print("Topic selected: "+topic +
              " . Levels found for this topic . Please state the distribution\n")
        levelKeys = questionBank["subjects"][subject]["topics"][topic]["difficulty"].keys(
        )
        for each in levelKeys:
            questLevelState["level"]["marks"][each] = 0
            questLevelState["level"]["marks"][each] = int(
                input("- "+each+"\t"))

        validateLevel(questLevelState)
        getCountQuestions(questLevelState)
        generateQuestionPaper(questLevelState, subject, topic)
        print("\n\n**************** Question Paper ****************\n\n")
        displayPaper(questLevelState)
    except Exception as e:
        print("okok", e)
        sys.exit(1)
else:
    sys.exit(0)
