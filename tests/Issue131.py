# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import absolute_import

from . import Framework


class Issue131(Framework.TestCase):  # https://github.com/jacquev6/PyGithub/pull/133
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user()
        self.repo = self.g.get_user("openmicroscopy").get_repo("ome-documentation")

    def testGetPullWithOrgHeadUser(self):
        user = self.repo.get_pull(204).head.user
        self.assertEqual(user.login, "imcf")
        self.assertEqual(user.type, "Organization")
        self.assertEqual(user.__class__.__name__, "NamedUser")  # Should be Organization

    def testGetPullsWithOrgHeadUser(self):
        for pull in self.repo.get_pulls("closed"):
            if pull.number == 204:
                user = pull.head.user
                self.assertEqual(user, None)
                # Should be:
                # self.assertEqual(user.login, 'imcf')
                # self.assertEqual(user.type, 'Organization')
                # self.assertEqual(user.__class__.__name__, 'NamedUser')  # Should be Organization
                break
        else:
            self.assertTrue(False)
