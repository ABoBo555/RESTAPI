USE [HR_DB]
GO

-- get all emp
CREATE OR ALTER PROCEDURE dbo.usp_GetEmployees
AS
BEGIN

    SET NOCOUNT ON;

    SELECT

        EmployeeID,

        Name,

        Age,

        Department,

        CreatedAt,

        UpdatedAt

    FROM dbo.Employee

    WHERE IsDeleted = 0

    ORDER BY EmployeeID;

END;
GO
