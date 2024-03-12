from pydantic import BaseModel, ConfigDict, RootModel


class Project(BaseModel):
    id: int
    name: str
    default_branch: str

    model_config = ConfigDict(extra="allow")


class Projects(RootModel[list[Project]]):
    root: list[Project]

    def __iter__(self):
        return iter(self.root)

    def __len__(self) -> int:
        return len(self.root)
