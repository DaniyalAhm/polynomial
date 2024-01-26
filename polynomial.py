import time

class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self,num):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    


            

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):


        #If p1 is an addition operation
        if isinstance(self.p1, Add) or isinstance(self.p1, div) or isinstance(self.p1, Mul) :
            #If p2 is also an addition operation
            if isinstance(self.p2, Add) or isinstance(self.p2, div) or isinstance(self.p2, Mul):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            
            #If only p1 is an add operation
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        
        #If p2 is an addition operation
        if isinstance(self.p2, Add) or  isinstance(self.p2, div) or isinstance(self.p2, Mul):

            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
class div:
    def __init__(self, p1,p2) :
        self.p1 =p1
        self.p2 = p2


    def __repr__(self):

        #If either object is an instance of add or multiply enclose in parethensis
        if isinstance(self.p1, Add) or isinstance(self.p1, Mul) or isinstance(self.p1, div)  :
             if isinstance(self.p2, Add) or isinstance(self.p2, Mul) or isinstance(self.p2, div):
                return "( " + repr(self.p1) + " ) /( " + repr(self.p2) + " )"  
             return "( " + repr(self.p1) + " ) / " + repr(self.p2)

        #if only p2 is a Multiplication opertation or not
        if isinstance(self.p2, Add) or isinstance(self.p2, Mul) or isinstance(self.p2, div):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    



        
def checkifX(can, num):
    if(isinstance(can, X)):
        return num
    return can


'''Explanation: I have modified the mul class, however there are several steps that I took to make the div class, one step one may disagree with 
is checking if the parameters of p1 and p2 are themselves instances of the same class. This is important for the following example'''

test1 = div(Mul(4,3), div(20,4)) # Should print (4*3)/ (20/4)
print(test1)

'''If we had not included checked if the instances of the variables were divs in lines such as 56,57 and 62
then we would have (4*3) /20/4 which is not the same as  (4*3) /(20/4),  The other cases are pretty self explanatory if some varaible is addition or multipication 
Then obviously we need to enclose it in parenthesis. Note I have made the same changes to mul to check for the exact same cases'''

#Some more test cases

test2 = div(div(4,3), div(20,4)) # Should print (4/3)/ (20/4)
print(test2)


test3 = Add(Mul(4,3), div(20,4)) # Should print 4 * 3 + 20 / 4 which is the same as (4*3)+(20/4)
print(test3)



poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)





