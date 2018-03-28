• Created a system which can convert a natural English language sentence to a MySQL query.


• The system uses tokenizer, NER tagger and a syntactical parser which helps to form the MySQL with proper syntax.


• First, the systems tokenizes the system then after removing stop words an NER tagged list is created and then the syntactical parser is used to parse through this tagged list to get the information with respect to MySQL syntax i.e. we create another tagged list which tags the word with information list this word is for where clause or for sort clause etc.


• Finally, with this new tagged list, we create a proper MySQL query.
