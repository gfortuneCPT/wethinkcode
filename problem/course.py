def create_outline():

    headings = ("Course Topics:", "Problems:","Student Progress:")
    topics = {'Introduction to Python', 'Tools of the Trade', 
                'How to make decisions','How to repeat code',
                'How to structure data','Functions','Modules'}
                
    sort_topics = sorted(topics)
    
    print(headings[0])
    problems = dict()

    for x in sort_topics:
        problems[x] = ["Problem 1", "Problem 2","Problem 3"]
        print("* {}".format(x))
        
    print(headings[1])
    for i in problems.keys():
        print("* {} : {}".format(i,(', '.join(map(str, problems[i])))))

    students = [(1, "Tom", "Modules", "Problem 2", "[GRADED]"),
                (2, "Nyari", "Introduction to Python", "Problem 2", "[STARTED]"),
                (3, "Adam", "Modules", "Problem 2", "[COMPLETED]")]

    sorted_students = sorted(students, key = lambda x: x[4], reverse=True)
    print(headings[2])

    for i in sorted_students:
        (nr,name,topic,problem,status) = i
        print("{}. {} - {} - {} {}".format(nr,name,topic,problem,status))

    pass


if __name__ == "__main__":
    create_outline()
