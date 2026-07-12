USE HR_DB
GO

CREATE OR ALTER PROCEDURE dbo.usp_GetUserByUsername

    @Username NVARCHAR(50)

AS
BEGIN

    SET NOCOUNT ON;

    SELECT

        UserID,
        Username,
        Email,
        PasswordHash,
        Role,
        IsActive,
        LastLoginAt,
        CreatedAt,
        UpdatedAt

    FROM dbo.Users

    WHERE

        Username = @Username
        AND IsActive = 1;

END;
GO