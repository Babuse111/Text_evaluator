# -*- coding: utf-8 -*-
"""function.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D9huydBVUnhP-fXniRa6wiZYxz_w_rtm
"""

def The_function(str):
  myList1 = ['shared', 'email']
  mylist2 = ['share', 'email']

  if all(x in str for x in myList1):
    return 'Student has shared'
  elif all(x in str for x in mylist2 ):
    return 'Student wants to know if can share'
  else:
    return 'the email is not based on shering your email or not'
