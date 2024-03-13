# -*- coding: utf-8

#  Copyright (c) 2021 <Florian Alu - alu@prolibre.com - https://www.prolibre.com>
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU Affero General Public License as
#      published by the Free Software Foundation, either version 3 of the
#      License, or any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU Affero General Public License for more details.
#
#      You should have received a copy of the GNU Affero General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NobinobiKitchenConfig(AppConfig):
    name = 'nobinobi_kitchen'
    verbose_name = _("Kitchen")

    def ready(self):
        try:
            import nobinobi_kitchen.signals  # noqa F401
        except ImportError:
            pass
