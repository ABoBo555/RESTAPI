USE [HR_DB]
GO

-- get particular emp by id
CREATE OR ALTER PROCEDURE dbo.usp_GetEmployeeById

    @EmployeeID INT

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

    WHERE EmployeeID = @EmployeeID

      AND IsDeleted = 0;

END;
GO


