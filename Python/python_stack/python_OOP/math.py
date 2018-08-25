class MathDojo(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def add(self, *num):

        for char in num:
            if isinstance(char, int):
                self.result += char
            elif isinstance(char, list):
                for elements in char:
                    self.result += elements
            elif isinstance(char, tuple):
                for t_elements in char:
                    self.result += t_elements
        return self

    def subtract(self, *num):
        temp = 0
        for char in num:
            if isinstance(char, int):
                temp += char
            elif isinstance(char, tuple):
                for t_element in char:
                    temp += t_element
            elif isinstance(char, list):
                for elements in char:
                    temp += elements
        self.result -= temp
        return self

    def results(self):
        print self.result


md = MathDojo()

md.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, (2,3), [1.1,2.3]).results()