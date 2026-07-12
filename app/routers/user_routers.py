from fastapi import (
    APIRouter,
    Depends,
    Path,
    status,
)

from app.config import (
    ADMIN_ROLE,HR_ROLE,
)

from app.schemas import (
    CreateUserRequest,
    MessageResponse,
    RegisterUserResponse,
    UserDetail,
    UserListQuery,
    UserListResponse,
    UserUpdate,
)

from app.security import (
    get_current_user,
    require_roles,
)

from app.services.user_service import (
    admin_create_user,
    delete_user,
    get_user_by_id,
    get_users,
    update_user,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[
        Depends(get_current_user),
    ],
)

@router.get(
    "/",
    response_model=UserListResponse,
    status_code=status.HTTP_200_OK,
    summary="Get All Users",
)
def get_all_users(
    query: UserListQuery = Depends(),
):
    """
    Retrieve all users.

    Admin only.
    """

    return get_users(query)


@router.get(
    "/{user_id}",
    response_model=UserDetail,
    status_code=status.HTTP_200_OK,
    summary="Get User By ID",
)
def get_user(
    user_id: int = Path(
        ...,
        gt=0,
        description="User ID",
    ),
):
    """
    Retrieve a user by ID.
    """

    return get_user_by_id(user_id)



@router.post(
    "/",
    response_model=RegisterUserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create User",
    dependencies=[
        Depends(require_roles(ADMIN_ROLE)),
        Depends(require_roles(ADMIN_ROLE, HR_ROLE)),
    ],
)
def create_user(
    request: CreateUserRequest,
):
    """
    Create a new user.

    Admin only.
    """

    user = admin_create_user(request)

    return RegisterUserResponse(
        message="User created successfully.",
        user=user,
    )


@router.put(
    "/{user_id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    summary="Update User",
    dependencies=[
        Depends(require_roles(ADMIN_ROLE)),
        Depends(require_roles(ADMIN_ROLE, HR_ROLE)),
    ],
)
def update_existing_user(
    user_id: int = Path(
        ...,
        gt=0,
        description="User ID",
    ),
    request: UserUpdate = ...,
):
    """
    Update an existing user.

    Admin only.
    """

    update_user(
        user_id,
        request,
    )

    return MessageResponse(
        message="User updated successfully.",
    )


@router.delete(
    "/{user_id}",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete User",
    dependencies=[
        Depends(require_roles(ADMIN_ROLE)),
        Depends(require_roles(ADMIN_ROLE, HR_ROLE)),
    ],
)
def delete_existing_user(
    user_id: int = Path(
        ...,
        gt=0,
        description="User ID",
    ),
):
    """
    Soft delete a user.

    Admin only.
    """

    delete_user(user_id)

    return MessageResponse(
        message="User deleted successfully.",
    )