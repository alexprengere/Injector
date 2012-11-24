
========
Injector
========

Example
-------

How to use::

 % cat example.pos
 key1   name1   address1phone1
 key2   name_2  address2phone__2

 % head example.pos | inject -i 7 15 23
 key1   ^name1   ^address1^phone1
 key2   ^name_2  ^address2^phone__2

 % head example.pos | inject -i 7 15 23 -n
 key1^name1^addres^s1phone1
 key2^name_2^addres^s2phone__2

 % head example.pos | inject -i 7 15 23 -n | inject -r -i 7 15 23
 key1   name1   address1phone1
 key2   name_2  address2phone__2

