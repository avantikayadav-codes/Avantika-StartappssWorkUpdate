dict={k:k**2 for k in range (1,101) if k>1 and all(k%a!=0 for a in range(2,k))}
print(dict)