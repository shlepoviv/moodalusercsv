class MoodelUser():
    def __init__(self,init_data = None) -> None:
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None
        if init_data:
            if isinstance(init_data,dict):
                self._parse_dict(init_data)
            elif isinstance(init_data,str):
                self._parse_line(init_data)

    def _parse_line(self,line:str) -> None:

        split_line = line.split()
        if len(split_line) == 4:
            self.lastname = split_line[0]
            self.firstname = split_line[1]
            self.surname = split_line[2]
            self.email = split_line[3]
            self.username = self.email.lower()
            #self.username = translit(f'{self.lastname}{self.firstname}'.replace('`','').casefold() , language_code='ru', reversed=True)
        elif len(split_line) == 5:
            self.lastname = split_line[0]
            self.firstname = split_line[1]
            self.surname = split_line[2]
            self.email = split_line[4]
            self.username = self.email.lower()
            #self.username = translit(f'{self.lastname}{self.firstname}'.replace('`','').casefold() , language_code='ru', reversed=True)
        else:
            print(f'косяк со строкой: {line}')
    
    def _parse_dict(self,inp:dict) -> None:
        for arg in inp:
            if arg in self.__dict__:
                self.__dict__[arg] = inp[arg]

    def getdict(self,fieldnames:list = None) -> dict:
        res = {}
        if fieldnames:
            for field in fieldnames:
                res[field] = (self.__getattribute__(field))      
        else:
            res = dict(((arg,self.__dict__[arg]) for arg in self.__dict__ if self.__dict__[arg] and not arg.startswith('_')))
        return res
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value,MoodelUser):
            if __value.email == self.email and __value.firstname == self.firstname and __value.lastname == self.lastname:
                return True
            return False
        else:
            raise TypeError(__value)
    
    def __repr__(self) -> str:
        return self.getdict().__repr__()