messageA = "One of Python's strengths is its diverse community."
print(messageA)
# purposely done wrong to display wrong quotation use:
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# 2-3. Personal Message: Use a variable to represent a person’s name, and print  a message to that person. Your message should be simple, such as, “Hello Eric,  would you like to learn some Python today?” 
name = "Tommy"
print(name +  " you ignorant slut");
# 2-4. Name Cases: Use a variable to represent a person’s name, and then print  that person’s name in lowercase, uppercase, and title case. 
print(name.upper())
print(name.title())
print(name.lower())
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the  quote and the name of its author. Your output should look something like the  following, including the quotation marks: 
# Albert Einstein once said, “A person who never made a  
# mistake never tried anything new.” 
quote = "If you're not first, you're last"
author = "Ricky Bobby"
print(author + " once said, " + '"' + quote + '"') #oh hey first try fuck yeah
# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the  
# famous person’s name using a variable called famous_person. Then compose  your message and represent it with a new variable called message. Print your  message. 
#nailed it on 2-5 already. 
famous_person = "Michael Myers"
message = " ... "
print(message + "-" + famous_person)
# 2-7. Stripping Names: Use a variable to represent a person’s name, and include  some whitespace characters at the beginning and end of the name. Make sure  you use each character combination, "\t" and "\n", at least once. 
# Print the name once, so the whitespace around the name is displayed.  
# Then print the name using each of the three stripping functions, lstrip(),  
# rstrip(), and strip().
new_name = "  Korbin Dallas \n\t"
print(new_name)
print(new_name.strip())
print(new_name.lstrip())
print(new_name.rstrip())