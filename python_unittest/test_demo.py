# -*-coding:UTF-8 -*-
class Testone():
    def number(self,x):
        return x
    def test_result(self):
        assert self.number(3)==3
a=Testone()
result=a.test_result()