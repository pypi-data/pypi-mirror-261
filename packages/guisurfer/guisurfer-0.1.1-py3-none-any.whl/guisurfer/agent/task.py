from dataclasses import dataclass, field
import uuid
import time
from typing import List, Optional
import json

from deepthread import RoleThread

from ..db.models import TaskRecord
from ..db.conn import WithDB
from ..server.models import TaskModel


@dataclass
class Task(WithDB):
    """An agent task"""

    description: str
    owner_id: str
    id: str = str(uuid.uuid4())
    url: Optional[str] = None
    status: str = "created"
    created: float = time.time()
    started: float = 0.0
    completed: float = 0.0
    thread: RoleThread = field(default_factory=RoleThread)
    assigned_to: Optional[str] = None
    error: str = ""
    output: str = ""

    def __post_init__(self) -> None:
        self.save()

    def to_record(self) -> TaskRecord:
        return TaskRecord(
            id=self.id,
            owner_id=self.owner_id,
            description=self.description,
            url=self.url,
            status=self.status,
            created=self.created,
            started=self.started,
            completed=self.completed,
            thread_id=self.thread._id,
            assigned_to=self.assigned_to,
            error=self.error,
            output=self.output,
        )

    @classmethod
    def from_record(cls, record: TaskRecord) -> "Task":
        obj = cls.__new__(cls)
        obj.id = record.id
        obj.owner_id = record.owner_id
        obj.description = record.description
        obj.url = record.url
        obj.status = record.status
        obj.created = record.created
        obj.started = record.started
        obj.completed = record.completed
        obj.thread = RoleThread.find(id=record.thread_id)[0]
        obj.assigned_to = record.assigned_to
        obj.error = record.error
        obj.output = record.output
        return obj

    def post_message(
        self,
        role: str,
        msg: str,
        images: List[str] = [],
        private: bool = False,
        metadata: Optional[dict] = None,
    ) -> None:
        self.thread.post(role, msg, images, private, metadata)
        self.save()

    def save(self) -> None:
        for db in self.get_db():
            db.merge(self.to_record())
            db.commit()

    @classmethod
    def find(cls, **kwargs) -> List["Task"]:
        for db in cls.get_db():
            records = db.query(TaskRecord).filter_by(**kwargs).all()
            return [cls.from_record(record) for record in records]

    @classmethod
    def delete(cls, id: str, owner_id: str) -> None:
        for db in cls.get_db():
            record = db.query(TaskRecord).filter_by(id=id, owner_id=owner_id).first()
            if record:
                db.delete(record)
                db.commit()

    def to_schema(self) -> TaskModel:
        return TaskModel(
            id=self.id,
            description=self.description,
            url=self.url,
            thread=self.thread.to_schema(),
            status=self.status,
            created=self.created,
            started=self.started,
            completed=self.completed,
            assigned_to=self.assigned_to,
            error=self.error,
            output=self.output,
        )

    @classmethod
    def from_schema(cls, schema: TaskModel, owner_id: str) -> "Task":
        return cls(
            id=schema.id,
            owner_id=owner_id,
            description=schema.description,
            url=schema.url,
            thread=RoleThread.from_schema(schema.thread),
            status=schema.status,
            created=schema.created,
            started=schema.started,
            completed=schema.completed,
            assigned_to=schema.assigned_to,
            error=schema.error,
            output=schema.output,
        )
