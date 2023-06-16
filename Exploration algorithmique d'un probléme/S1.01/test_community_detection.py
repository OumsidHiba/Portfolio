#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_create_network():
    assert create_network(couple) == {'Alice': ['Bob', 'Charlie', 'Denis'],
                                  'Bob': ['Alice', 'Denis', 'lala'], 'Charlie': ['Alice'],
                                  'Denis': ['Bob', 'Alice'], 'lala': ['Bob']}
    assert create_network ([]) == {}
    print('ok')


def test_get_people():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'lala'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'lala': ['Bob']}
    assert get_people(d) == ['Alice' , 'Bob' , 'Charlie', 'Denis' ,'']
    assert get_people({'Charlie':[]}) == ['Charlie']
    print('ok')

def test_are_friends():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis', 'nono'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice'], 'nono': ['Bob']}
    assert are_friends(d,'nono','Bob') == True
    assert are_friends(d,'Alice','Charlie') == True
    assert are_friends(d,'nono','Denis') == False
    print("ok")

def test_all_his_friends():

    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice']}
    assert all_his_friends(d,'Charlie',['Bob','nono']) == False
    assert all_his_friends(d,'Bob',['Alice']) == True
    print('ok')

def test_is_a_community():
    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice']}
    assert is_a_community(d,['Alice','Bob','Denis']) == True
    assert is_a_community(d,['Alice','Bob','nono']) == False
    print('ok')

def test_find_community():

    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice']}
    assert find_community(d,['Denis','Bob','Alice']) == ['Denis', 'Bob', 'Alice']
    assert find_community(d,['Alice','Bob','Charlie']) == ['Alice', 'Charlie']
    print('ok')


question 8
def test_order_by_decreasing_popularity():

    d={'Alice': ['Bob', 'Charlie', 'Denis'], 'Bob': ['Alice', 'Denis'],
       'Charlie': ['Alice'], 'Denis': ['Bob', 'Alice']}
    assert order_by_decreasing_popularity(d,['Bob','Alice','Charlie']) == ['Alice', 'Bob', 'Charlie']
    assert order_by_decreasing_popularity(d,['Denis','Alice','Charlie']) == ['Alice', 'Denis', 'Charlie']
    print('ok')


def test_find_community_by_decreasing_popularity():

    d={
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Charlie", "Dominique"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Alice", "Bob"]
}
  
    assert find_community_by_decreasing_popularity(d)  == ['bob','charlie','dominique']
    

def  test_find_community_from_person():
    assert find_community_from_person(

