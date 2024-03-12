"""Menu items."""

from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

menu_items = (
    NavMenuTab(
        name="WRRM",
        groups=(
            NavMenuGroup(
                name="Attributes",
                weight=150,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_plugin_w_rrm:radioattributes_list",
                        name="Radio Attributes",
                        permissions=["nautobot_plugin_w_rrm.add_radioattributes"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_w_rrm:radioattributes_list",
                                permissions=["nautobot_plugin_w_rrm.add_radioattributes"],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_w_rrm:locationattributes_list",
                        name="Location Attributes",
                        permissions=["nautobot_plugin_w_rrm.add_locationattributes"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_w_rrm:locationattributes_list",
                                permissions=["nautobot_plugin_w_rrm.add_locationattributes"],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_plugin_w_rrm:circuitattributes_list",
                        name="Circuit Attributes",
                        permissions=["nautobot_plugin_w_rrm.add_circuitattributes"],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_plugin_w_rrm:circuitattributes_list",
                                permissions=["nautobot_plugin_w_rrm.add_circuitattributes"],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
