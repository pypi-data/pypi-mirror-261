from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import time_machine
from dateutil.relativedelta import relativedelta
from django.contrib.sites.models import Site
from django.test import TestCase, override_settings, tag
from edc_protocol.research_protocol_config import ResearchProtocolConfig
from edc_sites.site import sites as site_sites
from edc_utils import get_utcnow
from faker import Faker
from model_bakery import baker

from edc_consent.field_mixins import IdentityFieldsMixinError
from edc_consent.site_consents import site_consents

from ...exceptions import ConsentDefinitionDoesNotExist, ConsentDefinitionModelError
from ..consent_test_utils import consent_factory

fake = Faker()


@time_machine.travel(datetime(2019, 4, 1, 8, 00, tzinfo=ZoneInfo("UTC")))
@override_settings(
    EDC_PROTOCOL_STUDY_OPEN_DATETIME=get_utcnow() - relativedelta(years=5),
    EDC_PROTOCOL_STUDY_CLOSE_DATETIME=get_utcnow() + relativedelta(years=1),
    EDC_AUTH_SKIP_SITE_AUTHS=True,
    EDC_AUTH_SKIP_AUTH_UPDATER=False,
)
class TestConsentModel(TestCase):
    def setUp(self):
        self.study_open_datetime = ResearchProtocolConfig().study_open_datetime
        self.study_close_datetime = ResearchProtocolConfig().study_close_datetime
        site_consents.registry = {}
        self.consent_v1 = consent_factory(
            start=self.study_open_datetime,
            end=self.study_open_datetime + timedelta(days=50),
            version="1.0",
        )
        self.consent_v2 = consent_factory(
            start=self.study_open_datetime + timedelta(days=51),
            end=self.study_open_datetime + timedelta(days=100),
            version="2.0",
            updated_by="3.0",
        )
        self.consent_v3 = consent_factory(
            model="consent_app.subjectconsentv3",
            start=self.study_open_datetime + timedelta(days=101),
            end=self.study_open_datetime + timedelta(days=150),
            version="3.0",
            updates=(self.consent_v2, "consent_app.subjectconsentupdatev3"),
        )
        self.dob = self.study_open_datetime - relativedelta(years=25)

    def test_encryption(self):
        subject_consent = baker.make_recipe(
            "consent_app.subjectconsent",
            first_name="ERIK",
            consent_datetime=self.study_open_datetime,
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.first_name, "ERIK")

    def test_gets_subject_identifier(self):
        """Asserts a blank subject identifier is set to the
        subject_identifier_as_pk.
        """
        consent = baker.make_recipe(
            "consent_app.subjectconsent",
            subject_identifier=None,
            consent_datetime=self.study_open_datetime,
            dob=get_utcnow() - relativedelta(years=25),
            site=Site.objects.get_current(),
        )
        self.assertIsNotNone(consent.subject_identifier)
        self.assertNotEqual(consent.subject_identifier, consent.subject_identifier_as_pk)
        consent.save()
        self.assertIsNotNone(consent.subject_identifier)
        self.assertNotEqual(consent.subject_identifier, consent.subject_identifier_as_pk)

    def test_subject_has_current_consent(self):
        subject_identifier = "123456789"
        identity = "987654321"
        baker.make_recipe(
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime + timedelta(days=1),
            dob=get_utcnow() - relativedelta(years=25),
        )
        cdef = site_consents.get_consent_definition(
            model="consent_app.subjectconsent", version="1.0"
        )
        subject_consent = cdef.get_consent_for(
            subject_identifier="123456789",
            report_datetime=self.study_open_datetime + timedelta(days=1),
        )
        self.assertEqual(subject_consent.version, "1.0")
        baker.make_recipe(
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime + timedelta(days=60),
            dob=get_utcnow() - relativedelta(years=25),
        )
        cdef = site_consents.get_consent_definition(
            model="consent_app.subjectconsent", version="2.0"
        )
        subject_consent = cdef.get_consent_for(
            subject_identifier="123456789",
            report_datetime=self.study_open_datetime + timedelta(days=60),
        )
        self.assertEqual(subject_consent.version, "2.0")

    def test_model_updates(self):
        subject_identifier = "123456789"
        identity = "987654321"
        consent = baker.make_recipe(
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime,
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(consent.version, "1.0")
        consent = baker.make_recipe(
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime + timedelta(days=51),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(consent.version, "2.0")
        consent = baker.make_recipe(
            "consent_app.subjectconsentv3",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime + timedelta(days=101),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(consent.version, "3.0")

    def test_model_updates2(self):
        subject_identifier = "123456789"
        identity = "987654321"
        consent = baker.make_recipe(
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime,
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(consent.version, "1.0")
        consent = baker.make_recipe(
            "consent_app.subjectconsentv3",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=self.study_open_datetime + timedelta(days=101),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(consent.version, "3.0")

    def test_model_updates_or_first_based_on_date(self):
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=110))
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"
        consent = baker.make_recipe(
            "consent_app.subjectconsentv3",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(consent.version, "3.0")

    def test_model_updates_from_v1_to_v2(self):
        traveller = time_machine.travel(self.study_open_datetime)
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"

        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.subject_identifier, subject_identifier)
        self.assertEqual(subject_consent.identity, identity)
        self.assertEqual(subject_consent.confirm_identity, identity)
        self.assertEqual(subject_consent.version, cdef.version)
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)
        traveller.stop()
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=51))
        traveller.start()

        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.subject_identifier, subject_identifier)
        self.assertEqual(subject_consent.identity, identity)
        self.assertEqual(subject_consent.confirm_identity, identity)
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)

    @tag("1")
    def test_v3_extends_v2_end_date_up_to_v3_consent_datetime(self):
        traveller = time_machine.travel(self.study_open_datetime)
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"

        # consent version 1
        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)
        self.assertEqual(subject_consent.version, "1.0")
        traveller.stop()

        # consent version 2
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=51))
        traveller.start()
        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)
        self.assertEqual(subject_consent.version, "2.0")
        traveller.stop()

        # consent version 3.0
        traveller = time_machine.travel(cdef.end + relativedelta(days=5))
        traveller.start()
        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)
        self.assertEqual(subject_consent.version, "3.0")
        self.assertEqual(cdef.version, "3.0")

        # get cdef for 3.0
        cdef = site_consents.get_consent_definition(
            report_datetime=get_utcnow(), site=site_sites.get(subject_consent.site.id)
        )
        self.assertEqual(cdef.version, "3.0")

        # use cdef-3.0 to get subject_consent 3.0
        subject_consent = cdef.get_consent_for(
            subject_identifier=subject_identifier, report_datetime=get_utcnow()
        )
        self.assertEqual(subject_consent.version, "3.0")

        # use cdef-3.0 to get subject_consent 2.0 showing that the lower bound
        # of a cdef that updates is extended to return a 2.0 consent
        subject_consent = cdef.get_consent_for(
            subject_identifier=subject_identifier,
            report_datetime=cdef.start - relativedelta(days=1),
        )
        self.assertEqual(subject_consent.version, "2.0")

    def test_first_consent_is_v2(self):
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=51))
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"

        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        self.assertEqual(cdef.version, "2.0")
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.subject_identifier, subject_identifier)
        self.assertEqual(subject_consent.identity, identity)
        self.assertEqual(subject_consent.confirm_identity, identity)
        self.assertEqual(subject_consent.version, cdef.version)
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)

    def test_first_consent_is_v3(self):
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=101))
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"

        cdef = site_consents.get_consent_definition(report_datetime=get_utcnow())
        self.assertEqual(cdef.version, "3.0")
        subject_consent = baker.make_recipe(
            cdef.model,
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )
        self.assertEqual(subject_consent.subject_identifier, subject_identifier)
        self.assertEqual(subject_consent.identity, identity)
        self.assertEqual(subject_consent.confirm_identity, identity)
        self.assertEqual(subject_consent.version, cdef.version)
        self.assertEqual(subject_consent.consent_definition_name, cdef.name)

    def test_raise_with_date_past_any_consent_period(self):
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=200))
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"
        self.assertRaises(
            ConsentDefinitionDoesNotExist,
            baker.make_recipe,
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )

    def test_raise_with_incorrect_model_for_cdef(self):
        traveller = time_machine.travel(self.study_open_datetime + timedelta(days=120))
        traveller.start()
        subject_identifier = "123456789"
        identity = "987654321"
        self.assertRaises(
            ConsentDefinitionModelError,
            baker.make_recipe,
            "consent_app.subjectconsent",
            subject_identifier=subject_identifier,
            identity=identity,
            confirm_identity=identity,
            consent_datetime=get_utcnow(),
            dob=get_utcnow() - relativedelta(years=25),
        )

    def test_model_str_repr_etc(self):
        obj = baker.make_recipe(
            "consent_app.subjectconsent",
            screening_identifier="ABCDEF",
            subject_identifier="12345",
            consent_datetime=self.study_open_datetime + relativedelta(days=1),
        )

        self.assertTrue(str(obj))
        self.assertTrue(repr(obj))
        self.assertTrue(obj.age_at_consent)
        self.assertTrue(obj.formatted_age_at_consent)
        self.assertEqual(obj.report_datetime, obj.consent_datetime)

    def test_checks_identity_fields_match_or_raises(self):
        self.assertRaises(
            IdentityFieldsMixinError,
            baker.make_recipe,
            "consent_app.subjectconsent",
            subject_identifier="12345",
            consent_datetime=self.study_open_datetime + relativedelta(days=1),
            identity="123456789",
            confirm_identity="987654321",
        )
