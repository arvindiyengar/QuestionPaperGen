import random
import math
from errors.exceptions import InsufficientErrors
from db.bank import questionBank


def getCountQuestions(questLevelState):
    for key in questLevelState["level"]["marks"].keys():
        questLevelState["level"]["count"][key] = math.floor(
            questLevelState["level"]["marks"][key]/questionBank["marksAllocated"][key])


def generateQuestionPaper(questLevelState, subject, topic):

    for level, value in questLevelState["level"]["count"].items():
        try:
            questLevelState["set"] += random.sample(questionBank["subjects"][subject]
                                                    ["topics"][topic]["difficulty"][level], value)
        except Exception:
            raise InsufficientErrors("Count Error in "+subject +
                                     " - " + topic + " - " + level)


def displayPaper(questLevelState):
    print("Time limit : 1 hr\n\n")
    print("Total Questions: " + str(len(questLevelState["set"]))+"\n")
    for id, question in enumerate(questLevelState["set"]):
        print(str(id)+". "+question["text"] +
              " ---  Marks : " + str(question["marks"]))
