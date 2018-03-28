• Created a system which can convert a natural English language sentence to a MySQL query.


• The system uses tokenizer, NER tagger and a syntactical parser which helps to form the MySQL with proper syntax.


• First, the systems tokenizes the system then after removing stop words an NER tagged list is created and then the syntactical parser is used to parse through this tagged list to get the information with respect to MySQL syntax i.e. we create another tagged list which tags the word with information list this word is for where clause or for sort clause etc.


• Finally, with this new tagged list, we create a proper MySQL query.


The corpus that can be used to test our system is not readily available and is dependent on a database. Hence, we have tested our system on a synthesized corpus of natural language statements related to a bank and a university database. The university and bank database consists of 11 and  6 tables respectively. However, system can work on any complex database. The natural language statement has to be a single sentence. The system has been evaluated on a corpus of around 75 natural language statements of university database and around 50 related to bank database. The accuracy of the system is found out to be around 86%. The system gives the same SQL query as the output when the same natural language statement is represented in different ways. If the system fails to generate SQL query corresponding to any natural language statement, an error message is displayed. These are a few results given by the system on the university corpus:


INPUT : 

1.  list all student
2.  list all employee whoes postal = 425001
3.  list employee having name Venus
4.  list 5 employee 
5.  list employe sort alphabetically
6.  count employee whoes birthyear = 1992
7.  what is average salary of employee
8.  highest salary of employee
9.  find employee with brithyear between 1992 and 1994
10. list all employee whoes postal = 425001 and birthyear = 1992
11. list 5 employee whoes postal = 425001 arrange alphabetically
12. find the id and profname where id = 1 from class
13. delete employee whoes birthyear is 1992
14. update employee set country = India whose birthyear = 1992

OUTPUT:

1.  SELECT * FROM student ;
2.  SELECT * FROM employee WHERE employee.postal = '425001' ;
3.  SELECT * FROM employee WHERE employee.name = 'Venus' ;
4.  SELECT * FROM employee LIMIT 5 ;
5.  SELECT DISTINC FROM employee ORDER BY ASC ;
6.  SELECT COUNT( * ) FROM employee WHERE employee.birthyear = '1992' ;
7.  SELECT AVG( DISTINCT employee.salary ) FROM employee ;
8.  SELECT MAX( DISTINCT employee.salary ) FROM employee ;
9.  SELECT * FROM employee WHERE ( employee.birthyear BETWEEN '1992' AND '1994' )  ;
10. SELECT * FROM employee WHERE employee.postal = '425001' AND employee.birthyear = '1992' ;
11. SELECT DISTINC FROM employee WHERE employee.postal = '425001' ORDER BY ASC LIMIT 5 ;
12. SELECT DISTINCT employee.id, student.ID, class.profname FROM student INNER JOIN class ON student.ID = class.studentid WHERE student.ID = '1' ;
13. DELETE FROM employee WHERE employee.birthyear = '1992' ;
14. UPDATE employee SET employee.country = India WHERE employee.birthyear = '1992' ;

