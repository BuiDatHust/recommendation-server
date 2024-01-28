from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetListRecommendUserRequest(_message.Message):
    __slots__ = ("id", "ids", "limit")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    id: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    def __init__(self, id: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ...) -> None: ...

class GetListRecommendUserResponse(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("id", "sexual_orientation", "relationship_goal", "passions", "pets", "workout", "smoking", "sleeping_habit", "score")
    ID_FIELD_NUMBER: _ClassVar[int]
    SEXUAL_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_GOAL_FIELD_NUMBER: _ClassVar[int]
    PASSIONS_FIELD_NUMBER: _ClassVar[int]
    PETS_FIELD_NUMBER: _ClassVar[int]
    WORKOUT_FIELD_NUMBER: _ClassVar[int]
    SMOKING_FIELD_NUMBER: _ClassVar[int]
    SLEEPING_HABIT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    id: str
    sexual_orientation: str
    relationship_goal: str
    passions: _containers.RepeatedScalarFieldContainer[str]
    pets: str
    workout: str
    smoking: str
    sleeping_habit: str
    score: int
    def __init__(self, id: _Optional[str] = ..., sexual_orientation: _Optional[str] = ..., relationship_goal: _Optional[str] = ..., passions: _Optional[_Iterable[str]] = ..., pets: _Optional[str] = ..., workout: _Optional[str] = ..., smoking: _Optional[str] = ..., sleeping_habit: _Optional[str] = ..., score: _Optional[int] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("is_success",)
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    def __init__(self, is_success: bool = ...) -> None: ...
