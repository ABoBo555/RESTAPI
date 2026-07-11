USE [HR_DB]
GO

CREATE OR ALTER PROCEDURE dbo.usp_GetEmployeeCount

    @Search NVARCHAR(100) = NULL,
    @Department NVARCHAR(50) = NULL

AS
BEGIN

    SET NOCOUNT ON;

    SELECT
        COUNT(*) AS TotalRecords
    FROM dbo.Employee
    WHERE
        IsDeleted = 0
        AND (
            @Search IS NULL
            OR Name LIKE '%' + @Search + '%'
        )
        AND (
            @Department IS NULL
            OR Department = @Department
        );

END;
GO


