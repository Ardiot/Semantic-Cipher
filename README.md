# Semantic-Cipher    
Semantic cypher is a cryptosystem based on sha256.    
The main goal is to change each word for other in a deterministic and secure way.     
![imagen](https://user-images.githubusercontent.com/31859239/213827054-e8cb60c1-49e7-4879-a8fd-2ce1678acb79.png)

First of all we will hash each word from our *ordered dictionary* with a password.    
![imagen](https://user-images.githubusercontent.com/31859239/213827559-c4f37461-0ef8-4280-bea1-49c4236b9678.png)
   

Second, we will sort all these hashes in a list that we we call Sorted_Hash_List     
![imagen](https://user-images.githubusercontent.com/31859239/213777478-b67df721-f356-426c-b708-0145646d893e.png)


Now we are ready to encrypt. The aplication that we will use for encrypt is this : f(dictionary[i])= Sorted_Hash_List[i]
![imagen](https://user-images.githubusercontent.com/31859239/213777927-de6d59b9-65c7-4aa9-97a7-239627b7e0bd.png)


This could be one possible output 
![imagen](https://user-images.githubusercontent.com/31859239/213778075-a39ae12c-0276-4203-a57e-e664cfe02c99.png)
     
     
If you encrypt something with this dictiorany it will be  trivial to decrypt. But instead of using a 8 words dictonary if you use a list of more than 1 M words you will have 1000000! possible permutations for the Sorted_Hash_List and they will change "in a random way" depending on the password you choose. 
For example, using a file with more than 1065200 words and _12345_ as a password, the phrase *I am looking for a job* will be converted to  *bullshitterting torture's corneliaring tubulether defamia immanencyses*

