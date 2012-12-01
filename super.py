#!/bin/env python
# -*- coding: utf-8 -*-

class Fuck(object):
    def fuck1(self):
        print("Fuck.fuck1")

    def fuck2(self):
        print("Fuck.fuck2")

    def fuck3(self):
        print("Fuck.fuck3")

class Duck(Fuck):
    def fuck1(self):                      # \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u043b\u0438 \u043c\u0435\u0442\u043e\u0434, \u043c\u0435\u0442\u043e\u0434 \u0441 \u0442\u0430\u043a\u0438\u043c \u0436\u0435 \u0438\u043c\u0435\u043d\u0435\u043c \u0435\u0441\u0442\u044c \u0432 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u0435
        print("Duck.fuck1")

    def fuck2(self):                      # \u0442\u043e\u0436\u0435 \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u043b\u0438 \u043c\u0435\u0442\u043e\u0434
        super(Duck, self).fuck2()         # \u0438 \u0432\u044b\u0437\u0432\u0430\u043b\u0438 \u0432 \u043d\u0435\u043c \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439, \u0431\u0435\u0437 super \u043c\u044b \u0431\u044b \u0432\u044b\u0437\u0432\u0430\u043b\u0438 \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434 \u0438\u0437 Duck
        print("Duck.fuck2")

    def duck1(self):
        self.fuck1()                      # \u0432\u044b\u0437\u0432\u0430\u043b\u0438 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u043c\u0435\u0442\u043e\u0434, \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0439, \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u044f super \u0432\u044b\u0437\u0432\u0430\u043b\u0438 \u0431\u044b Fuck.fuck1
        print("Duck.duck1")

    def duck2(self):
        self.fuck3()                      # \u0432\u044b\u0437\u0432\u0430\u043b\u0438 \u0443\u043d\u0430\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u043c\u0435\u0442\u043e\u0434, \u043c\u044b \u0435\u0433\u043e \u0432 \u043f\u043e\u0442\u043e\u043c\u043a\u0435 \u043d\u0435 \u043f\u0435\u0440\u0435\u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u043b\u0438, \u0442\u0430\u043a \u0447\u0442\u043e \u043e\u043d \u043f\u0440\u043e\u0441\u0442\u043e \u043d\u0430\u0441\u043b\u0435\u0434\u0443\u0435\u0442\u0441\u044f
        print("Duck.duck2")

if __name__ == "__main__":
    fuck = Fuck()
    fuck.fuck1()
    fuck.fuck2()
    fuck.fuck3()
    print("=======================")
    duck = Duck()
    duck.fuck1()
    print("=======================")
    duck.fuck2()
    print("=======================")
    duck.duck1()
    print("=======================")
    duck.duck2()


# Fuck.fuck1
# Fuck.fuck2
# Fuck.fuck3
# =======================
# Duck.fuck1
# =======================
# Fuck.fuck2
# Duck.fuck2
# =======================
# Duck.fuck1
# Duck.duck1
# =======================
# Fuck.fuck3
# Duck.duck2
