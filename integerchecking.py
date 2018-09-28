# t ← min{m, n}
# while(t > 0) do
#    if(m mod t = 0 and n mod t = 0)
#        return t
#    t ← t - 1

# function for consecutive integer checking algorithm
def intCheck():
  t = min{m, n}
  while (t > 0) do
    if(m % t == 0 and n % t == 0)
        return t
    t = t - 1

    
    COULD WE USE THE BOTTOM????
    
# function for consecutive integer checking algorithm and getting modulo average
def intCheck(m, n):
  dcount = 0;
  t = min{m, n}
  while (t > 0) do
    if(m % t == 0 and n % t == 0)
      dcount += 2
      return t
    dcount += 1
    t = t - 1
