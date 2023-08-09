person1 = {"name": "John Doe", "age": 38,"skills":['Python','JavaScript','C++']}
skills_required1 = ['Python','JavaScript']
skills_required2 = ['Python','JavaScript',"C#"]
person2 = {"name": "John Doe", "age": 38,"skills":['Python','JavaScript','C++','C#']}
def has_required_skills(person,skills):
    '''
    for skill in person['skills'] :
        if skill in skills:
            print(skill)
    '''
    return all([skill in person['skills']  for skill in skills ])



print(has_required_skills(person2,skills_required2))
