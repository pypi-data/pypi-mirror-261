from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlbumModified")


@_attrs_define
class AlbumModified:
    """
    Attributes:
        name (str):
        title (str):
        cover (Union[None, str]):
    """

    name: str
    title: str
    cover: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        title = self.title

        cover: Union[None, str]
        cover = self.cover

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        def _parse_cover(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        cover = _parse_cover(d.pop("cover"))

        album_modified = cls(
            name=name,
            title=title,
            cover=cover,
        )

        album_modified.additional_properties = d
        return album_modified

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
