
class DictKeyException(Exception):
    message = 'Key does not exist in dictionary'



    # def key_not_exists(self):
    #     raise Exception("Key doesn't exist")

class DictClass:
    
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        # if (key in self.data):
        #     return self.data[key]   
        # else:
        #     raise DictException("Key doesn't exist")
        
        try:
            value = self.data[key]
        except KeyError:
            ex = DictKeyException()
            print (ex.message)
            

    def __setitem__(self, key, data):
        self.data[key] = data
        self.__dict__[key] = data

if __name__ == "__main__":
    dic = DictClass()
    # print (dic.__dict__)
    dic['a'] = 5
    print (dic.a)
    # print (dic['abc'], dic['ab'])