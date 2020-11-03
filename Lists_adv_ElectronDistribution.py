'''Electron Distribution

You are a mad scientist and you decided to play with electron distribution among atom's shells. You know that basic idea of electron distribution
is that electrons should fill a shell until it's holding the maximum number of electrons.

The rules for electron distribution are as follows:
Maximum number of electrons in a shell is distributed with a rule of 2n^2 (n being position of a shell a.k.a the list index + 1).
For example, maximum number of electrons in 3rd shield is 2*3^2 = 18.
Electrons should fill the lowest level shell first.

If the electrons have completely filled the lowest level shell, the other unoccupied electrons will fill the higher level shell and so on.'''
'''
input : Output
10

[2, 8]

44

[2, 8, 18, 16]'''

atom=[]

electrons = int(input())

i=0


'''
atom.append(2 * (0+1) ** 2)
electrons-=(2 * (0+1) ** 2)
i+=1

atom.append(2 * (1+1) ** 2)
electrons-=(2 * (1+1) ** 2)
i+=1

atom.append(2 * (2+1) ** 2)
electrons-=(2 * (2+1) ** 2)
i+=1'''
while   electrons>0:

    if 2*(i+1)**2> electrons:
        atom.append(electrons)
        electrons=0

    else:
        atom.append(2 * (i + 1) ** 2)
        electrons -= (2 * (i + 1) ** 2)
        i += 1

#print(i)
print(atom)
#print(electrons)

