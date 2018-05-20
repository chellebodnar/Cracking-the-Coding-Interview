# 1.1 
"""Implement an algorithm to determine if a string has all unique characters."""
# Let n be the length of the string.
# O(n) time, O(n) space
def isUnique(myString):
	seen = set(); #Will store distinct characters seen so far
	for c in myString:
		if c in seen:
			return False
		seen.add(c)
	return True

# 1.2
"""Given two strings, write a method to decide if one is a permutation of the other."""
# Let n be the length of the strings
# O(n) time, O(n) space
def checkPermutation(s1, s2):
	if len(s1) != len(s2):
		return "Not permutations"
	d = {}
	for c in s1:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	for c in s2:
		if c not in d:
			return "Not permutations"
		else:
			d[c] -= 1
			if d[c] < 0:
				return "Not permutations"
	return "Permutations"


#print checkPermutation("Hello World", "Wrldo llohe")

# 1.3
"""Write a method to replace all spaces in a string with "%20".  """
# Let m be the true length
# O(m) time, O(m) additional space since strings in python are immutable so we need to turn it into a list... 
def URLify(myString, trueLength):
	s = list(myString)
	numSpaces = 0
	for i in range(trueLength):
		if s[i] == " ":
			numSpaces += 1
	j = trueLength + 2*numSpaces - 1
	i = trueLength - 1
	while i >= 0:
		if s[i] == " ":
			s[j] = "0"
			s[j-1] = "2"
			s[j-2] = "%"
			j = j - 3
			i = i - 1
		else:
			s[j] = s[i]
			i = i - 1
			j = j - 1
	output = "".join(s)
	return output

print URLify("Hey you there    ", 13)

# 1.4
"""Given a string, write a function to check if it is a permutation of a palindrome."""
# Let n be the length of s
# O(n) time, O(n) space
def palindromePermutation(s):
	d = {}
	for c in s:
		if c in d:
			d[c] += 1
		else:
			d[c] = 1
	numOdds = 0;
	for key in d:
		if d[key]%2 == 1:
			numOdds += 1
			if numOdds > 1:
				return False
	return True

"""print palindromePermutation("aabbc")
print palindromePermutation("abab")
print palindromePermutation("acb")"""

# 1.5
"""There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check
if they are at most one edit away from each other."""
# Let n be the length of one of the strings
# O(n) time, O(1) space
def oneAway(s1, s2):
	numEdits = 0;
	i = 0
	j = 0
	if abs(len(s1) - len(s2)) > 1:
		return "Nope!"
	if len(s1) == len(s2):
		for t in range(len(s1)):
			if(s1[t] != s2[t]):
				numEdits+=1
				if(numEdits > 1):
					return "Nope!"
		return "At most one edit!"
	if len(s1) > len (s2):
		s1,s2 = s2,s1 #makes sure s2 is the longer string
	while numEdits < 2 and i < len(s1):
		if(s1[i] != s2[j]):
			if numEdits > 0:
				return "Nope!"
			if s1[i] == s2[j + 1]: #inserted into s2  abc, abwc
				numEdits+=1
				j+=1
			else:
				return "Nope!"
		else:
			i+=1
			j+=1
	
	if numEdits > 1:
		return "Nope!"
	
	return "At most one edit!"


print oneAway("abc", "aebc") #yes
print oneAway("abc", "cbc") #yes
print oneAway("abc", "ac") #yes
print oneAway("abc", "bac") #no
print oneAway("abc", "bbd") #no
print oneAway("abc", "abcd") #yes
print oneAway("abc", "adbcd") #no

# 1.6
"""Implement a method to perform basic string compression using the counts of repeated characters.
For example, "aabcccccaaa" would become "a2b1c5a3". Only compress if it actually reduces length."""
# Let n be the length of the input string and m be the length of the compressed string
# O(n) time, O(m) space 
def stringCompression(myString):
	s = ""
	i = 0
	while i < len(myString):
		numCurChar = 1
		while i < len(myString) - 1 and myString[i] == myString[i+1]:
			numCurChar += 1
			i += 1
		s = s + myString[i]
		s = s + str(numCurChar)
		i += 1  
	if len(s) < len(myString):
		print s
	else:
		print myString

stringCompression("aabcccccaaa")
stringCompression("abcdd")

#1.7
"""Given an NxN matrix, rotate it by 90 degrees.  Do it in place."""
# O(N^2) time, O(1) space
def rotateMatrix(matrix):
	#First we transpose, then we swap columns.
	n = len(matrix)
	for i in range(n-1):
		for j in range(i+1, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	for col in range(n/2):
		for row in range(n):
			matrix[row][col], matrix[row][n-1-col] = matrix[row][n-1-col], matrix[row][col]
	print matrix

myMatrix = [[1,2,3], [4,5,6], [7,8,9]]
print myMatrix
rotateMatrix(myMatrix)

# 1.8
"""Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0"""
# O(MN) time, O(M + N) space
def zeroMatrix(matrix):
	rows = set()
	cols = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				rows.add(i)
				cols.add(j)
	for r in rows:
		for i in range(len(matrix[0])):
			matrix[r][i] = 0
	for c in cols:
		for i in range(len(matrix)):
			matrix[i][c] = 0
	print matrix
	
zeroTest = [[1,2,3], [4,0,6], [7,8,9]]		
zeroMatrix(zeroTest)	

# 1.9
"""Assume isSubstring checks if one word is a substring of another.  Give two strings s1 and s2, write code to check
if s2 is a rotation of s1 using only one call to isSubstring."""
# Let n be the length of the input strings and T(n) be the time complexity of isSubstring and S(n) be the required space
# O(T(n)) time and O(S(n)) space
def stringRotation(s1, s2):
	if len(s1) == len(s2):
		return isSubstring(s1, s2 + s2)
	else:
		return False

def isSubstring(s1, s2): #returns true if s1 is a substring of s2
	return s2.find(s1) >= 0

print stringRotation("abcd", "cdab")
print stringRotation("abcd", "acdb")


def flatten(root):
	if root.left:
		L = flatten(root.left)
		root.left = L[0]
		L[0].right = root
	else:
		L = [root, root]
	if root.right:
		R = flatten(root.right)
		root.right = R[1]
		R[1].left = root
	else:
		R = [root, root]
	result = [R[0], L[1]]
	return result

class BiNode:
	def __init__(self, left=None, right=None, data=None):
		self.left = left
		self.right = right
		self.data = data


