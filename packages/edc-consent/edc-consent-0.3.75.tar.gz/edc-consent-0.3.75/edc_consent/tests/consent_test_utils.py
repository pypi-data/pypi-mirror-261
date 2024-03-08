from __future__ import annotations

from datetime import datetime

from edc_protocol.research_protocol_config import ResearchProtocolConfig

from edc_consent.consent_definition import ConsentDefinition
from edc_consent.site_consents import site_consents


def consent_definition_factory(
    model: str | None = None,
    start: datetime = None,
    end: datetime = None,
    gender: list[str] | None = None,
    updates: tuple[str, str] = None,
    updated_by: str | None = None,
    version: str | None = None,
    age_min: int | None = None,
    age_max: int | None = None,
    age_is_adult: int | None = None,
) -> ConsentDefinition:
    options = dict(
        start=start or ResearchProtocolConfig().study_open_datetime,
        end=end or ResearchProtocolConfig().study_close_datetime,
        gender=gender or ["M", "F"],
        updates=updates or None,
        updated_by=updated_by or None,
        version=version or "1",
        age_min=age_min or 16,
        age_max=age_max or 64,
        age_is_adult=age_is_adult or 18,
    )
    model = model or "consent_app.subjectconsent"
    consent_definition = ConsentDefinition(model, **options)
    site_consents.register(consent_definition)
    return consent_definition


def consent_factory(model=None, **kwargs):
    options = dict(
        start=kwargs.get("start"),
        end=kwargs.get("end"),
        gender=kwargs.get("gender", ["M", "F"]),
        updates=kwargs.get("updates", None),
        updated_by=kwargs.get("updated_by", None),
        version=kwargs.get("version", "1"),
        age_min=kwargs.get("age_min", 16),
        age_max=kwargs.get("age_max", 64),
        age_is_adult=kwargs.get("age_is_adult", 18),
        validate_duration_overlap_by_model=kwargs.get(
            "validate_duration_overlap_by_model", True
        ),
    )
    model = kwargs.get("model", model or "consent_app.subjectconsent")
    consent_definition = ConsentDefinition(model, **options)
    site_consents.register(consent_definition)
    return consent_definition
