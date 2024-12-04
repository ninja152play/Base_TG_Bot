from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase, PrimaryKeyField,
)


from config_data.config import DATE_FORMAT, DB_PATH

db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    class Meta:
        db_table = "Users"
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()
    last_name = CharField(null=True)


class Task(BaseModel):
    task_id = AutoField()
    user = ForeignKeyField(User, backref="tasks")
    title = CharField()
    due_date = DateField()
    is_done = BooleanField(default=False)

    def __str__(self):
        return "{task_id}. {check} {title} - {due_date}".format(
            task_id=self.task_id,
            check="[V]" if self.is_done else "[ ]",
            title=self.title,
            due_date=self.due_date.strftime(DATE_FORMAT),
        )


class Commands(BaseModel):
    class Meta:
        db_table = "Commands"

    command_id = PrimaryKeyField(null=False)
    user = ForeignKeyField(User, backref="hist")
    title = CharField()
    due_date = DateField()

    def __str__(self):
        return "{command_id}. {title} - {due_date}".format(
            command_id=self.command_id,
            title=self.title,
            due_date=self.due_date.strftime(DATE_FORMAT),
        )


def create_models():
    db.create_tables(BaseModel.__subclasses__())
