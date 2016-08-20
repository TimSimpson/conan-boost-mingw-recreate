#define BOOST_TEST_MODULE ACME_TEST
#include <boost/test/unit_test.hpp>
#include "acme.h"

BOOST_AUTO_TEST_CASE(test_number_factory) {
    HelperManagerContextService hmcs;
    BOOST_REQUIRE_EQUAL(5, hmcs.number_factory());
}
