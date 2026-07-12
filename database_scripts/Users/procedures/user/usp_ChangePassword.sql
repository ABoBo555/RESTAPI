USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_ChangePassword
(
    @UserID INT,
    @PasswordHash NVARCHAR(255)
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Users
    SET
        PasswordHash = @PasswordHash,
        UpdatedAt = GETDATE()
    WHERE
        UserID = @UserID
        AND IsDeleted = 0;

    SELECT @@ROWCOUNT AS AffectedRows;
END;
GO