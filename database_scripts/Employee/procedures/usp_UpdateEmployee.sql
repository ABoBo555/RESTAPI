USE [HR_DB]
GO

CREATE OR ALTER PROCEDURE dbo.usp_UpdateEmployee

    @EmployeeID INT,
    @Name NVARCHAR(100),
    @Age INT,
    @Department NVARCHAR(100)

AS
BEGIN

    SET NOCOUNT ON;

    UPDATE dbo.Employee
    SET
        Name = @Name,
        Age = @Age,
        Department = @Department,
        UpdatedAt = SYSUTCDATETIME()
    WHERE EmployeeID = @EmployeeID
      AND IsDeleted = 0;

    SELECT @@ROWCOUNT AS AffectedRows;

END;
GO