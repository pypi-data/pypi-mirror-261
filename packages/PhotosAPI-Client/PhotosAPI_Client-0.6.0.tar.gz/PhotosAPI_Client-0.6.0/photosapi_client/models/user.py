from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        user (str):
        email (Union[None, str]):
        quota (Union[None, int]):
        disabled (Union[None, bool]):
    """

    user: str
    email: Union[None, str]
    quota: Union[None, int]
    disabled: Union[None, bool]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user = self.user

        email: Union[None, str]
        email = self.email

        quota: Union[None, int]
        quota = self.quota

        disabled: Union[None, bool]
        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "email": email,
                "quota": quota,
                "disabled": disabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        def _parse_email(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        email = _parse_email(d.pop("email"))

        def _parse_quota(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        quota = _parse_quota(d.pop("quota"))

        def _parse_disabled(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        disabled = _parse_disabled(d.pop("disabled"))

        user = cls(
            user=user,
            email=email,
            quota=quota,
            disabled=disabled,
        )

        user.additional_properties = d
        return user

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
