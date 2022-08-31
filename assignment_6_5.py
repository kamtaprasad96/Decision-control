# Write a python script to print two given words inn dictionary order

print('enter two words:')
a,b=input(),input()
print((a,b) if a>b else (b,a))