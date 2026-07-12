USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_UpdateUser
(
    @UserID INT,
    @Username NVARCHAR(50),
    @Email NVARCHAR(255),
    @Role NVARCHAR(50),
    @IsActive BIT
)
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE dbo.Users
    SET
        Username = @Username,
        Email = @Email,
        Role = @Role,
        IsActive = @IsActive,
        UpdatedAt = GETDATE()
    WHERE
        UserID = @UserID
        AND IsDeleted = 0;

    SELECT @@ROWCOUNT AS AffectedRows;
END;
GO