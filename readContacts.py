#import pandas as pd
import difflib as di
import pickle

# data = pd.read_csv('contacts.csv')
# contacts = data['Name']
# contacts = contacts.dropna()
# contacts = list(contacts)
#
# open_file = open("contacts.pkl", "wb")
# pickle.dump(contacts, open_file)
import sys

open_file = open("contacts.pkl", "rb")
contacts = pickle.load(open_file)

def matcher(name):
    resul = di.get_close_matches(name, contacts)
    return resul

if __name__ == '__main__':
    # name = sys.argv[1]
    matcher('Fran')
