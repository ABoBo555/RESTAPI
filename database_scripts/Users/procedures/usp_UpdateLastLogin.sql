USE HR_DB
GO

CREATE OR ALTER PROCEDURE dbo.usp_UpdateLastLogin

    @UserID INT

AS
BEGIN

    SET NOCOUNT ON;

    UPDATE dbo.Users

    SET
        LastLoginAt = SYSDATETIME(),
        UpdatedAt = SYSDATETIME()

    WHERE

        UserID = @UserID
        AND IsActive = 1;

    SELECT @@ROWCOUNT AS AffectedRows;

END;
GO