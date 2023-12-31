class Fraction:
    """Fraction class to help with float imprecision
    !!! Be careful if you put float in an instance, it will round the float !!!
    """
    def __init__(self, num, denom = 1) -> 'Fraction':
        if denom < 0:
            num,denom = -num,-denom         
        if isinstance(num, float): 
            num = round(num)
        if isinstance(denom, float):
            denom = round(denom)
        pgdc = self.get_pgdc(num, denom)
        self.__num = int(num / pgdc)
        self.__denom = int(denom / pgdc)

    def __repr__(self) -> str:
        return f"Fraction({self.__num},{self.__denom})"

    def __str__(self) -> str:
        return f"({self.__num}/{self.__denom})"
    
    def __eq__(self, autre : 'Fraction') -> bool:
        if isinstance(autre, Fraction):
            return self.__num == autre.__num and self.__denom == autre.__denom
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__eq__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")
    
    def __lt__(self, autre: 'Fraction') -> bool:
        if isinstance(autre, Fraction):
            return self.__num * autre.__denom < autre.__num * self.__denom
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__lt__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")
    
    def __gt__(self, autre: 'Fraction') -> bool:
        if isinstance(autre, Fraction):
            return self.__num * autre.__denom > autre.__num * self.__denom
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__gt__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")
    
    def __int__(self) -> int:
        return self.__num // self.__denom
    
    def __float__(self) -> float:
        return self.__num / self.__denom

    def __abs__(self) -> 'Fraction':
        return Fraction(abs(self.__num), abs(self.__denom))

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__denom)
    
    def __add__(self,autre) -> 'Fraction': 
        if isinstance(autre,Fraction):
            return Fraction((self.__num*autre.__denom)+(autre.__num * self.__denom),self.__denom*autre.__denom)
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__add__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")


    def __sub__(self, autre) -> 'Fraction': 
        if isinstance(autre, Fraction):
            return Fraction((self.__num * autre.__denom) - (autre.__num * self.__denom), self.__denom * autre.__denom)
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__sub__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")

    def __mul__(self, autre) -> 'Fraction': 
        if isinstance(autre, Fraction):
            return Fraction(self.__num * autre.__num, self.__denom * autre.__denom)
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__mul__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")

    def __truediv__(self, autre) -> 'Fraction': 
        if isinstance(autre, Fraction):
            return self.__mul__(Fraction(autre.__denom, autre.__num))
        elif isinstance(autre, int) or isinstance(autre, float):
            return self.__truediv__(Fraction(autre))
        else:
            raise TypeError(f"{type(autre)} n'est pas supporté")

    def __pow__(self, autre : int) -> 'Fraction':
        if isinstance(autre, int):
            if autre < 0:
                return Fraction(self.__denom ** abs(autre), self.__num ** abs(autre))
            else:
                return Fraction(self.__num ** autre, self.__denom ** autre)
        else:
            raise TypeError(f"La puissance doit être un entier, pas un {type(autre)}")
    
    @classmethod      
    def get_pgdc(self, num : int, denom : int) -> int:
        if isinstance(num, int) and isinstance(denom, int):
            if num == 0 or denom == 0:
                return num if num > 0 else 1
            if num<0 or denom<0:
                return Fraction.get_pgdc(num = abs(num),denom = abs(denom))
            if denom != 0:
                return Fraction.get_pgdc(num = denom, denom = num % denom)
        raise TypeError("Invalid type for the get_pgdc arguments")

    def to_decimal(self) -> float:
        return self.__num / self.__denom

    def to_string(self) -> str:
        if self.__denom == 1:
            return str(self.__num)
        else:
            return f"{self.__num}/{self.__denom}"

    def invert(self) -> 'Fraction':
        return Fraction(self.__denom,self.__num)
    
    def simplify(self) -> 'Fraction':
        return Fraction(self.__num,self.__denom)
    
    def get_num(self) -> int:
        return self.__num
    
    def get_denom(self) -> int:
        return self.__denom




if __name__ == '__main__':
    frac = Fraction(1,2)
    