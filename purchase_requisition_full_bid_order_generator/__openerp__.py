# -*- coding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Purchase Requisition Full Bid Order Generator",
    "version": "1.0",
    "author": "AvanzOSC, "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza",
    "website": "www.avanzosc.es",
    "category": "Purchase Management",
    "contributors": ["Esther Martín <esthermartin@avanzosc.es>",
                     "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
                     "Ana Juaristi <anajuaristi@avanzosc.es>",
                     "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>"],
    "depends": ["base", "purchase", "purchase_requisition"],
    "data": [
            "views/bids_ext_view.xml",
            "views/purchase_config_setting_view.xml",],
    "installable": True
}
