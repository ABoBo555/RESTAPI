USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_DeleteUser
(
    @UserID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Users
    SET
        IsDeleted = 1,
        UpdatedAt = GETDATE()
    WHERE
        UserID = @UserID
        AND IsDeleted = 0;

    SELECT @@ROWCOUNT AS AffectedRows;
END;
GO