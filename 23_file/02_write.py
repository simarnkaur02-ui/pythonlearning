# Write to a file called John Doe.txt
# It should contain data about John Doe.

f = open("John Doe.txt", "w")

string = '''
John Doe is a nice guy. he lives in NYC and he works with python his favorite package is Pandas
'''

f.write(string)

f. close()