Algorithm for file updates in Python
Project description
[The aim of this algorithm is to automate the process of updating an “allow list” of IP addresses.]
Open the file that contains the allow list
#assign  ‘import_file’ to the name of the file.
Import_file = “allow_list.txt”

#assign “remove_list” to a list of ip addresses that are no longer allowed to access the file
Remove_list = [‘192.168.225”, “192.168.158.170”, 192.168.201.40”, “192.168.58.57”]

#open file in read mode (“r”) with open(import_file, “r”) as file:
Read the file contents
With open(import_file, “r”) as file:
#read the file contents and store them in “ip_addresses”
       Ip_addresses = file.read()
#Display the string
print(ip_addresses)
Convert the string into a list
#convert the string into a list of individual strings
Ip_addresses = ip_addresses.split()

#display the list format
print(ip_addresses)
Iterate through the remove list
#iterate through the remove_list
for element in remove_list:
#check if the ip address is in the allow_list
Remove IP addresses that are on the remove list
If element in ip_addresses:
   #remove the ip address from the allow list
         ip_address.remove(element)
print(ip_addresses removed successfully.)
Update the file with the revised list of IP addresses 
#convert the list back to a string
Ip_addresses_string = “\n”.join(ip_addresses)
Summary
The aim of this python algorithm was to automate the removal of unauthorized ip addresses from restricted access file.  The process began by using the open() function with keyword to access the “allow_list.txt” file in read mode. I then used the .read() method to convert the file’s contents into a string, the applied the .split() method to transform that string into a list of individual ip addresses for easier processing. To update the list, I implemented the a for loop to iterate through a secondary list of ip addresses that needed to be removed . Within this loo[p, I used a conditional if statement to check for the presence of each ip, and applied the .remove() method to delete it from the primary list. 
Finally, I converted the updated list back into a string using the .join() method and used the open() function with the “w” argument to overwrite the original file with the new, secured allow list.
