USE HR_DB
GO

IF OBJECT_ID('dbo.Users', 'U') IS NOT NULL
BEGIN
    DROP TABLE dbo.Users;
END
GO

CREATE TABLE dbo.Users
(
    UserID INT IDENTITY(1,1) PRIMARY KEY,

    Username NVARCHAR(50) NOT NULL,

    Email NVARCHAR(255) NOT NULL,

    PasswordHash NVARCHAR(255) NOT NULL,

    Role NVARCHAR(20) NOT NULL
        CONSTRAINT DF_Users_Role
        DEFAULT ('Employee'),

    IsActive BIT NOT NULL
        CONSTRAINT DF_Users_IsActive
        DEFAULT (1),

    IsDeleted BIT NOT NULL
        CONSTRAINT DF_Users_IsDeleted
        DEFAULT (0),

    LastLoginAt DATETIME2 NULL,

    CreatedAt DATETIME2 NOT NULL
        CONSTRAINT DF_Users_CreatedAt
        DEFAULT (SYSDATETIME()),

    UpdatedAt DATETIME2 NULL
);
GO


ALTER TABLE dbo.Users
ADD CONSTRAINT UQ_Users_Username
UNIQUE (Username);
GO

ALTER TABLE dbo.Users
ADD CONSTRAINT UQ_Users_Email
UNIQUE (Email);
GO


ALTER TABLE dbo.Users
ADD CONSTRAINT CK_Users_Role
CHECK
(
    Role IN
    (
        'Admin',
        'Manager',
        'Employee',
        'HR',
        'Auditor'
    )
);
GO

CREATE UNIQUE INDEX IX_Users_Username
ON dbo.Users(Username);
GO

CREATE UNIQUE INDEX IX_Users_Email
ON dbo.Users(Email);
GO