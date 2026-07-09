USE [HR_DB]
GO

CREATE OR ALTER PROCEDURE dbo.usp_GetEmployees

    @Page INT = 1,
    @PageSize INT = 10,
    @Search NVARCHAR(100) = NULL,
    @Department NVARCHAR(50) = NULL,
    @SortBy NVARCHAR(50) = 'id',
    @SortDirection NVARCHAR(4) = 'asc'

AS
BEGIN

    SET NOCOUNT ON;

    DECLARE @Offset INT =
        (@Page - 1) * @PageSize;

    SELECT

        EmployeeID,
        Name,
        Age,
        Department,
        CreatedAt,
        UpdatedAt

    FROM dbo.Employee

    WHERE
        IsDeleted = 0

    ORDER BY
        EmployeeID

    OFFSET @Offset ROWS

    FETCH NEXT @PageSize ROWS ONLY;

END;
GO