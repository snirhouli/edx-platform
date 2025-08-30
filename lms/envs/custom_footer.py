"""
Custom footer settings to remove Open edX branding
Add this to your settings configuration
"""

# Override the default footer settings
FOOTER_OPENEDX_URL = ""  # Empty to disable the link
FOOTER_OPENEDX_LOGO_IMAGE = ""  # Empty to disable the logo

# Custom platform name
PLATFORM_NAME = "Your Learning Platform"

# Custom copyright text (this will override the default copyright)
# You can set this in your site configuration or environment variables
CUSTOM_FOOTER_COPYRIGHT = "© Your Organization Name. All rights reserved."

# Hide the Open edX link in the footer
HIDE_OPENEDX_LINK = True 