# Link: https://t.ly/9XXqe
# TODO: Implement with a quit_word, rather than asking after each input
#       or with a combination of keyboard keys.

def input_name_and_number():
    print('-'*10)
    phonebook = {}
    while True:
        name, number = input('Enter name.\t'), int(input('Enter number\t'))
        phonebook[name] = number
        print("Phone number of %s is %d" % (name, number))
        print('-'*10)
        add_more = input('Do you wish to add more contacts?(y/n)\t')
        print('-'*10)
        if  add_more == 'n':
            print('--Input of contacts complete--')
            print('-'*10)
            break

    print(' ')
    return(phonebook)


if __name__ == '__main__':
    phonebook = input_name_and_number()
    print(phonebook)
