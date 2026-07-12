USE HR_DB;
GO

CREATE OR ALTER PROCEDURE dbo.usp_CreateUser
(
    @Username NVARCHAR(50),
    @Email NVARCHAR(255),
    @PasswordHash NVARCHAR(255),
    @Role NVARCHAR(50)
)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.Users
    (
        Username,
        Email,
        PasswordHash,
        Role,
        IsActive,
        CreatedAt,
        UpdatedAt,
        IsDeleted
    )
    VALUES
    (
        @Username,
        @Email,
        @PasswordHash,
        @Role,
        1,
        GETDATE(),
        NULL,
        0
    );

    SELECT SCOPE_IDENTITY() AS UserID;
END;
GO