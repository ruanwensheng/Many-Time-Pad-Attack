from logger import logging
import json
import string 
import collections
logging.info('load inputs')

with open("inputs/inputs.json") as f:
    inputs = json.load(f)
with open("inputs/test.json") as t:
    test = json.load(t)

logging.info(f'successfully loaded {inputs},{test}')

def xor(a,b):
    return bytes([x ^ y for (x, y) in zip(a, b)])

class ManyTimePad:

    def __init__(self, inputs, test):
        self.inputs = [inputs[f'h{i}'] for i in range(1,11)]
        self.test = [test['h11']]
        self.inputs_bytes = [bytes.fromhex(c) for c in self.inputs]
        self.test_bytes = bytes.fromhex(self.test[0])

        self.final_key = [None]*150
        self.known_key = set()

    def XorOneWith0Others(self, ci_index, ci, counter):
        # ci with ci_index being the chosen one to xor with 9 others
        # counter is a collection.Counter object to count the number of valid char


        for i, ci_other in enumerate(self.inputs_bytes):
            if ci_index !=i:
                xored = xor(ci,ci_other)

                for id, char in enumerate(xored):
                    if chr(char) in string.printable and chr(char).isalpha():
                        counter[id]+=1

                    
    def XorEachOther(self):
        counter = collections.Counter()

        for id, ci in enumerate(self.inputs_bytes):
            counter = collections.Counter()

            self.XorOneWith0Others(id,ci,counter)

            space_ids = []

            for i, val in counter.items():
                if val>=7:
                    space_ids.append(i)

            xor_with_spaces = xor(ci, b' ' * 150)

            # save the key

            for index in space_ids:
                if index < len(xor_with_spaces):
                
                    self.final_key[index] = xor_with_spaces[index]
                    self.known_key.add(index)       

    def ConstructKey(self):
        final_key_bytes = bytes([val if val is not None else 0x00 for val in self.final_key])
        return final_key_bytes
    
    def Test(self):

        res =  xor(self.test_bytes, self.ConstructKey())

        return ''.join([chr(char) if i in self.known_key else '.' for i, char in enumerate(res)])
    

if __name__ ==  "__main__":
    obj = ManyTimePad(inputs, test)
    obj.XorEachOther()
    logging.info(f'{obj.Test()}')
    

                                      



