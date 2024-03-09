from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from numbers import Number
from typing import Literal

from dacite import from_dict


@dataclass
class Project:
    id: int | None = None
    name: str | None = None
    company_wide: bool | None = None
    owner: str | None = None
    well_groups: dict | None = None
    custom_attributes: dict | None = None
    note: str | None = None
    well_count: int | None = None
    analysis_count: int | None = None


@dataclass
class Field:
    name: str | None = None
    id: int | None = None
    projects: list | None = None

    def __post_init__(self):
        if self.projects:
            self.projects = [from_dict(data=p, data_class=Project) for p in self.projects]


@dataclass
class Well:
    """
    Required fields:
        name: str
            well name, cannot contain colons
        project_id: int
            Whitson project id
        uwi_api: str
            unique well identifier, e.g. API or license number
    """

    name: str
    project_id: int
    uwi_api: str | None  # e.g. license number, API
    Sw_i: float | None = None  # initial water saturation, %
    bothole_lat: float | None = None
    bothole_long: float | None = None
    bounded: Literal["bounded", "unbounded", "half-bounded"] | None = None
    clusters: Number | None = None
    county: str | None = None
    cr: float | None = None
    custom_attributes: dict | None = None  # guessed this type
    external_id: str | None = None
    fluid_pumped: float | None = None
    gamma_f: float | None = None  # fracture gamma, 1e-4/psia
    gamma_m: float | None = None  # matrix gamma, 1e-4/psia
    groups: list | None = None  # guessed this type
    h: float | None = None  # reservoir height, ft
    h_f: float | None = None  # fracture height, ft
    id: int | None = None  # Whitson well id
    l_w: float | None = None  # gross perforated interval, ft
    n_f: float | None = None  # number of fractures
    note: str | None = None
    p_res_i: float | None = None  # initial reservoir pressure, psia
    phi: float | None = None  # porosity
    process_id: int | None = None
    prop_pumped: float | None = None  # total proppant pumped, lbs
    reservoir: str | None = None
    salinity: float | None = None
    spacing: float | None = None
    stages: Number | None = None
    state: str | None = None
    surf_lat: float | None = None
    surf_long: float | None = None
    t_res: float | None = None  # inital reservoir temperature, F

    def __post_init__(self):
        if ":" in self.name:
            raise TypeError("Illegal character ':' in name")


@dataclass
class ProductionData:
    well_id: str
    qg_sc: list[dict[str, datetime | float | None]]
    gor_sep: list[dict[str, datetime | float | None]]
    qg_sep: list[dict[str, datetime | float | None]]
    qo_sc: list[dict[str, datetime | float | None]]
    qg_gas_lift: list[dict[str, datetime | float | None]]
    gor_sc: list[dict[str, datetime | float | None]]
    liquid_level: list[dict[str, datetime | float | None]]
    p_tubing: list[dict[str, datetime | float | None]]
    p_casing: list[dict[str, datetime | float | None]]
    choke_size: list[dict[str, datetime | float | None]]
    qo_sep: list[dict[str, datetime | float | None]]
    p_sep: list[dict[str, datetime | float | None]]
    qw_sc: list[dict[str, datetime | float | None]]
    t_sep: list[dict[str, datetime | float | None]]
    qw_sep: list[dict[str, datetime | float | None]]
    p_wf_measured: list[dict[str, datetime | float | None]]
