-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
-- personId is the primary key (column with unique values) for this table.
-- This table contains information about the ID of some persons and their first and last names.
 

-- Table: Address

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
-- addressId is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the city and state of one person with ID = PersonId.
 

-- Write a solution to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Person table:
-- +----------+----------+-----------+
-- | personId | lastName | firstName |
-- +----------+----------+-----------+
-- | 1        | Wang     | Allen     |
-- | 2        | Alice    | Bob       |
-- +----------+----------+-----------+
-- Address table:
-- +-----------+----------+---------------+------------+
-- | addressId | personId | city          | state      |
-- +-----------+----------+---------------+------------+
-- | 1         | 2        | New York City | New York   |
-- | 2         | 3        | Leetcode      | California |
-- +-----------+----------+---------------+------------+
-- Output: 
-- +-----------+----------+---------------+----------+
-- | firstName | lastName | city          | state    |
-- +-----------+----------+---------------+----------+
-- | Allen     | Wang     | Null          | Null     |
-- | Bob       | Alice    | New York City | New York |
-- +-----------+----------+---------------+----------+
-- Explanation: 
-- There is no address in the address table for the personId = 1 so we return null in their city and state.
-- addressId = 1 contains information about the address of personId = 2.
SELECT firstName , lastName , city , state
FROM Person p
LEFT JOIN Address a
ON p.personId = a.personId
Order by firstName
--Ôn tập về join 
-- JOIN
-- LEFT JOIN : TRẢ VỀ TẤT CẢ CÁC PHẦN TỬ TỪ BẢNG BÊN TRÁI KHỚP VỚI BẢNG BÊN PHẢI , NẾU KHÔNG CÓ TRẢ VỀ NULL
-- RIGHT JOIN : TRẢ VỀ TẤT CẢ CÁC PHẦN TỬ TỪ BẢNG BÊN PHẢI KHỚP VỚI BẢNG BÊN TRÁI , NẾU KHÔNG CÓ TRẢ VỀ NULL 
-- INNER JOIN :TRẢ VỀ CÁC HÀNG CÓ GIÁ TRỊ GIỐNG NHAU TRONG BẢNG
-- SELF JOIN  : TỰ JOIN CHÍNH BẢN THÂN NÓ NHƯNG THÀNH 2 BẢNG 
-- CROSS JOIN : TẠO RA SẢN PHẨM DECARTER CỦA HAI BẢNG , TỨC LÀ KẾT HỢP MỖI HÀNG CỦA BẢNG NÀY VỚI BẢNG KIA 
-- FULL JOIN : TRẢ VỀ TẤT CẢ CÁC CÁC HÀNG CÓ KHỚP TRONG 2 BẢNG NẾU KHÔNG CÓ TRẢ VỀ NULL