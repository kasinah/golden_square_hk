
class IncludesTodo:

    def __init__(self, input_list):
        self.input_list = input_list
        
    def check_ContainString_todo(self): 
        if type(self.input_list) is str:
            if "#TODO" in self.input_list: 
                return True 
            elif self.input_list == "":
                return "empty list"
            else:
                return False
        
        else:
            return "That was not a valid string!"
           
  
