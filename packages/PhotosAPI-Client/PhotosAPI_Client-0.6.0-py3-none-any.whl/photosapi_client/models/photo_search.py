from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PhotoSearch")


@_attrs_define
class PhotoSearch:
    """
    Attributes:
        id (str):
        filename (str):
        caption (Union[None, str]):
    """

    id: str
    filename: str
    caption: Union[None, str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        filename = self.filename

        caption: Union[None, str]
        caption = self.caption

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "filename": filename,
                "caption": caption,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        filename = d.pop("filename")

        def _parse_caption(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        caption = _parse_caption(d.pop("caption"))

        photo_search = cls(
            id=id,
            filename=filename,
            caption=caption,
        )

        photo_search.additional_properties = d
        return photo_search

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
