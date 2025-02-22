"""
Default settings for the Richie courses app.

If you use Django Configuration for your settings, you can use our mixin to import these
default settings:
    ```
    from configurations import Configuration
    from richie.apps.courses.settings.mixins import RichieCoursesConfigurationMixin

    class MyConfiguration(RichieCoursesConfigurationMixin, Configuration):
        ...
    ```

Otherwise, you can just use the usual Django pattern in your settings.py file:
    ```
    from richie.apps.courses.settings import *
    ```
"""
from django.utils.translation import ugettext_lazy as _

# Easy Thumbnails
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
    "easy_thumbnails.processors.background",
)

# Django CMS
CMS_TEMPLATES = (
    ("courses/cms/course_detail.html", _("Course page")),
    ("courses/cms/course_run_detail.html", _("Course run page")),
    ("courses/cms/organization_list.html", _("Organization list")),
    ("courses/cms/organization_detail.html", _("Organization page")),
    ("courses/cms/category_list.html", _("Category list")),
    ("courses/cms/category_detail.html", _("Category page")),
    ("courses/cms/blogpost_list.html", _("Blog post list")),
    ("courses/cms/blogpost_detail.html", _("Blog post page")),
    ("courses/cms/person_detail.html", _("Person page")),
    ("courses/cms/person_list.html", _("Person list")),
    ("search/search.html", _("Search")),
    ("richie/child_pages_list.html", _("List of child pages")),
    ("richie/homepage.html", _("Homepage")),
    ("richie/single_column.html", _("Single column")),
)

CMS_PLACEHOLDER_CONF = {
    # Homepage
    "richie/homepage.html maincontent": {
        "name": _("Main content"),
        "plugins": ["LargeBannerPlugin", "SectionPlugin"],
        "child_classes": {
            "SectionPlugin": [
                "BlogPostPlugin",
                "CoursePlugin",
                "CategoryPlugin",
                "LinkPlugin",
                "OrganizationPlugin",
                "PersonPlugin",
            ]
        },
    },
    # Single column page
    "richie/single-column.html maincontent": {
        "name": _("Main content"),
        "excluded_plugins": ["CKEditorPlugin", "GoogleMapPlugin"],
        "parent_classes": {
            "BlogPostPlugin": ["SectionPlugin"],
            "CategoryPlugin": ["SectionPlugin"],
            "CoursePlugin": ["SectionPlugin"],
            "OrganizationPlugin": ["SectionPlugin"],
            "PersonPlugin": ["SectionPlugin"],
        },
        "child_classes": {
            "SectionPlugin": [
                "BlogPostPlugin",
                "CategoryPlugin",
                "CoursePlugin",
                "LinkPlugin",
                "OrganizationPlugin",
                "PersonPlugin",
            ]
        },
    },
    # Course detail
    "courses/cms/course_detail.html course_cover": {
        "name": _("Cover"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/course_detail.html course_introduction": {
        "name": _("Catch phrase"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/course_detail.html course_teaser": {
        "name": _("Teaser"),
        "plugins": ["VideoPlayerPlugin", "SimplePicturePlugin"],
        "limits": {"VideoPlayerPlugin": 1, "SimplePicturePlugin": 1},
    },
    "courses/cms/course_detail.html course_description": {
        "name": _("About the course"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_skills": {
        "name": _("What you will learn"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_format": {
        "name": _("Format"),
        "plugins": ["PlainTextPlugin"],
    },
    "courses/cms/course_detail.html course_prerequisites": {
        "name": _("Prerequisites"),
        "plugins": ["PlainTextPlugin"],
    },
    "courses/cms/course_detail.html course_team": {
        "name": _("Team"),
        "plugins": ["PersonPlugin"],
    },
    "courses/cms/course_detail.html course_plan": {
        "name": _("Plan"),
        "plugins": ["CKEditorPlugin"],
    },
    "courses/cms/course_detail.html course_information": {
        "name": _("Complementary information"),
        "plugins": ["SectionPlugin"],
        "parent_classes": {
            "CKEditorPlugin": ["SectionPlugin"],
            "SimplePicturePlugin": ["SectionPlugin"],
        },
        "child_classes": {"SectionPlugin": ["CKEditorPlugin", "SimplePicturePlugin"]},
    },
    "courses/cms/course_detail.html course_license_content": {
        "name": _("License for the course content"),
        "plugins": ["LicencePlugin"],
        "limits": {"LicencePlugin": 1},
    },
    "courses/cms/course_detail.html course_license_participation": {
        "name": _("License for the content created by course participants"),
        "plugins": ["LicencePlugin"],
        "limits": {"LicencePlugin": 1},
    },
    "courses/cms/course_detail.html course_categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/course_detail.html course_icons": {
        "name": _("Icon"),
        "plugins": ["CategoryPlugin"],
        "limits": {"CategoryPlugin": 1},
    },
    "courses/cms/course_detail.html course_organizations": {
        "name": _("Organizations"),
        "plugins": ["OrganizationPlugin"],
    },
    "courses/cms/course_detail.html course_assessment": {
        "name": _("Assessment and Certification"),
        "plugins": ["PlainTextPlugin"],
    },
    # Organization detail
    "courses/cms/organization_detail.html banner": {
        "name": _("Banner"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/organization_detail.html logo": {
        "name": _("Logo"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/organization_detail.html description": {
        "name": _("Description"),
        "plugins": ["CKEditorPlugin"],
        "limits": {"CKEditorPlugin": 1},
    },
    # Category detail
    "courses/cms/category_detail.html banner": {
        "name": _("Banner"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/category_detail.html logo": {
        "name": _("Logo"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/category_detail.html icon": {
        "name": _("Icon"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/category_detail.html description": {
        "name": _("Description"),
        "plugins": ["CKEditorPlugin"],
        "limits": {"CKEditorPlugin": 1},
    },
    # Person detail
    "courses/cms/person_detail.html categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/person_detail.html portrait": {
        "name": _("Portrait"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/person_detail.html bio": {
        "name": _("Bio"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/person_detail.html organizations": {
        "name": _("Organizations"),
        "plugins": ["OrganizationPlugin"],
    },
    # Blog page detail
    "courses/cms/blogpost_detail.html author": {
        "name": _("Author"),
        "plugins": ["PersonPlugin"],
        "limits": {"PersonPlugin": 1},
    },
    "courses/cms/blogpost_detail.html categories": {
        "name": _("Categories"),
        "plugins": ["CategoryPlugin"],
    },
    "courses/cms/blogpost_detail.html cover": {
        "name": _("Cover"),
        "plugins": ["SimplePicturePlugin"],
        "limits": {"SimplePicturePlugin": 1},
    },
    "courses/cms/blogpost_detail.html excerpt": {
        "name": _("Excerpt"),
        "plugins": ["PlainTextPlugin"],
        "limits": {"PlainTextPlugin": 1},
    },
    "courses/cms/blogpost_detail.html body": {
        "name": _("Body"),
        "excluded_plugins": ["CKEditorPlugin", "GoogleMapPlugin"],
    },
}

# Main CKEditor configuration
CKEDITOR_SETTINGS = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/richie/css/ckeditor.css",
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Enable some plugins
    # 'extraPlugins': 'codemirror',
    # Disable element filter to enable full HTML5, also this will let
    # append any code, even bad syntax and malicious code, so be careful
    "removePlugins": "stylesheetparser",
    "allowedContent": True,
    # Image plugin options
    "image_prefillDimensions": False,
    # Justify text using shortand class names
    "justifyClasses": ["text-left", "text-center", "text-right"],
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar": "CMS",
    "toolbar_CMS": [
        ["Undo", "Redo"],
        ["cmsplugins", "-", "ShowBlocks"],
        ["Format", "Styles"],
        ["RemoveFormat"],
        ["Maximize"],
        "/",
        ["Bold", "Italic", "Underline", "-", "Subscript", "Superscript"],
        ["JustifyLeft", "JustifyCenter", "JustifyRight"],
        ["Link", "Unlink"],
        ["NumberedList", "BulletedList", "-", "HorizontalRule"],
        ["Source"],
    ],
}
# Share the same configuration for djangocms_text_ckeditor field and derived
# CKEditor widgets/fields
CKEDITOR_SETTINGS["toolbar_HTMLField"] = CKEDITOR_SETTINGS["toolbar_CMS"]

# CKEditor configuration for basic formatting
CKEDITOR_BASIC_CONFIGURATION = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/css/ckeditor.css",
    # Only enable following tag definitions
    "allowedContent": ["p", "b", "i", "a[href]"],
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar": "HTMLField",
    "toolbar_HTMLField": [["Undo", "Redo"], ["Bold", "Italic"], ["Link", "Unlink"]],
}

# CKEditor configuration for formatting limited to:
# paragraph, bold, italic and numbered or bulleted lists.
CKEDITOR_LIMITED_CONFIGURATION = {
    "language": "{{ language }}",
    "skin": "moono-lisa",
    "toolbarCanCollapse": False,
    "contentsCss": "/static/css/ckeditor.css",
    # Only enable following tag definitions
    "allowedContent": ["p", "b", "i", "ol", "ul", "li"],
    # Enabled showblocks as default behavior
    "startupOutlineBlocks": True,
    # Default toolbar configurations for djangocms_text_ckeditor
    "toolbar": "HTMLField",
    "toolbar_HTMLField": [
        ["Undo", "Redo"],
        ["Bold", "Italic"],
        ["Link", "Unlink"],
        ["NumberedList", "BulletedList", "-"],
    ],
}

# Additional LinkPlugin templates. Note how choice value is just a keyword
# instead of full template path. Value is used inside a path formatting
# such as "templates/djangocms_link/VALUE/link.html"
DJANGOCMS_LINK_TEMPLATES = [("button-caesura", _("Button caesura"))]

DJANGOCMS_VIDEO_TEMPLATES = [("full-width", _("Full width"))]

# Richie plugins

RICHIE_PLAINTEXT_MAXLENGTH = {"course_introduction": 200, "bio": 150, "excerpt": 200}

RICHIE_SIMPLETEXT_CONFIGURATION = [
    {
        "placeholders": ["course_skills", "course_plan"],
        "ckeditor": "CKEDITOR_LIMITED_CONFIGURATION",
    },
    {
        "placeholders": ["course_description"],
        "ckeditor": "CKEDITOR_LIMITED_CONFIGURATION",
        "max_length": 1200,
    },
]

RICHIE_SIMPLEPICTURE_PRESETS = {
    # Formatting images for the courses search index
    "cover": {
        "src": {"size": (300, 170), "crop": "smart"},
        "srcset": [
            {
                "options": {"size": (300, 170), "crop": "smart", "upscale": True},
                "descriptor": "300w",
            },
            {
                "options": {"size": (600, 340), "crop": "smart", "upscale": True},
                "descriptor": "600w",
            },
            {
                "options": {"size": (900, 560), "crop": "smart", "upscale": True},
                "descriptor": "900w",
            },
        ],
        "sizes": "300px",
    },
    "icon": {
        "src": {"size": (60, 60), "crop": "smart"},
        "srcset": [
            {
                "options": {"size": (60, 60), "crop": "smart", "upscale": True},
                "descriptor": "60w",
            },
            {
                "options": {"size": (120, 120), "crop": "smart", "upscale": True},
                "descriptor": "120w",
            },
            {
                "options": {"size": (180, 180), "crop": "smart", "upscale": True},
                "descriptor": "180w",
            },
        ],
        "sizes": "60px",
    },
}
