#!/usr/bin/env python

from complex import Complex

def test_add_one():
    assert Complex(10, 5) + Complex(2, 2) == Complex(12, 7)

def test_add_two():
    assert Complex(0, 5) + Complex(3, 0) == Complex(3, 5)

def test_add_three():
    assert Complex(0, 0) + Complex(0, 0) == Complex(0, 0)

def test_sub_one():
    assert Complex(10, 10) - Complex(2, 8) == Complex(8, 2)

def test_sub_two():
    assert Complex(0, 3) - Complex(10, 10) == Complex(-10, -7)

def test_sub_three():
    assert Complex(0, 0) - Complex(0, 0) == Complex(0, 0)

def test_mul_one():
    assert Complex(2, 2) * Complex(3, 3) == Complex(0, 12)

def test_mul_two():
    assert Complex(5, -4) * Complex(0, 0) == Complex(0, 0)

def test_mul_three():
    assert Complex(5, -4) * Complex(-3, 2) == Complex(-7, 22)

def test_mul_four():
    assert 4 * Complex(1,1) == Complex(4,4)

def test_conj_one():
    assert Complex(0, 0).conjugate() == Complex(0, 0)

def test_conj_two():
    assert Complex(2, 5).conjugate() == Complex(2, -5)

def test_conj_three():
    assert Complex(0, -3).conjugate() == Complex(0, 3)

def test_mod_one():
    assert Complex(2, 2).modulus() == 2.8284271247461903

def test_mod_two():
    assert Complex(0, 0).modulus() == 0.0

def test_mod_three():
    assert Complex(-5, 3).modulus() == 5.830951894845301

def test_eq_one():
    assert Complex(0, 1) == Complex(0, 1)

def test_eq_two():
    assert Complex(-1, 0) == Complex(-1, 0)

def test_eq_three():
    assert Complex(0, 0) == Complex(0, 0)

def test_py_complex_one():
    assert Complex(2,3) + (2+2j) == Complex(4,5)

def test_py_complex_two():
    assert 4*Complex(3,4) - 2 == Complex(10,16)
