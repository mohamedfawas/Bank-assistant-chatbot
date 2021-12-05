create table CustomerDetails 
(AccountNumber int not null , FirstName varchar(255) not null, LastName varchar(255) not null, primary key(AccountNumber));

insert into CustomerDetails (AccountNumber , FirstName, LastName)
values 
(34120, 'David' , 'Warner'),
(34121, 'Steve' , 'Smith'),
(34122, 'Aron' , 'Finch'),
(34123, 'Glenn' , 'Maxwell'),
(34124, 'Mitch' , 'Marsh');

create table Transactions(TransactionsDate date, AccountNumber int, TransactionType varchar(2) , Amount float,
foreign key(AccountNumber) references CustomerDetails(AccountNumber));

insert into Transactions(TransactionsDate, AccountNumber, TransactionType, Amount)
values
('2017-01-01' , 34120 , 'CR' , 1000),
('2017-01-01' , 34121 , 'CR' , 2000),
('2017-01-01' , 34122 , 'CR' , 3000),
('2017-01-01' , 34123 , 'CR' , 4000),
('2017-01-01' , 34124 , 'CR' , 5000);


insert into Transactions(TransactionsDate, AccountNumber, TransactionType, Amount)
values
('2017-01-02' , 34120 , 'CR' , 1000),
('2017-01-03' , 34121 , 'CR' , 2000),
('2017-01-04' , 34122 , 'CR' , 3000),
('2017-01-04' , 34123 , 'CR' , 4000),
('2017-01-02' , 34124 , 'CR' , 5000);

insert into Transactions(TransactionsDate, AccountNumber, TransactionType, Amount)
values
('2017-01-05' , 34120 , 'DB' , 321),
('2017-01-07' , 34121 , 'DB' , 422),
('2017-01-09' , 34122 , 'DB' , 311),
('2017-01-11' , 34123 , 'DB' , 222),
('2017-01-24' , 34124 , 'DB' , 115);

insert into Transactions(TransactionsDate, AccountNumber, TransactionType, Amount)
values
('2017-02-22' , 34120 , 'CR' , 1000),
('2017-02-23' , 34121 , 'CR' , 2000),
('2017-02-14' , 34122 , 'CR' , 3000),
('2017-02-14' , 34123 , 'CR' , 4000),
('2017-02-22' , 34124 , 'CR' , 5000);

insert into Transactions(TransactionsDate, AccountNumber, TransactionType, Amount)
values
('2017-02-05' , 34120 , 'DB' , 321),
('2017-03-07' , 34121 , 'DB' , 422),
('2017-02-09' , 34122 , 'DB' , 311),
('2017-05-11' , 34123 , 'DB' , 222),
('2017-03-24' , 34124 , 'DB' , 115);



