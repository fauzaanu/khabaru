from django.templatetags.static import static
from django.utils.html import format_html
from wagtail import hooks
#
#
# @hooks.register('insert_editor_css', order=2)
# def editor_css():
#     """
#     Register the insert_editor_css hook and apply custom CSS styling to the editor.
#
#     Returns:
#         str: The CSS code to be inserted.
#
#     Example:
#         register_insert_editor_css_hook()
#         css = editor_css()
#     """
#     return format_html('<style>.Draftail-Editor { direction: rtl; }</style>')

#
# # inject some javascript to the admin
# @hooks.register('insert_global_admin_js', order=2)
# def global_admin_js():
#     """
#     Method to generate and return JavaScript code to add a bottom button to the admin to switch to RTL and back
#
#     Returns:
#         str: JavaScript code to add the button
#     """
#     return """
# <script>
#    // add a bottom button to the admin to switch to RTL and back
#     const rtl_button = document.createElement('button');
#     rtl_button.innerHTML = 'RTL';
#     rtl_button.onclick = () => {
#         const html = document.querySelector('html');
#         html.dir = html.dir === 'rtl' ? 'ltr' : 'rtl';
#     }
#
#     // add the button to the bottom of main
#     const main_doc = document.querySelector('#main');
#     document.querySelector('body').insertBefore(rtl_button, main_doc);
#
#     // center the button horizontally
#     rtl_button.style.position = 'fixed';
#     rtl_button.style.bottom = '0';
#     rtl_button.style.left = '50%';
#     rtl_button.style.transform = 'translateX(-50%)';
#     rtl_button.style.zIndex = '1000';
# </script>
# """
#
#
# # make RTL the default direction
# @hooks.register('insert_global_admin_css', order=2)
# def global_admin_css():
#     """
#     Method to generate and return CSS code to set the default direction of the admin to RTL
#
#     Returns:
#         str: CSS code to set the default direction to RTL
#     """
#     return """
# <style>
#     html {
#         direction: rtl;
#     }
# </style>
# """


@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/admin_custom.css'))
