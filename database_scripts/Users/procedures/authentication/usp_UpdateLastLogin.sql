USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_UpdateLastLogin
(
    @UserID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Users
    SET
        LastLoginAt = GETDATE()
    WHERE
        UserID = @UserID
        AND IsDeleted = 0;

    SELECT @@ROWCOUNT AS AffectedRows;
END;
GO