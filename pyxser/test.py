#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
##     Copyright (c) 2009 Daniel Molina Wegener <dmw@coder.cl>
##
##     This file is part of pyxser.
##
##     pyxser is free software: you can redistribute it and/or modify
##     it under the terms of the GNU Lesser General Public License as
##     published by the Free Software Foundation, either version 3 of
##     the License, or (at your option) any later version.
##
##     pyxser is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with pyxser.  If not, see <http://www.gnu.org/licenses/>.
##
##     <!DOCTYPE pyxs:object
##               PUBLIC "-//coder.cl//DTD pyxser 1.0//EN"
##               "http://projects.coder.cl/pyxser/dtd/pyxser-1.0.dtd">


import sys
import traceback

import pyxser
import testpkg.sample


if __name__ == "__main__":
    another = testpkg.sample.TestAnotherObject()
    another.first_element = 123
    another.second_element = 456

    other = testpkg.sample.TestAnotherObject()
    other.first_element = "abc"
    other.second_element = "cdf"

    thisa = testpkg.sample.TestAnotherObject()
    thisa.first_element = "xyz"
    thisa.second_element = "zyx"

    thisb = testpkg.sample.TestAnotherObject()
    thisb.first_element = "456"
    thisb.second_element = "789"

    thisc = testpkg.sample.TestAnotherObject()
    thisc.first_element = "XXX"
    thisc.second_element = thisb

    test = testpkg.sample.ParentObject("hola", "chao", 2354345L)
    test.child("hi", 4.5, 2354)
    test.nested("holahola", 345, "hola")
    test.subnested(other)
    another.dyn_prop1 = thisa
    test.dyn_prop1 = [u'holá', u'chaó', another]
    test.dyn_prop2 = (u'hol`', u'sïn', 'trip', other)
    test.dyn_prop3 = {'saludo1': u'hólà', 'saludo2': u'chäó', 'saludo4': 'goodbye', 'saludo5': thisc}
    test.dyn_prop4 = u'sómé tèxtè ïñ Unicodè'
    test.dyn_prop5 = u'Añother Texé Iñ ÜnìcóDËc'
    test.dyn_prop6 = 1.5
    test.dyn_prop7 = 1000

    try:
        serialized = pyxser.serialize(test)
        print "Serilized Object:\n" + serialized
        print "Serilized Object Validation:\n", pyxser.validate(serialized)
        print "First Object:\n" + repr(test) + "\n\n"
        unserialized = pyxser.unserialize(serialized)
        print "Unserialized Object:\n" + repr(unserialized) + "\n\n"

        another = testpkg.sample.TestAnotherObject()
        another.first_element = 123
        another.second_element = 456

        serialized = pyxser.serialize(another)
        print "1. Serilized Object:\n" + serialized
        print "Serilized Object Validation:\n", pyxser.validate(serialized)
        unserialized = pyxser.unserialize(serialized)
        print "1. Unserialized Object:\n" + repr(unserialized) + "\n\n"

        other = testpkg.sample.TestAnotherObject()
        other.first_element = "abc"
        other.second_element = "cdf"

        serialized = pyxser.serialize(other)
        print "2. Serilized Object:\n" + serialized
        print "Serilized Object Validation:\n", pyxser.validate(serialized)
        unserialized = pyxser.unserialize(serialized)
        print "2. Unserialized Object:\n" + repr(unserialized) + "\n\n"

        thisa = testpkg.sample.TestAnotherObject()
        thisa.first_element = "xyz"
        thisa.second_element = "zyx"

        serialized = pyxser.serialize(thisa)
        print "3. Serilized Object:\n" + serialized
        print "Serilized Object Validation:\n", pyxser.validate(serialized)
        unserialized = pyxser.unserialize(serialized)
        print "3. Unserialized Object:\n" + repr(unserialized) + "\n\n"

        thisb = testpkg.sample.TestAnotherObject()
        thisb.first_element = "456"
        thisb.second_element = "789"

        serialized = pyxser.serialize(thisb)
        print "4. Serilized Object:\n" + serialized
        print "Serilized Object Validation:\n", pyxser.validate(serialized)
        unserialized = pyxser.unserialize(serialized)
        print "4. Unserialized Object:\n" + repr(unserialized) + "\n\n"

        thisc = testpkg.sample.TestAnotherObject()
        thisc.first_element = "XXX"
        thisc.second_element = thisb

        serialized = pyxser.serialize(thisc)
        print "5. Serilized Object:\n" + serialized
        print "Serilized Object Validation:\n", pyxser.validate(serialized)
        unserialized = pyxser.unserialize(serialized)
        print "5. Unserialized Object:\n" + repr(unserialized) + "\n\n"

    except Exception, e:
        print "-" * 60
        traceback.print_exc(file=sys.stdout)
        print "-" * 60

