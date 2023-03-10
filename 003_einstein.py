'''
Lesson: 003
Einstein
03/06/2023
Even if you haven’t studied physics (recently or ever!), you might have heard that
E = mc^2
Where:
    E = Energy (Joules)
    m = Mass (Kilograms)
    c = Speed of Light 300000000 meters per second)
Essentially, the formula means that mass and energy are equivalent.
1. implement a program in Python that
    a. prompts the user for mass as an integer (in kilograms)
    b. outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.
(me: never assume user input)
'''


def convert_mass(mass):
    '''
    Outputs the equivalent number of Joules as an integer.
    E = mc^2
    https://www.wyzant.com/resources/answers/315201/e_mc2_m_3_c_6_solve_for_e
    E = Massinput(c^2)
    '''

    c = 300000000

    energy = mass*(c^2)
    print(energy)
    return energy




if __name__ == '__main__':
    massUserInput = int(input("Enter an integer for Mass (M) " ))
    convert_mass(massUserInput)
