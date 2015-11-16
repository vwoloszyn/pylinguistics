# cases.py - Auxiliary file for silva2011.py
# Copyright (C) 2014  Alessandro Bokan
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:  Alessandro Bokan <alessandro.bokan@gmail.com>


def case1(w, p, p0, pVt, k, c):
    w = w[:p[k] + 1] + '-' + w[p[k] + 1:]
    p0 = p[k] + 1
    k = k + 1 if k + 1 < len(p) else k
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt


def case2(w, p, p0, pVt, k, c):
    w = w[:p[k] + 2] + '-' + w[p[k] + 2:]
    p0 = p[k] + 2
    k = k + 1 if k + 1 < len(p) else k
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt


def case3(w, p, p0, pVt, k, c):
    w = w[:p[k] + 1] + '-' + w[p[k] + 1:]
    p0 = p[k] + 1
    k += 1
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt


def case4(w, p, p0, pVt, k, c):
    w = w[:p[k] + 2] + '-' + w[p[k] + 2:]
    p0 = p[k] + 2
    k = k + 1 if k + 1 < len(p) else k
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt


def case5(w, p, p0, pVt, k, c):
    w = w[:p[k] + 3] + '-' + w[p[k] + 3:]  # Case 5
    p0 = p[k] + 3
    k += 1
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt


def case6(w, p0):
    p0 += len(w) - 1
    return p0


def case7(w, p, p0, pVt, k, c):
    w = w[:p[k] + 3] + '-' + w[p[k] + 3:]  # Case 5
    p0 = p[k] + 3
    k += 1
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt


def case8(w, p, p0, pVt, k, c):
    w = w[:p[k] + 1] + '-' + w[p[k] + 1:]
    p0 = p[k] + 1
    k += 1
    c += 1
    p[k] = p[k] + c
    pVt += 1
    return w, p0, k, c, p, pVt
