from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem


#
# Define plugin menu buttons
#


# Access List
accesslist_buttons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:accesslist_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_access_lists.add_accesslist'],
    )
]

# Access List Rule
accesslistrule_buttons = [
    PluginMenuButton(
        link='plugins:netbox_access_lists:accesslistrule_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        permissions=['netbox_access_lists.add_accesslistrule'],
    )
]

#
# Define plugin menu items
#

# Access List
accesslist_item = PluginMenuItem(
    link='plugins:netbox_access_lists:accesslist_list',
    link_text='Access Lists',
    permissions=['netbox_access_lists.view_accesslist'],
    buttons=accesslist_buttons,
)

# Access List Rule
accesslistrule_item = PluginMenuItem(
    link='plugins:netbox_access_lists:accesslistrule_list',
    link_text='Access List Rules',
    permissions=['netbox_access_lists.view_accesslistrule'],
    buttons=accesslistrule_buttons,
)

#
# Define plugin menu groups
#

menu = PluginMenu(
    label='Access Lists',
    groups=(
        (
            'Access Lists',
            (accesslist_item,),
        ),
        (
            'Rules',
            (accesslistrule_item,),
        ),
    ),
    icon_class='mdi mdi-lock',
)
