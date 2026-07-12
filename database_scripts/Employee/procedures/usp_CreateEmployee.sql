-- create emp
CREATE OR ALTER PROCEDURE dbo.usp_CreateEmployee

    @Name NVARCHAR(100),

    @Age INT,

    @Department NVARCHAR(100)

AS
BEGIN

    SET NOCOUNT ON;

    INSERT INTO dbo.Employee
    (
        Name,
        Age,
        Department
    )
    VALUES
    (
        @Name,
        @Age,
        @Department
    );

    SELECT
        SCOPE_IDENTITY() AS EmployeeID;

END;
GO

