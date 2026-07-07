USE [HR_DB]
GO

-- soft delete emp
CREATE OR ALTER PROCEDURE dbo.usp_DeleteEmployee

    @EmployeeID INT

AS
BEGIN

    SET NOCOUNT ON;

    UPDATE dbo.Employee

    SET

        IsDeleted = 1,

        UpdatedAt = SYSUTCDATETIME()

    WHERE EmployeeID = @EmployeeID;

    SELECT @@ROWCOUNT AS AffectedRows;
    
END;
GO