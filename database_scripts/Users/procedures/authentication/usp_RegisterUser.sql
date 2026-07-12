USE HR_DB
GO

CREATE OR ALTER PROCEDURE dbo.usp_RegisterUser

    @Username NVARCHAR(50),
    @Email NVARCHAR(255),
    @PasswordHash NVARCHAR(255),
    @Role NVARCHAR(20) = 'Employee'

AS
BEGIN

    SET NOCOUNT ON;

    --------------------------------------------------------
    -- Username already exists
    --------------------------------------------------------

    IF EXISTS
    (
        SELECT 1
        FROM dbo.Users
        WHERE Username = @Username
    )
    BEGIN
        THROW 50001, 'Username already exists.', 1;
    END;

    --------------------------------------------------------
    -- Email already exists
    --------------------------------------------------------

    IF EXISTS
    (
        SELECT 1
        FROM dbo.Users
        WHERE Email = @Email
    )
    BEGIN
        THROW 50002, 'Email already exists.', 1;
    END;

    --------------------------------------------------------
    -- Insert User
    --------------------------------------------------------

    INSERT INTO dbo.Users
    (
        Username,
        Email,
        PasswordHash,
        Role
    )
    VALUES
    (
        @Username,
        @Email,
        @PasswordHash,
        @Role
    );

    --------------------------------------------------------
    -- Return new UserID
    --------------------------------------------------------

    SELECT
        CAST(SCOPE_IDENTITY() AS INT) AS UserID;

END;
GO