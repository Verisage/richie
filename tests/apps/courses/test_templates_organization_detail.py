"""
End-to-end tests for the organization detail view
"""
import re

from cms.test_utils.testcases import CMSTestCase

from richie.apps.core.factories import UserFactory
from richie.apps.courses.factories import (
    CourseFactory,
    OrganizationFactory,
    PersonFactory,
)


class OrganizationCMSTestCase(CMSTestCase):
    """
    End-to-end test suite to validate the content and Ux of the organization detail view
    """

    def test_templates_organization_detail_cms_published_content(self):
        """
        Validate that the important elements are displayed on a published organization page
        """
        courses = CourseFactory.create_batch(4)
        organization = OrganizationFactory(
            page_title="La Sorbonne", fill_courses=courses
        )
        page = organization.extended_object

        # Publish only 2 out of 4 courses
        courses[0].extended_object.publish("en")
        courses[1].extended_object.publish("en")

        # The unpublished objects may have been published and unpublished which puts them in a
        # status different from objects that have never been published.
        # We want to test both cases.
        courses[2].extended_object.publish("en")
        courses[2].extended_object.unpublish("en")

        # The page should not be visible before it is published
        url = page.get_absolute_url()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

        # Publish the organization and ensure the content is correct
        page.publish("en")
        response = self.client.get(url)
        self.assertContains(
            response, "<title>La Sorbonne</title>", html=True, status_code=200
        )
        self.assertContains(
            response,
            '<h1 class="organization-detail__title">La Sorbonne</h1>',
            html=True,
        )

        # Only published courses should be present on the page
        for course in courses[:2]:
            self.assertContains(
                response,
                '<p class="course-glimpse__content__title">{:s}</p>'.format(
                    course.extended_object.get_title()
                ),
                html=True,
            )
        for course in courses[-2:]:
            self.assertNotContains(response, course.extended_object.get_title())

    def test_templates_organization_detail_cms_draft_content(self):
        """
        A staff user should see a draft organization including its draft elements with an
        annotation.
        """
        user = UserFactory(is_staff=True, is_superuser=True)
        self.client.login(username=user.username, password="password")

        courses = CourseFactory.create_batch(4)
        organization = OrganizationFactory(
            page_title="La Sorbonne", fill_courses=courses
        )
        page = organization.extended_object

        # Publish only 2 out of 4 courses
        courses[0].extended_object.publish("en")
        courses[1].extended_object.publish("en")

        # The unpublished objects may have been published and unpublished which puts them in a
        # status different from objects that have never been published.
        # We want to test both cases.
        courses[2].extended_object.publish("en")
        courses[2].extended_object.unpublish("en")

        # The page should be visible as draft to the staff user
        url = page.get_absolute_url()
        response = self.client.get(url)
        self.assertContains(
            response, "<title>La Sorbonne</title>", html=True, status_code=200
        )
        self.assertContains(
            response,
            '<h1 class="organization-detail__title">La Sorbonne</h1>',
            html=True,
        )

        # The published courses should be present on the page
        for course in courses[:2]:
            self.assertContains(
                response,
                '<p class="course-glimpse__content__title">{:s}</p>'.format(
                    course.extended_object.get_title()
                ),
                html=True,
            )
        # Draft courses should also be present on the page with an annotation for styling
        for course in courses[-2:]:
            self.assertContains(
                response,
                '<a href="{link:s}" class="{name:s} {name:s}--link {name:s}--draft">'.format(
                    name="course-glimpse",
                    link=course.extended_object.get_absolute_url(),
                ),
            )
            self.assertContains(
                response,
                '<p class="course-glimpse__content__title">{title:s}</p>'.format(
                    title=course.extended_object.get_title()
                ),
                html=True,
            )

    def test_templates_organization_detail_related_persons(self):
        """
        Persons related to an organization via a plugin should appear on the organization
        detail page.
        """
        user = UserFactory(is_staff=True, is_superuser=True)
        self.client.login(username=user.username, password="password")

        organization = OrganizationFactory()
        person = PersonFactory(fill_organizations=[organization])
        page = organization.extended_object

        url = page.get_absolute_url()
        response = self.client.get(url)

        # The person should be present on the page
        pattern = (
            r'<a href="{url:s}">'
            r'<h2 class="person-glimpse__content__wrapper__title">'
            r".*{name:s}.*</h2></a>"
        ).format(
            url=person.extended_object.get_absolute_url(),
            name=person.extended_object.get_title(),
        )
        self.assertIsNotNone(re.search(pattern, str(response.content)))
