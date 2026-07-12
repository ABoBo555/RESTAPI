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

    --------------------------------------------------------
    -- Validate Sort Column
    --------------------------------------------------------

    IF @SortBy NOT IN
    (
        'id',
        'name',
        'age',
        'department',
        'createdat',
        'updatedat'
    )
    BEGIN
        SET @SortBy = 'id';
    END

    --------------------------------------------------------
    -- Validate Sort Direction
    --------------------------------------------------------

    SET @SortDirection = LOWER(@SortDirection);

    IF @SortDirection NOT IN ('asc', 'desc')
    BEGIN
        SET @SortDirection = 'asc';
    END

    --------------------------------------------------------
    -- Map API fields to database columns
    --------------------------------------------------------

    DECLARE @SortColumn NVARCHAR(100);

    SET @SortColumn =
        CASE @SortBy
            WHEN 'id' THEN 'EmployeeID'
            WHEN 'name' THEN 'Name'
            WHEN 'age' THEN 'Age'
            WHEN 'department' THEN 'Department'
            WHEN 'createdat' THEN 'CreatedAt'
            WHEN 'updatedat' THEN 'UpdatedAt'
        END;

    --------------------------------------------------------
    -- Build SQL
    --------------------------------------------------------

    DECLARE @SQL NVARCHAR(MAX);

    SET @SQL = N'

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

        AND
        (
            @Search IS NULL
            OR Name LIKE ''%'' + @Search + ''%''
        )

        AND
        (
            @Department IS NULL
            OR Department = @Department
        )

    ORDER BY
        ' + QUOTENAME(@SortColumn) + ' ' + @SortDirection + '

    OFFSET @Offset ROWS

    FETCH NEXT @PageSize ROWS ONLY;
    ';

    EXEC sp_executesql

        @SQL,

        N'
        @Search NVARCHAR(100),
        @Department NVARCHAR(50),
        @Offset INT,
        @PageSize INT
        ',

        @Search,
        @Department,
        @Offset,
        @PageSize;

END;
GO