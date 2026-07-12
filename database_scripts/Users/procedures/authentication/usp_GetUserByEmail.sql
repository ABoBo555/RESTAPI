USE HR_DB
GO

CREATE OR ALTER PROCEDURE dbo.usp_GetUserByEmail

    @Email NVARCHAR(255)

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

        Email = @Email
        AND IsActive = 1;

END;
GO