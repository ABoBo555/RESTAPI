USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_GetUserById
(
    @UserID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        UserID,
        Username,
        Email,
        Role,
        IsActive,
        LastLoginAt,
        CreatedAt,
        UpdatedAt
    FROM dbo.Users
    WHERE
        UserID = @UserID
        AND IsDeleted = 0;
END;
GO