'''This is a short tutorial on Lists and Queues, python generally has in-built methods such as append, pop, etc  for lists.
 Although this is not necessary a new feature, but it is a new feature for me. 
  We are going to be importing the collection fuction and converting a list into a queue. 
  To  create a queues, we use collections.deque which was designed to have fast appends and pops from both ends. '''

from collections import deque
a_queue = deque(['MircoSoft', 'Google' , 'Apple' , 'Meta' , 'Netflix']

a_queue.append('Sony')
a_queue.append('Samsung')