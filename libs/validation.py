

def validateLevel(questLevelState):
    totalMarks = 100
    sum = 0
    for value in questLevelState["level"]["marks"].values():
        sum += value
    if (sum != totalMarks):
        raise Exception("Total marks not equals"+totalMarks)


def validateTopics(topicKeys, topic):
    if (topic not in topicKeys):
        raise Exception("Topic not found")
