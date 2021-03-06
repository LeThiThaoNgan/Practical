"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


from prac_06.Programminglanguage import programminglanguage

def main():

    ruby = programminglanguage("Ruby", "Dynamic", True, 1995)
    python = programminglanguage("Python", "Dynamic", True, 1991)
    visual_basic = programminglanguage("Visual Basic", "Static", False, 1991)

    print(ruby)

    programming_list = []
    programming_list.append(ruby)
    programming_list.append(python)
    programming_list.append(visual_basic)

    print("The dynamically typed languages are:")

    """for i in range(len(programming_list)):
        if programming_list[i].is_dynamic() == True:
            print(programming_list[i].field)      
    """
    for program in programming_list:
        if program.is_dynamic() == True:
            print(program.field)


main()