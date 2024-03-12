from dataclasses import dataclass


@dataclass
class LegacyApiUser:
    id: int
    nick: str
    is_deleted: bool = False
    avatar: str | None = None
    gender: int | None = None
    activated: str | None = None
    avatar_id: int | None = None
    category: int | None = None
    client_type: int | None = None
    entry: int | None = None

    @staticmethod
    def from_dict(user: dict):
        return LegacyApiUser(
            id=user["id"],
            nick=user["nick"],
            gender=user.get("gender"),
            is_deleted=user.get("is_deleted"),
            avatar=user["avatar"]["64"] if user.get("avatar") else None,
            avatar_id=user.get("avatar_id"),
            activated=user.get("activated"),
            category=user.get("category"),
            entry=user.get("entry")
        )
