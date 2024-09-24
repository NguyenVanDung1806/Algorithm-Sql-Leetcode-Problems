-- Table: Employee

-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the salary of an employee.
 

-- Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+
-- Example 2:

-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | null                |
-- +---------------------+
--Solution 1:
select max(salary) as SecondHighestSalary
from Employee
where salary NOT IN (
        select MAX(salary) from Employee)
--solution 2: subquery
# Write your MySQL query statement below
Select(select DISTINCT(salary) 
from Employee
Order by salary DESC 
LIMIT 1 OFFSET 1) as SecondHighestSalary
--Limit 1 offset 1 lay dong dau tien va bo dong do 
--DESC sort lai tu cao xuong thap de ta loai bo dong dau la gia tri max sau do lay gia tri 2
--Distinct lay cac gia tri duy nhat trong salary 