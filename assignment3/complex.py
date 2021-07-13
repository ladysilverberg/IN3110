#!/usr/bin/env python

import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if (self.real == 0):
            return "(%+di))" % (self.imag)
        else:
            return "(%d%+di)" % (self.real, self.imag)

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def modulus(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return Complex(real, imag)

    def __eq__(self, other):
        if (self.real == other.real and self.imag == other.imag):
            return True
        return False

    def __radd__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __rsub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __rmul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return Complex(real, imag)

    def __complex__(self):
        return complex(self.real, self.imag)
