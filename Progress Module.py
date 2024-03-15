
histogram = [0, 0, 0, 0, 0]
list_of_outcome = []
dictionary = {}

def Histogram_display():
    f = open('Text File.txt', 'w')
    for i in range (4):
        histogram[4] += histogram[i]
    print('------------------------------------------------')
    print('Histogram \n')
    print('Progress {:>3}'.format(histogram[0]),  ': ', '*'*histogram[0])
    print('Trailer {:>4}'.format(histogram[1]),   ': ', '*'*histogram[1])
    print('Retriever {:>2}'.format(histogram[2]), ': ', '*'*histogram[2])
    print('Excluded {:>3}'.format(histogram[3]),  ': ', '*'*histogram[3])
    print('Total outcomes :', histogram[4])
    print('------------------------------------------------')
    print('Lists \n')
    for i in range(0, histogram[4]*2, 2):
        print(list_of_outcome[i], ' - ', list_of_outcome[i+1][0], ', ', list_of_outcome[i+1][1], ', ',list_of_outcome[i+1][2])
        for_file = str(list_of_outcome[i]) + ' - ' + str(list_of_outcome[i+1][0]) + ', ' + str(list_of_outcome[i+1][1]) + ', ' + str(list_of_outcome[i+1][2])
        if i != histogram[4]*2 - 2:
            for_file += '\n'
        f.write(for_file)
    f.close()
    print('------------------------------------------------')
    print('Text File \n')
    f = open('Text File.txt', 'r')
    print(f.read())
    print('------------------------------------------------')
    print('Dictionary \n')
    dictionary_without_brackets = '\n'.join(f'{key}: {value}' for key, value in dictionary.items())
    print(dictionary_without_brackets)
    print('------------------------------------------------')
        
def Outcome (credits, idstudent):
    if credits[0] == 120:
        print('Progress')
        histogram[0] += 1
        list_of_outcome.append('Progress')
        dictionary_outcome = 'Progress'
        
    elif credits[0] == 100:
        print('Progress (module trailer)')
        histogram[1] += 1
        list_of_outcome.append('Progress (module trailer)')
        dictionary_outcome = 'Progress (module trailer)'
        
    elif credits[2] >= 80:
        print('Exclude')
        histogram[3] += 1
        list_of_outcome.append('Exclude')
        dictionary_outcome = 'Exclude'
        
    else:
        print('Module Retriever')
        histogram[2] += 1
        list_of_outcome.append('Module Retriever')
        dictionary_outcome = 'Module Retriever'
    list_of_outcome.append(credits)
    dictionary[idstudent] = dictionary_outcome, credits

def main():
    
    access = True
    while access:
        idstudent = input('Please enter a student id: ')
        credits = [0, 0, 0]
        try:
            Pass = int(input('Please enter your PASS credits: '))
            if Pass % 20 != 0 or Pass > 120 or Pass < 0:
                print('Out of range.')
            else:
                Defer = int(input('Please enter your DEFER credits: '))
                if Defer % 20 != 0 or Defer > 120 or Defer < 0:
                    print('Out of range.')
                elif Defer + Pass > 120:
                    print('Incorrect Total.')
                else:
                    Fail = int(input('Please enter your FAIL credits: '))
                    if Fail % 20 != 0 or Fail > 120 or Fail < 0:
                        print('Out of range.')
                    elif Pass + Defer + Fail > 120 or Pass + Defer + Fail < 120:
                        print('Incorrect Total.')
                    else:
                        credits[0] = Pass
                        credits[1] = Defer
                        credits[2] = Fail
                        Outcome(credits, idstudent)
                        while True:
                            option = input('Would you like to enter another set of data? Enter y for yes, q for quit: ')
                            match option:
                                case 'y': break
                                case 'q': 
                                    Histogram_display()
                                    access = False
                                    break
                                case _: print('Invalid input')
        except ValueError:
            print('Integer required.')

main()

# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1911654
# Date: 30/11/2022


























