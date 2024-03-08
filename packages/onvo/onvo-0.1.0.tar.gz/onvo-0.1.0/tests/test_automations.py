from .base_test import BaseTest

SAMPLE_DASHBOARD_PARAMS = {
    "description": "Sample dashboard for widget testing",
    "title": "Widget Testing Dashboard",
}

SAMPLE_AUTOMATION_PARAMS = {
    "created_by": "197302e5-88e2-49f4-bbe7-92b5a4dc4264",
    "description": "A sample description",
    "email_format": "This is an automation from Onvo",
    "email_subject": "This is an automation from Onvo",
    "enabled": "false",
    "output_format": "link",
    "recipient_type": "internal",
    "schedule": "",
    "title": "API datasource test",
}


class TestAutomations(BaseTest):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.sampleDashboardId = cls.onvoSDK.dashboards.create(SAMPLE_DASHBOARD_PARAMS)[
            "id"
        ]
        # Skipping test create
        cls.sampleAutomationId = cls.onvoSDK.automations.create(
            {**SAMPLE_AUTOMATION_PARAMS, "dashboard": cls.sampleDashboardId}
        )["id"]

    def test_list(self):
        self.assertShouldRaise(None, self.onvoSDK.automations.list)

    def test_get(self):
        self.assertShouldRaise(
            None, lambda: self.onvoSDK.automations.get(self.sampleAutomationId)
        )

    def test_update(self):
        self.assertShouldRaise(
            None,
            lambda: self.onvoSDK.automations.update(
                self.sampleAutomationId,
                {"description": "A New Test Description. Delete if seen."},
            ),
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.onvoSDK.dashboards.delete(cls.sampleDashboardId)
        cls.onvoSDK.automations.delete(cls.sampleAutomationId)  # Skipping test delete
        super().tearDownClass()
