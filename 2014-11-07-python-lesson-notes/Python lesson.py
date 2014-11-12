
# coding: utf-8

# # header1
# cool stuff
# ## header2

# In[1]:

import numpy


# In[2]:

numpy.loadtxt('inflammation-01.csv', delimiter=',')


# In[3]:

my_variable = 20


# In[4]:

print my_variable
# PEP 8


# In[5]:

my_variable


# In[6]:

inflam = numpy.loadtxt('inflammation-01.csv', delimiter=',')


# In[7]:

inflam


# In[8]:

my_variable = 20
my_variable = my_variable + 3
print my_variable


# In[9]:

type(3)


# In[10]:

type(4.5)


# In[11]:

type(inflam)


# In[12]:

inflam.shape


# In[13]:

inflam


# In[14]:

# slicing
inflam[0, 0]


# In[15]:

inflam[0, 2]


# In[16]:

print('thing in the 0th row and 2nd column: ', inflam[0, 2])


# In[17]:

inflam[30, 19]


# In[18]:

inflam[0:4, ]


# In[19]:

inflam[0:10:3, 0:10]


# In[20]:

first_row = inflam[0, ]


# In[21]:

first_row.shape


# In[22]:

type(first_row)


# In[23]:

first_row.mean()


# In[24]:

first_row.max()


# In[25]:

first_row


# In[26]:

first_row * 2


# In[27]:

first_row


# In[28]:

double = first_row * 2


# In[29]:

first_row


# In[30]:

double


# In[31]:

first_row + double


# In[32]:

first_row.std()


# In[33]:

inflam.mean()


# In[34]:

inflam.shape


# In[35]:

inflam.mean(axis = 0)


# In[36]:

inflam.min(axis = 1)


# In[37]:

inflam.max(axis = 1)


# In[38]:

inflam.std(axis = 1)


# element = 'oxygen'
# give me the first 2 letters of oxygen
# give me the middle 2 litters of oxygen

# In[39]:

element = 'oxygen'
first_2_letters = element[0:2]
first_2_letters


# In[40]:

middle_2_letters = element[2:4]
middle_2_letters


# In[41]:

# example of slicing
inflam[1:2,]


# In[42]:

# extra: how would you get 'gen' without specifying all indicies
element[:3]


# In[43]:

get_ipython().magic(u'matplotlib inline')


# In[44]:

import matplotlib.pyplot as plt


# In[45]:

plt.imshow(inflam)


# In[46]:

inflam.mean(axis=0)


# In[47]:

# average inflammation for each time
plt.plot(inflam.mean(axis=0))


# In[48]:

print 'max inflammation per time'
plt.plot(inflam.max(axis = 0))
plt.show()

print 'min inflammation per time'
plt.plot(inflam.min(axis = 0))
plt.show()

print 'mean inflammation per time'
plt.plot(inflam.mean(axis = 0))
plt.show()


# In[49]:

# create a plot for standard deviation of inflammtion by time
print 'max inflammation per time'
plt.plot(inflam.std(axis = 0))
plt.show()

# and person
print 'max inflammation per person'
plt.plot(inflam.std(axis = 1))
plt.show()



# In[50]:

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("inflammation-02.csv",delimiter=',')


# In[51]:

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("inflammation-02.csv",delimiter=',')
plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.ylabel('mean')
plt.plot(data.mean(axis=0))


plt.subplot(1, 3, 2)
plt.ylabel('std')
plt.plot(data.std(axis=0))


plt.subplot(1, 3, 3)
plt.ylabel('max')
plt.plot(data.max(axis=0))


# In[52]:

# instead of 1 row 3 cols,
# 3 rows, 1 col

plt.figure(figsize=(3, 10))

plt.subplot(3, 1, 1)
plt.ylabel('mean')
plt.plot(data.mean(axis=0))


plt.subplot(3, 1, 2)
plt.ylabel('std')
plt.plot(data.std(axis=0))


plt.subplot(3, 1, 3)
plt.ylabel('max')
plt.plot(data.max(axis=0))


# In[53]:

# http://matplotlib.org/mpl_examples/api/radar_chart.py


# # functions

# In[54]:

def fahr_to_kelvin(fahr_num_to_convert):
    converted = (fahr_num_to_convert - 32) * (5 / 9.0) + 273.15
    return converted


# In[55]:

temp = 32
temp - 32


# In[56]:

(5/9.0)


# In[57]:

type(9.0)


# In[58]:

fahr_to_kelvin(32)


# In[59]:

fahr_to_kelvin(212)


# In[60]:

assert fahr_to_kelvin(32) == 273.15


# In[61]:

assert fahr_to_kelvin(212) == 373.15


# # more functions and why we use them

# In[62]:

def fahr_to_kelvin(fahr_num_to_convert):
    converted = (fahr_num_to_convert - 32) * (5 / 9.0) + const()
    return converted


# In[63]:

def fahr_to_cel(degree):
    converted = fahr_to_kelvin(degree) - const()
    return converted


# In[64]:

def const():
    return 273.15


# In[65]:

fahr_to_kelvin(212)


# In[66]:

number = '3'


# In[67]:

type(float(number))


# In[68]:

convert = 'hello'
fahr_to_kelvin(212)
print(convert)


# In[69]:

import numpy as np
import matplotlib.pyplot as plt

def plot_me(fname):
    '''this is a function that takes a csv that plots the mean, std,
    and max values
    
    parameters
    ----------
    fname = string that repsesnts the file name to plot
    '''
    
    # loat in csv
    data = np.loadtxt(fname, delimiter=',')
        
    # set dims
    plt.figure(figsize=(10, 3))

    # plot 1
    plt.subplot(1, 3, 1)
    plt.ylabel('mean')
    plt.plot(data.mean(axis=0))


    plt.subplot(1, 3, 2)
    plt.ylabel('std')
    plt.plot(data.std(axis=0))


    plt.subplot(1, 3, 3)
    plt.ylabel('max')
    plt.plot(data.max(axis=0))


# In[70]:

plot_me('inflammation-01.csv')
plot_me('inflammation-02.csv')
plot_me('inflammation-03.csv')
plot_me('inflammation-04.csv')
plot_me('inflammation-05.csv')


# In[71]:

ls


# In[72]:

get_ipython().magic(u'pinfo plot_me')


# In[73]:

my_list = []
my_tuples = ()
my_dict = {}


# In[74]:

my_list = [1, 2, 3, 4]
my_list


# In[75]:

# iterators
for thing in my_list:
    print(fahr_to_kelvin(thing))


# In[76]:

ls


# In[77]:

import glob


# 

# In[78]:

list_of_files = glob.glob('i*.csv')


# In[79]:

list_of_files


# In[80]:

# iterators
for inflam_file in list_of_files:
    plot_me(inflam_file)


# In[81]:

list_of_files = glob.glob('i*.csv')
for inflam_file in list_of_files:
    plot_me(inflam_file)


# In[82]:

for inflam_file in glob.glob('i*.csv'):
    plot_me(inflam_file)


# In[83]:

list_of_files.sort()


# In[84]:

list_of_files


# In[85]:

list_of_files.append('junk')


# In[86]:

list_of_files


# In[87]:

for file_name in list_of_files:
    plot_me(file_name)


# In[88]:

list_of_files = glob.glob("i*.csv")
list_of_files.append("junk")
list_of_files


# In[89]:

num = 37

if num > 40:
    print "you are greater than 40"
if num <= 40:
    print "you are less than 40"
    print "YAY!!!!!"


# In[90]:

num = 37

if num > 40:
    print "you are greater than 40"
elif num < 39:
    print "you are less than 39"
else:
    print "you are less than 40"
    print "YAY!!!!!"


# In[91]:

# in python 3, range returns a generator
for number in range(10):
    if number == 3:
        continue
    elif number == 5:
       break 
    else:
        print number


# In[92]:

# making decisions
for filename in list_of_files:
    if not filename.endswith('csv'):
        continue
    else:
        plot_me(filename)


# In[ ]:



