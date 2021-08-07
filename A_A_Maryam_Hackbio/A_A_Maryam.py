#!/usr/bin/env python
# coding: utf-8

# In[11]:


name = "Ahmadu Maryam Abdulazeez"
email_address ="abdulazeezmaryam108@gmail.com"
slack_username = "@maryam"
biostack = "genomics"
twitter_handle = "@maryamahmadu108"
hamming_distance = 0



def hammingDist(str1, str2):
    i = 0
    count = 0
 
    while(i < len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
 
# Driver code 
str1 = "@maryam"
str2 = "@maryamahmadu108"
 
# function call
hamming_distance = (hammingDist(str1, str2))

output = name + "," + email_address+ "," + slack_username + "," + biostack + "," + twitter_handle + "," + str(hamming_distance) 
print(output)


file = open('C:/Users/MADEENAH ABDULAZEEZ/Desktop/A_A_Maryam_Hackbio/output.txt', 'w')
file.write(output)
file.close()


# In[ ]:





# In[ ]:




