
import sys
import numpy as np
def create_pyramid(n):
    ''' 
    create a pyramid with the length of n
    
    Parameters
    ----------
    n : int
        The lenght of the pyramid
    
    Returns
    -------
    list of the  numbers at the end of each pyramid line.
    '''
    end_numbers=[]
    step=1
    pyramid=[]
    while n>0:
        if n>=step:
            _int=int(step*(step-1)/2) # the start number of each line
            _end=int(step*(step-1)/2+step )# the end number of each line
            _row=list(np.arange(_int,_end))
            # print(_row)
            pyramid.append(_row)
            end_numbers.append(str(_end))
            n-=step
            step+=1
            
        else:
            break
    return(end_numbers)

def decode(message_file):
    """
    Decode a message from a txt file.

    The message file contains a column of integers, and a columns of words

    Parameters
    ----------
    message_file : txt file
        The name of the file containing the message to decode.

    Returns
    -------
    str
        The decoded message.
    """
    digit_words_dict = {}
    message=''
    with open(message_file, 'r') as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        digit_words = line.strip().split()
        if digit_words[0].isdigit() and digit_words[1].isalpha() and len(digit_words)==2:
            digit_words_dict[digit_words[0]]=digit_words[1]

    word_idx=create_pyramid(len(digit_words_dict))
    selected_values = [digit_words_dict[key] for key in word_idx  if key in digit_words_dict]
    return(' '.join(selected_values))
        
def main():
    """ Main function """

    if sys.argv[1] == '-h':
        print("Usage: python decode.py <message_file>")
        sys.exit(0)
    else:
        message_file = sys.argv[1]
        print(decode(message_file))

if __name__ == '__main__':
    main()
