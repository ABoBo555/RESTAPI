USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_GetUserCredentials
(
    @UserID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        UserID,
        PasswordHash
    FROM dbo.Users
    WHERE
        UserID = @UserID
        AND IsDeleted = 0
        AND IsActive = 1;
END;
GO